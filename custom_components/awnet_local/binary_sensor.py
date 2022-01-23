"""Support for Ambient Weather Station binary sensors."""
from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_NAME
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import AmbientWeatherEntity
from .const import ATTR_LAST_DATA, DOMAIN
from .const_types import BINARY_SENSOR_DESCRIPTIONS
from .helpers import AmbientBinarySensorDescription

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Ambient PWS binary sensors based on a config entry."""
    ambient = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            AmbientWeatherBinarySensor(
                ambient, mac_address, station[ATTR_NAME], description
            )
            for mac_address, station in ambient.stations.items()
            for description in BINARY_SENSOR_DESCRIPTIONS
            if description.key in station[ATTR_LAST_DATA]
        ]
    )


class AmbientWeatherBinarySensor(AmbientWeatherEntity, BinarySensorEntity):
    """Define an Ambient binary sensor."""

    entity_description: AmbientBinarySensorDescription

    @callback
    def update_from_latest_data(self) -> None:
        """Fetch new state data for the entity."""
        self._attr_is_on = (
            self._ambient.stations[self._mac_address][ATTR_LAST_DATA][
                self.entity_description.key
            ]
            == self.entity_description.on_state
        )
