"""The Ambient Weather Local integration"""

import logging
import re
from typing import Any

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
from homeassistant.helpers.entity import DeviceInfo, EntityDescription
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.helpers.storage import Store

from .const import (
    ATTR_LAST_DATA,
    ATTR_PASSKEY,
    ATTR_MAC,
    ATTR_KNOWN_SENSORS,
    ATTR_SENSOR_UPDATE_IN_PROGRESS,
    ATTR_STATIONTYPE,
    CONF_MAC,
    CONF_NAME,
    DOMAIN,
    MAC_REGEX,
    ATTR_LIGHTNING_DATA,
)

from .const_binary_sensor import (
    SUPPORTED_BINARY_SENSOR_TYPES,
)

from .const_sensor import (
    SUPPORTED_SENSOR_TYPES,
    CALCULATED_SENSOR_TYPES,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR, Platform.WEATHER]
STORAGE_KEY = DOMAIN + "_data"
STORAGE_VERSION = 1


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
        if mac != entry.unique_id:
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
            hass.data[DOMAIN][real_entry.entry_id].station,
        )
        await hass.data[DOMAIN][real_entry.entry_id].async_on_data(mac, call.data)

    hass.services.async_register(DOMAIN, "update", async_handle_update)

    await ambient.async_load()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload an Ambient PWS config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        await hass.data[DOMAIN][entry.entry_id].async_unload()
    return unload_ok


