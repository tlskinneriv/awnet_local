"""Support for Ambient Weather Station sensors."""
from __future__ import annotations

from datetime import datetime
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import ATTR_NAME

from . import AmbientStation, AmbientWeatherEntity
from .const import (
    ATTR_LAST_DATA,
    DOMAIN,
)
from .const_types import (
    SENSOR_DESCRIPTIONS,
    TYPE_LASTRAIN,
    TYPE_SOLARRADIATION_LX,
)

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

    def __init__(
        self,
        ambient: AmbientStation,
        mac_address: str,
        station_name: str,
        description: EntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(ambient, mac_address, station_name, description)

        if description.key == TYPE_SOLARRADIATION_LX:
            # Since TYPE_SOLARRADIATION and TYPE_SOLARRADIATION_LX will have the same
            # name in the UI, we influence the entity ID of TYPE_SOLARRADIATION_LX here
            # to differentiate them:
            self.entity_id = f"sensor.{station_name}_solar_rad_lx"

    @callback
    def update_from_latest_data(self) -> None:
        """Fetch new state data for the sensor."""
        raw = self._ambient.stations[self._mac_address][ATTR_LAST_DATA].get(
            self.entity_description.key
        )
        if raw is not None:
            if self.entity_description.key == TYPE_LASTRAIN:
                self._attr_native_value = datetime.strptime(
                    raw, "%Y-%m-%dT%H:%M:%S.%f%z"
                )
            else:
                self._attr_native_value = raw
