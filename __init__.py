"""The Ambient Weather Local integration"""

import logging
from .const_types import SUPPORTED_SENSOR_TYPES, SUPPORTED_BINARY_SENSOR_TYPES, TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX

from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect, async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo, Entity, EntityDescription

from .const import (
    ATTR_LAST_DATA,
    ATTR_PASSKEY,
    CONF_MAC,
    CONF_NAME,
    DOMAIN,
)

from homeassistant.const import (
    ATTR_NAME,
    Platform,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:

    if not entry.unique_id:
        hass.config_entries.async_update_entry(
            entry, unique_id=entry.data[CONF_MAC]
        )

    ambient = AmbientStation(
        hass,
        entry
    )

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = ambient

    async def async_handle_update(call):
        """Handle the service call"""
        _LOGGER.debug('Called async_handle_update with %s', call)
        mac = format_mac(call.data.get('PASSKEY', None))
        if mac is None:
            _LOGGER.error('Message is malformed (missing PASSKEY); not updating any entities')
        if mac not in hass.data[DOMAIN][entry.entry_id].stations:
            _LOGGER.warning('Data received for %s that is not our MAC', mac)
        _LOGGER.debug('Last data: %s', hass.data[DOMAIN][entry.entry_id].stations.get(mac, None))
        hass.data[DOMAIN][entry.entry_id].on_data(call.data)

    hass.services.async_register(DOMAIN, "update", async_handle_update)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload an Ambient PWS config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return unload_ok

class AmbientStation:
    """Define a class to handle the Ambient local updates."""

    def __init__(
        self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        self._entry = entry
        self._entry_setup_complete = False
        self._hass = hass
        self.stations: dict[str, dict] = {}

        self.add_station(entry.data[CONF_MAC], entry.data[CONF_NAME])

    def add_station(self, mac: str, name: str) -> None:
        if mac not in self.stations:
            self.stations.setdefault(mac, {})
            self.stations[mac][ATTR_NAME] = name
            self.stations[mac].setdefault(ATTR_LAST_DATA, {})
            for attr_type in (SUPPORTED_SENSOR_TYPES + SUPPORTED_BINARY_SENSOR_TYPES):
                self.stations[mac][ATTR_LAST_DATA][attr_type] = None
            if not self._entry_setup_complete:
                self._hass.config_entries.async_setup_platforms(self._entry, PLATFORMS)
                self._entry_setup_complete = True

    def on_data(self, data: dict) -> None:
        _LOGGER.info('Processing data')
        mac = format_mac(data[ATTR_PASSKEY])
        _LOGGER.info("MAC address: %s", mac)
        _LOGGER.debug("New data received: %s", data)
        extracted_data = {key: value for key, value in data.items() if key in (SUPPORTED_SENSOR_TYPES + SUPPORTED_BINARY_SENSOR_TYPES)}
        if extracted_data == self.stations[mac][ATTR_LAST_DATA]:
            return
        self.stations[mac][ATTR_LAST_DATA] = extracted_data
        async_dispatcher_send(self._hass, f"{DOMAIN}_data_update_{mac}")


class AmbientWeatherEntity(Entity):
    """Define a base Ambient PWS entity."""

    _attr_should_poll = False

    def __init__(
        self,
        ambient: AmbientStation,
        mac_address: str,
        station_name: str,
        description: EntityDescription,
    ) -> None:
        """Initialize the entity."""
        self._ambient = ambient

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, mac_address)},
            manufacturer="Ambient Weather",
            name=station_name,
        )

        self._attr_name = f"{station_name}_{description.name}"
        self._attr_unique_id = f"{mac_address}_{description.key}"
        self._mac_address = mac_address
        self.entity_description = description

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""

        @callback
        def update() -> None:
            """Update the state."""
            if self.entity_description.key == TYPE_SOLARRADIATION_LX:
                self._attr_available = (
                    self._ambient.stations[self._mac_address][ATTR_LAST_DATA][
                        TYPE_SOLARRADIATION
                    ]
                    is not None
                )
            else:
                self._attr_available = (
                    self._ambient.stations[self._mac_address][ATTR_LAST_DATA][
                        self.entity_description.key
                    ]
                    is not None
                )

            self.update_from_latest_data()
            self.async_write_ha_state()

        self.async_on_remove(
            async_dispatcher_connect(
                self.hass, f"{DOMAIN}_data_update_{self._mac_address}", update
            )
        )

        self.update_from_latest_data()

    @callback
    def update_from_latest_data(self) -> None:
        """Update the entity from the latest data."""
        raise NotImplementedError