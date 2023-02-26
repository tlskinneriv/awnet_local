"""The Ambient Weather Local integration"""

import logging
import re

from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_NAME,
    Platform,
)
from homeassistant.helpers.device_registry import format_mac
from homeassistant.helpers.dispatcher import (
    async_dispatcher_connect,
    async_dispatcher_send,
)
from homeassistant.helpers.entity import DeviceInfo, Entity, EntityDescription

from .const import (
    ATTR_LAST_DATA,
    ATTR_PASSKEY,
    ATTR_MAC,
    ATTR_KNOWN_SENSORS,
    ATTR_SENSOR_UPDATE_IN_PROGRESS,
    CONF_MAC,
    CONF_NAME,
    DOMAIN,
    MAC_REGEX,
)

from .const_binary_sensor import (
    SUPPORTED_BINARY_SENSOR_TYPES,
)

from .const_sensor import (
    SUPPORTED_SENSOR_TYPES,
    CALCULATED_SENSOR_TYPES,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setup the integration based on configuration data. Register the service."""
    if not entry.unique_id:
        hass.config_entries.async_update_entry(entry, unique_id=entry.data[CONF_MAC])

    ambient = AmbientStation(hass, entry)

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = ambient

    async def async_handle_update(call):
        """Handle the service call"""
        _LOGGER.debug("Called async_handle_update with %s", call)
        mac = None
        data = call.data
        if ATTR_PASSKEY in data:
            mac = format_mac(data[ATTR_PASSKEY])
        elif ATTR_MAC in data:
            mac = format_mac(data[ATTR_MAC])
        if mac:
            if not re.search(MAC_REGEX, mac):
                _LOGGER.error(
                    "MAC address not in correct format. Parsed MAC: %s. "
                    "Expected formats: 000000000000, 00:00:00:00:00:00, 00-00-00-00-00-00 or "
                    "0000.0000.0000",
                    mac,
                )
                return
        else:
            _LOGGER.error("MAC address not found in data. Raw data: %s", data)
            return

        real_entry = entry
        if mac not in hass.data[DOMAIN][entry.entry_id].stations:
            _LOGGER.debug(
                "Data received for %s that is not this entry's MAC. Try to find the other entry.",
                mac,
            )
            config_entries = hass.config_entries.async_entries(DOMAIN)
            config_entry_for_mac = [x for x in config_entries if x.unique_id == mac]
            if len(config_entry_for_mac) == 0:
                _LOGGER.warning(
                    "Data received for %s does not belong to any config entries", mac
                )
                return
            _LOGGER.debug("Found real entry for %s", mac)
            real_entry = config_entry_for_mac[0]

        _LOGGER.info(
            "Last data: %s",
            hass.data[DOMAIN][real_entry.entry_id].stations.get(mac, None),
        )
        await hass.data[DOMAIN][real_entry.entry_id].async_on_data(mac, call.data)

    hass.services.async_register(DOMAIN, "update", async_handle_update)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload an Ambient PWS config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return unload_ok


class AmbientStation:
    """Define a class to handle the Ambient local updates."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        self._entry = entry
        self._entry_setup_complete = False
        self._hass = hass
        self.stations: dict[str, dict] = {}

        self.add_station(entry.data[CONF_MAC], entry.data[CONF_NAME])

    def add_station(self, mac: str, name: str) -> None:
        """Add a station to the list of stations in the integration data; currently the integration
        only supports 1 as configured from the UI."""
        if mac not in self.stations:
            self.stations.setdefault(mac, {})
            self.stations[mac][ATTR_NAME] = name
            self.stations[mac].setdefault(ATTR_LAST_DATA, {})
            self.stations[mac].setdefault(ATTR_KNOWN_SENSORS, [])
            self.stations[mac][ATTR_SENSOR_UPDATE_IN_PROGRESS] = False
            if not self._entry_setup_complete:
                self._hass.config_entries.async_setup_platforms(self._entry, PLATFORMS)
                self._entry_setup_complete = True

    async def async_on_data(self, mac: str, data: dict) -> None:
        """Processes the data from the incoming service call to update the sensors."""
        _LOGGER.info("Processing data")
        _LOGGER.info("MAC address: %s", mac)
        _LOGGER.debug("New data received: %s", data)
        extracted_data = {
            key: value
            for key, value in data.items()
            if key in (SUPPORTED_SENSOR_TYPES + SUPPORTED_BINARY_SENSOR_TYPES)
        }
        if (
            extracted_data == self.stations[mac][ATTR_LAST_DATA]
            and not self.stations[mac][ATTR_SENSOR_UPDATE_IN_PROGRESS]
        ):
            return
        self.stations[mac][ATTR_LAST_DATA] = extracted_data
        known_sensors = list(
            set(self.stations[mac][ATTR_KNOWN_SENSORS] + list(extracted_data.keys()))
        )
        _LOGGER.info(
            "Previously known sensors: %s", self.stations[mac][ATTR_KNOWN_SENSORS]
        )
        _LOGGER.info("Now known sensors: %s", known_sensors)
        if known_sensors != self.stations[mac][ATTR_KNOWN_SENSORS]:
            self.stations[mac][ATTR_KNOWN_SENSORS] = known_sensors
            await self._hass.config_entries.async_unload_platforms(
                self._entry, PLATFORMS
            )
            await self._hass.config_entries.async_forward_entry_setups(
                self._entry, PLATFORMS
            )
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
        self._attr_has_entity_name = True
        self._attr_name = f"{description.name}"
        self._attr_unique_id = f"{mac_address}_{description.key}"
        self._mac_address = mac_address
        self._attr_available = False
        self.entity_description = description

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""

        @callback
        def update() -> None:
            """Update the state."""
            last_data = self._ambient.stations[self._mac_address][ATTR_LAST_DATA]

            if self.entity_description.key in CALCULATED_SENSOR_TYPES:
                # if we are a calculated sensor type, report available only if all our dependencies
                # are available
                self._attr_available = all(
                    last_data.get(x) is not None
                    for x in CALCULATED_SENSOR_TYPES[self.entity_description.key]
                )
            else:
                self._attr_available = (
                    last_data.get(self.entity_description.key) is not None
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