class AmbientStation:
    """Define a class to handle the Ambient local updates."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        self._entry = entry
        self._hass = hass
        self.station: dict[str, Any] = {}

        self.station[ATTR_MAC] = entry.data[CONF_MAC]
        self.station[ATTR_NAME] = entry.data[CONF_NAME]
        self.station.setdefault(ATTR_LAST_DATA, {})
        self.station.setdefault(ATTR_KNOWN_SENSORS, [])
        self.station.setdefault(ATTR_LIGHTNING_DATA, {})
        self.station[ATTR_SENSOR_UPDATE_IN_PROGRESS] = False
        self.station[ATTR_STATIONTYPE] = ""
        self._old_storage_key = f"{STORAGE_KEY}_{self.station[ATTR_MAC]}"
        self._storage_key = f"{STORAGE_KEY}_{self.station[ATTR_MAC].replace(':','')}"
        self._old_store: Store = Store(hass, STORAGE_VERSION, self._old_storage_key)
        self._store: Store = Store(hass, STORAGE_VERSION, self._storage_key)
        self._update_event_handle = f"{DOMAIN}_data_update_{self.station[ATTR_MAC]}"

    @property
    def update_event_handle(self) -> str:
        """Returns the update event handle for the instance"""
        return self._update_event_handle

    async def async_load(self) -> None:
        """Load data for station from datastore"""
        _LOGGER.info("Loading data for integration")
        if (data := await self._old_store.async_load()) is not None:
            _LOGGER.info("Data being migrated to new storage key: %s", data)
            if isinstance(data, list):
                self.station[ATTR_KNOWN_SENSORS] = data
                self.station[ATTR_LIGHTNING_DATA] = {}
            elif isinstance(data, dict):
                self.station[ATTR_KNOWN_SENSORS] = data.get(ATTR_KNOWN_SENSORS, None)
                self.station[ATTR_LIGHTNING_DATA] = data.get(ATTR_LIGHTNING_DATA, None)
            else:
                self.station[ATTR_KNOWN_SENSORS] = {}
                self.station[ATTR_LIGHTNING_DATA] = {}
            _LOGGER.info("Data being saved into new storage key")
            await self._store.async_save(
                {
                    ATTR_KNOWN_SENSORS: self.station[ATTR_KNOWN_SENSORS],
                    ATTR_LIGHTNING_DATA: self.station[ATTR_LIGHTNING_DATA],
                }
            )
            _LOGGER.info("Old storage key being removed")
            await self._old_store.async_remove()
        if (data := await self._store.async_load()) is not None:
            _LOGGER.info("Data being restored: %s", data)
            # handle old style data if that's what we have saved
            if isinstance(data, list):
                self.station[ATTR_KNOWN_SENSORS] = data
                self.station[ATTR_LIGHTNING_DATA] = {}
            elif isinstance(data, dict):
                self.station[ATTR_KNOWN_SENSORS] = data.get(ATTR_KNOWN_SENSORS, None)
                self.station[ATTR_LIGHTNING_DATA] = data.get(ATTR_LIGHTNING_DATA, None)
            else:
                self.station[ATTR_KNOWN_SENSORS] = {}
                self.station[ATTR_LIGHTNING_DATA] = {}

    async def async_unload(self) -> None:
        """Remove all data for the station from the datastore"""
        _LOGGER.info("Removing all stored data")
        await self._store.async_remove()

    async def async_on_data(self, mac: str, data: dict) -> None:
        """Processes the data from the incoming service call to update the sensors."""
        _LOGGER.info("Processing data")
        _LOGGER.info("MAC address: %s", mac)
        _LOGGER.debug("New data received: %s", data)
        self.station[ATTR_STATIONTYPE] = data.get(ATTR_STATIONTYPE, "")
        extracted_data = {
            key: value
            for key, value in data.items()
            if key in (SUPPORTED_SENSOR_TYPES + SUPPORTED_BINARY_SENSOR_TYPES)
        }
        if (
            extracted_data == self.station[ATTR_LAST_DATA]
            and not self.station[ATTR_SENSOR_UPDATE_IN_PROGRESS]
        ):
            _LOGGER.info("Data received is the same as last received, not updating")
            return
        self.station[ATTR_LAST_DATA] = extracted_data
        known_calc_sensors = [
            key
            for key, value in CALCULATED_SENSOR_TYPES.items()
            if all(x in list(extracted_data.keys()) for x in value)
        ]
        _LOGGER.debug("Known calc'd sensor types: %s", known_calc_sensors)
        known_sensors_set = set(
            self.station[ATTR_KNOWN_SENSORS]
            + known_calc_sensors
            + list(extracted_data.keys())
        )
        new_sensors = list(
            known_sensors_set.difference(set(self.station[ATTR_KNOWN_SENSORS]))
        )

        _LOGGER.debug("New sensors to add: %s", new_sensors)
        if new_sensors:
            self.station[ATTR_KNOWN_SENSORS] = list(known_sensors_set)
            await self._hass.config_entries.async_unload_platforms(
                self._entry, PLATFORMS
            )
            await self._hass.config_entries.async_forward_entry_setups(
                self._entry, PLATFORMS
            )

        # Store the data off
        await self._store.async_save(
            {
                ATTR_KNOWN_SENSORS: self.station[ATTR_KNOWN_SENSORS],
                ATTR_LIGHTNING_DATA: self.station[ATTR_LIGHTNING_DATA],
            }
        )
        async_dispatcher_send(self._hass, self.update_event_handle)


class AmbientWeatherEntity(RestoreEntity):
    """Define a base Ambient PWS entity."""

    _attr_should_poll = False

    def __init__(
        self,
        ambient: AmbientStation,
        description: EntityDescription,
    ) -> None:
        """Initialize the entity."""
        self._ambient = ambient

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, ambient.station[ATTR_MAC])},
            manufacturer="Ambient Weather",
            model="Weather Station",
            sw_version=self._ambient.station[ATTR_STATIONTYPE],
            name=ambient.station[ATTR_NAME],
        )
        self._attr_has_entity_name = True
        self._attr_name = f"{description.name}"
        self._attr_unique_id = f"{ambient.station[ATTR_MAC]}_{description.key}"
        self._attr_available = False
        self.entity_description = description

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""

        async_dispatcher_connect(
            self.hass,
            self._ambient.update_event_handle,
            self.update,
        )

    @callback
    def update_from_latest_data(self) -> None:
        """Update the entity from the latest data."""
        raise NotImplementedError

    @callback
    def update(self) -> None:
        """Update the state."""
        last_data = self._ambient.station[ATTR_LAST_DATA]

        self._attr_available = last_data.get(self.entity_description.key) is not None

        self.update_from_latest_data()
        self.async_write_ha_state()
