"""Support for Ambient Weather Station sensors."""

from __future__ import annotations

import logging

from homeassistant.components.sensor import RestoreSensor
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import AmbientWeatherEntity
from .const import (
    ATTR_LAST_DATA,
    ATTR_KNOWN_SENSORS,
    DOMAIN,
)
from .const_sensor import (
    CALCULATED_SENSOR_TYPES,
    SENSOR_DESCRIPTIONS,
    CONVERTED_SENSOR_TYPES,
    RESTORE_SENSOR_TYPES,
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
            AmbientWeatherSensor(ambient, description)
            for description in SENSOR_DESCRIPTIONS
            if description.key in ambient.station[ATTR_KNOWN_SENSORS]
        ]
    )


class AmbientWeatherSensor(AmbientWeatherEntity, RestoreSensor):
    """Define an Ambient sensor."""

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()

        if self.entity_description.key in RESTORE_SENSOR_TYPES:
            state = await self.async_get_last_sensor_data()
            _LOGGER.debug("State to restore for %s was %s", self.name, state)
            if not state:
                return
            self._attr_native_value = state.native_value
            self._attr_available = True

        if self.entity_description.key in CALCULATED_SENSOR_TYPES:
            self._attr_available = True

    @callback
    def update_from_latest_data(self) -> None:
        """Fetch new state data for the sensor."""
        station_data = self._ambient.station[ATTR_LAST_DATA]
        raw = station_data.get(self.entity_description.key)

        if self.entity_description.key in CALCULATED_SENSOR_TYPES:
            self._attr_available = True

        if self.entity_description.key in CALCULATED_SENSOR_TYPES:
            # if we are a calculated sensor type, report available only if all our dependencies
            # are available
            if all(
                station_data.get(x) is not None
                for x in CALCULATED_SENSOR_TYPES[self.entity_description.key]
            ):
                # calculation of sensor values
                value = AmbientSensorCalculations.calculate(
                    self.entity_description.key, self._ambient.station
                )
                if value is not None:
                    raw = value
                else:
                    raw = self._attr_native_value
            else:
                raw = None

        # conversion of native units to HA supported units
        elif raw is not None and self.entity_description.key in CONVERTED_SENSOR_TYPES:
            raw = AmbientSensorConversions.convert(self.entity_description.key, raw)

        self._attr_native_value = raw
