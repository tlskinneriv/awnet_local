"""Support for Ambient Weather Station binary sensors."""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import AmbientWeatherEntity
from .const import ATTR_LAST_DATA, DOMAIN, ATTR_KNOWN_SENSORS
from .const_binary_sensor import BINARY_SENSOR_DESCRIPTIONS
from .helpers import AmbientBinarySensorDescription


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Ambient PWS binary sensors based on a config entry."""
    ambient = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            AmbientWeatherBinarySensor(ambient, description)
            for description in BINARY_SENSOR_DESCRIPTIONS
            if description.key in ambient.station[ATTR_KNOWN_SENSORS]
        ]
    )


class AmbientWeatherBinarySensor(AmbientWeatherEntity, BinarySensorEntity):
    """Define an Ambient binary sensor."""

    entity_description: AmbientBinarySensorDescription

    @callback
    def update_from_latest_data(self) -> None:
        """Fetch new state data for the entity."""
        raw = self._ambient.station[ATTR_LAST_DATA].get(self.entity_description.key)
        if raw is not None:
            self._attr_is_on = raw == self.entity_description.on_state
