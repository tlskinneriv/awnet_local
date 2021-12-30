"""The Ambient Weather Local integration"""

import logging

from homeassistant import core, config_entries
from homeassistant.core import Event, HomeAssistant, callback
from homeassistant.helpers.entity import DeviceInfo, Entity, EntityDescription

from .const import DOMAIN

from homeassistant.const import (
    ATTR_LOCATION,
    ATTR_NAME,
    CONF_API_KEY,
    EVENT_HOMEASSISTANT_STOP,
    Platform,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    
    async def async_handle_update(call):
        """Handle the service call"""
        _LOGGER.info('called the service')
        mac = call.data.get('PASSKEY', '')
        _LOGGER.info(f'mac is {mac}')
    
    hass.services.async_register(DOMAIN, "update", async_handle_update)
    
    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


class AmbientWeatherEntity(Entity):
    """Define a base Ambient PWS entity."""

    _attr_should_poll = False

    def __init__(
        self,
        mac_address: str,
        station_name: str,
        description: EntityDescription,
    ) -> None:
        """Initialize the entity."""
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
            self._attr_available = False
            self.update_from_latest_data()
            self.async_write_ha_state()

        self.update_from_latest_data()

    @callback
    def update_from_latest_data(self, raw=None) -> None:
        """Update the entity from the latest data."""
        raise NotImplementedError