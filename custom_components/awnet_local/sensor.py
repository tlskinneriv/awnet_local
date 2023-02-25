"""Support for Ambient Weather Station sensors."""

from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import ATTR_NAME

from . import AmbientWeatherEntity
from .const import (
    ATTR_LAST_DATA,
    DOMAIN,
)
from .const_sensor import (
    CALCULATED_SENSOR_TYPES,
    SENSOR_DESCRIPTIONS,
    CONVERTED_SENSOR_TYPES,
)

from .helpers_calc import AmbientSensorCalculations, AmbientSensorConversions

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Ambient PWS sensors based on a config entry."""
    ambient = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            AmbientWeatherSensor(ambient, mac_address, station[ATTR_NAME], description)
            for mac_address, station in ambient.stations.items()
            for description in SENSOR_DESCRIPTIONS
            if description.key in station[ATTR_LAST_DATA]
        ]
    )


class AmbientWeatherSensor(AmbientWeatherEntity, SensorEntity):
    """Define an Ambient sensor."""

    @callback
    def update_from_latest_data(self) -> None:
        """Fetch new state data for the sensor."""
        station_data = self._ambient.stations[self._mac_address][ATTR_LAST_DATA]
        raw = station_data.get(self.entity_description.key)

        # calculation of sensor values
        if (
            self.entity_description.key in CALCULATED_SENSOR_TYPES
            and self._attr_available
        ):
            raw = AmbientSensorCalculations.calculate(
                self.entity_description.key, station_data
            )

        if raw is not None:
            # conversion of native units to HA supported units
            if self.entity_description.key in CONVERTED_SENSOR_TYPES:
                raw = AmbientSensorConversions.convert(self.entity_description.key, raw)

            self._attr_native_value = raw
