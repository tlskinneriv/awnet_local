"""Support for Ambient Weather Station weather entity."""

from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.components.weather import (
    WeatherEntity,
    WeatherEntityDescription,
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
    ATTR_CONDITION_WINDY_VARIANT,
)

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from homeassistant.const import (
    UnitOfPressure,
    UnitOfSpeed,
    UnitOfTemperature,
)

from . import AmbientWeatherEntity
from .const import (
    ATTR_LAST_DATA,
    DOMAIN,
)

from .const_sensor import (
    CALCULATED_SENSOR_TYPES,
    TYPE_BAROMRELIN,
    TYPE_DEWPOINT,
    TYPE_FEELSLIKE,
    TYPE_HUMIDITY,
    TYPE_TEMPF,
    TYPE_WINDDIR,
    TYPE_WINDGUSTMPH,
    TYPE_WINDSPEEDMPH,
    TYPE_HOURLYRAININ,
    TYPE_SOLARRADIATION,
    TYPE_LIGHTNING_TIME,
    TYPE_DATEUTC,
)

from .helpers_calc import AmbientSensorCalculations, AmbientSensorConversions

_LOGGER = logging.getLogger(__name__)

WEATHER_ATTR_MAPPING = [
    ("native_temperature", float, TYPE_TEMPF),
    ("native_apparent_temperature", float, TYPE_FEELSLIKE),
    ("native_dew_point", float, TYPE_DEWPOINT),
    ("native_pressure", float, TYPE_BAROMRELIN),
    ("humidity", float, TYPE_HUMIDITY),
    ("native_wind_gust_speed", float, TYPE_WINDGUSTMPH),
    ("native_wind_speed", float, TYPE_WINDSPEEDMPH),
    ("wind_bearing", float, TYPE_WINDDIR),
]

WEATHER_POURING_RATE = 0.15
WEATHER_LIGHT_LEVEL_NIGHT = 0.02
WEATHER_MODERATE_WINDSPEED = 7.0
WEATHER_LIGHT_LEVEL_CLOUDY = 200.0
WEATHER_LIGHT_LEVEL_PARTLYCLOUDY = 100.0


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Ambient PWS sensors based on a config entry."""
    ambient = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            AmbientWeatherWeather(
                ambient,
                WeatherEntityDescription(key="weather", name="Weather"),
            )
        ]
    )


class AmbientWeatherWeather(AmbientWeatherEntity, WeatherEntity):
    """Define an Ambient Weather weather entity."""

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._attr_available = True

        # default unknown condition and temp
        self._attr_condition = None
        self._attr_native_temperature = None

        # native units
        self._attr_native_temperature_unit = UnitOfTemperature.FAHRENHEIT
        self._attr_native_pressure_unit = UnitOfPressure.INHG
        self._attr_native_wind_speed_unit = UnitOfSpeed.MILES_PER_HOUR

    def set_weather_attr(
        self,
        attribute: str,
        attr_type: type,
        key: str,
    ) -> None:
        """From a set of mapping to attributes, set the appropriate attribute on the entity based on
        the sensor key"""
        station_data = self._ambient.station[ATTR_LAST_DATA]
        if key in CALCULATED_SENSOR_TYPES:
            if all(
                station_data.get(x) is not None for x in CALCULATED_SENSOR_TYPES[key]
            ):
                # calculation of sensor values
                value = AmbientSensorCalculations.calculate(key, self._ambient.station)
            else:
                value = None
        else:
            value = station_data.get(key)
        raw = attr_type(value) if value is not None else None
        setattr(self, attribute, raw)

    @callback
    def update_from_latest_data(self) -> None:
        """Fetch new state data for the entity."""
        self._attr_available = True

        # fill condition attributes
        for attr_data in WEATHER_ATTR_MAPPING:
            self.set_weather_attr("_attr_" + attr_data[0], attr_data[1], attr_data[2])

        # current condition

        # we can loosely predict the following conditions with the basic sensor data that we get
        # from the weather station: clear-night, cloudy, lightning & lightning-rainy (if lightning
        # sensor exists), partlycloudy, pouring, rainy, sunny, windy, windy-variant

        # get the data we'll use to determine the condition
        station_data = self._ambient.station[ATTR_LAST_DATA]
        light_level = float(station_data.get(TYPE_SOLARRADIATION, 0.0))  # w/m^2
        _LOGGER.debug("light level: %s", light_level)
        rain_rate = float(station_data.get(TYPE_HOURLYRAININ, 0.0))  # in/hr
        _LOGGER.debug("rain rate: %s", rain_rate)
        wind_speed = float(station_data.get(TYPE_WINDSPEEDMPH, 0.0))  # mi/hr)
        _LOGGER.debug("wind speed: %s", wind_speed)
        last_lightning = AmbientSensorConversions.convert(
            TYPE_LIGHTNING_TIME, station_data.get(TYPE_LIGHTNING_TIME, 0)
        )
        now = AmbientSensorConversions.convert(
            TYPE_DATEUTC, station_data.get(TYPE_DATEUTC)
        )
        _LOGGER.debug("last_lightning: %s", last_lightning)
        _LOGGER.debug("now: %s", now)

        # set binaries for comparisons
        is_rainy = rain_rate > 0.0
        is_pouring = rain_rate >= WEATHER_POURING_RATE
        is_night = light_level <= WEATHER_LIGHT_LEVEL_NIGHT
        is_windy = wind_speed >= WEATHER_MODERATE_WINDSPEED
        is_cloudy = (
            light_level >= WEATHER_LIGHT_LEVEL_CLOUDY
            and light_level < WEATHER_LIGHT_LEVEL_PARTLYCLOUDY
        )
        is_partlycloudy = light_level >= WEATHER_LIGHT_LEVEL_PARTLYCLOUDY
        is_lightning = now - last_lightning <= timedelta(minutes=10)

        # start condition as sunny until we determine otherwise
        condition = ATTR_CONDITION_SUNNY
        if is_partlycloudy:
            condition = ATTR_CONDITION_PARTLYCLOUDY
        if is_cloudy:
            condition = ATTR_CONDITION_CLOUDY
        if is_night:
            condition = ATTR_CONDITION_CLEAR_NIGHT
        if is_windy:
            condition = ATTR_CONDITION_WINDY
        if is_windy and is_cloudy:
            condition = ATTR_CONDITION_WINDY_VARIANT
        if is_rainy:
            condition = ATTR_CONDITION_RAINY
        if is_pouring:
            condition = ATTR_CONDITION_POURING
        if is_lightning and not is_rainy:
            condition = ATTR_CONDITION_LIGHTNING
        if is_lightning and is_rainy:
            condition = ATTR_CONDITION_LIGHTNING_RAINY

        self._attr_condition = condition
