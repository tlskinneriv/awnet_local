"""Support for Ambient Weather Station sensors."""
from __future__ import annotations

from datetime import datetime
import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_NAME,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_MILLION,
    DEGREE,
    IRRADIATION_WATTS_PER_SQUARE_METER,
    LIGHT_LUX,
    PERCENTAGE,
    PRECIPITATION_INCHES,
    PRECIPITATION_INCHES_PER_HOUR,
    PRESSURE_INHG,
    SPEED_MILES_PER_HOUR,
    TEMP_FAHRENHEIT,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import AmbientWeatherEntity
from .const import DOMAIN, CONF_MAC, CONF_NAME
from .const_types import *

_LOGGER = logging.getLogger(__name__)

SUPPORTED_TYPES = [
    TYPE_TEMPINF,
    TYPE_HUMIDITYIN,
    TYPE_BAROMRELIN,
    TYPE_BAROMABSIN,
    TYPE_TEMPF,
    TYPE_HUMIDITY,
    TYPE_WINDDIR,
    TYPE_WINDSPEEDMPH,
    TYPE_WINDGUSTMPH,
    TYPE_MAXDAILYGUST,
    TYPE_HOURLYRAININ,
    TYPE_EVENTRAININ,
    TYPE_DAILYRAININ,
    TYPE_WEEKLYRAININ,
    TYPE_MONTHLYRAININ,
    TYPE_TOTALRAININ,
    TYPE_SOLARRADIATION,
    TYPE_UV
]

SENSOR_DESCRIPTIONS = (
    SensorEntityDescription(
        key=TYPE_24HOURRAININ,
        name="24 Hr Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TYPE_BAROMABSIN,
        name="Abs Pressure",
        native_unit_of_measurement=PRESSURE_INHG,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_BAROMRELIN,
        name="Rel Pressure",
        native_unit_of_measurement=PRESSURE_INHG,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_CO2,
        name="co2",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_DAILYRAININ,
        name="Daily Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TYPE_DEWPOINT,
        name="Dew Point",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_EVENTRAININ,
        name="Event Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_FEELSLIKE,
        name="Feels Like",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HOURLYRAININ,
        name="Hourly Rain Rate",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES_PER_HOUR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY10,
        name="Humidity 10",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY1,
        name="Humidity 1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY2,
        name="Humidity 2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY3,
        name="Humidity 3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY4,
        name="Humidity 4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY5,
        name="Humidity 5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY6,
        name="Humidity 6",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY7,
        name="Humidity 7",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY8,
        name="Humidity 8",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY9,
        name="Humidity 9",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY,
        name="Humidity",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITYIN,
        name="Humidity In",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_LASTRAIN,
        name="Last Rain",
        icon="mdi:water",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key=TYPE_MAXDAILYGUST,
        name="Max Gust",
        icon="mdi:weather-windy",
        native_unit_of_measurement=SPEED_MILES_PER_HOUR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_MONTHLYRAININ,
        name="Monthly Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_24H,
        name="PM25 24h Avg",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_IN,
        name="PM25 Indoor",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_IN_24H,
        name="PM25 Indoor 24h Avg",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
    ),
    SensorEntityDescription(
        key=TYPE_PM25,
        name="PM25",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM10,
        name="Soil Humidity 10",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM1,
        name="Soil Humidity 1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM2,
        name="Soil Humidity 2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM3,
        name="Soil Humidity 3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM4,
        name="Soil Humidity 4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM5,
        name="Soil Humidity 5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM6,
        name="Soil Humidity 6",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM7,
        name="Soil Humidity 7",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM8,
        name="Soil Humidity 8",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM9,
        name="Soil Humidity 9",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP10F,
        name="Soil Temp 10",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP1F,
        name="Soil Temp 1",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP2F,
        name="Soil Temp 2",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP3F,
        name="Soil Temp 3",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP4F,
        name="Soil Temp 4",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP5F,
        name="Soil Temp 5",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP6F,
        name="Soil Temp 6",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP7F,
        name="Soil Temp 7",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP8F,
        name="Soil Temp 8",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP9F,
        name="Soil Temp 9",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOLARRADIATION,
        name="Solar Rad",
        native_unit_of_measurement=IRRADIATION_WATTS_PER_SQUARE_METER,
        device_class=SensorDeviceClass.ILLUMINANCE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOLARRADIATION_LX,
        name="Solar Rad",
        native_unit_of_measurement=LIGHT_LUX,
        device_class=SensorDeviceClass.ILLUMINANCE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP10F,
        name="Temp 10",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP1F,
        name="Temp 1",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP2F,
        name="Temp 2",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP3F,
        name="Temp 3",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP4F,
        name="Temp 4",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP5F,
        name="Temp 5",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP6F,
        name="Temp 6",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP7F,
        name="Temp 7",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP8F,
        name="Temp 8",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP9F,
        name="Temp 9",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMPF,
        name="Temp",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMPINF,
        name="Inside Temp",
        native_unit_of_measurement=TEMP_FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TOTALRAININ,
        name="Lifetime Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_UV,
        name="UV Index",
        native_unit_of_measurement="Index",
        device_class=SensorDeviceClass.ILLUMINANCE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WEEKLYRAININ,
        name="Weekly Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR,
        name="Wind Dir",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_AVG10M,
        name="Wind Dir Avg 10m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_AVG2M,
        name="Wind Dir Avg 2m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
    ),
    SensorEntityDescription(
        key=TYPE_WINDGUSTDIR,
        name="Gust Dir",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
    ),
    SensorEntityDescription(
        key=TYPE_WINDGUSTMPH,
        name="Wind Gust",
        icon="mdi:weather-windy",
        native_unit_of_measurement=SPEED_MILES_PER_HOUR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPDMPH_AVG10M,
        name="Wind Avg 10m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=SPEED_MILES_PER_HOUR,
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPDMPH_AVG2M,
        name="Wind Avg 2m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=SPEED_MILES_PER_HOUR,
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPEEDMPH,
        name="Wind Speed",
        icon="mdi:weather-windy",
        native_unit_of_measurement=SPEED_MILES_PER_HOUR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_YEARLYRAININ,
        name="Yearly Rain",
        icon="mdi:water",
        native_unit_of_measurement=PRECIPITATION_INCHES,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Ambient PWS sensors based on a config entry."""
    _LOGGER.info('in async_setup_entry')
    mac_address = entry.data[CONF_MAC]
    station_name = entry.data[CONF_NAME]
    _LOGGER.info(f'mac is {mac_address}')
    _LOGGER.info(f'station_name is {station_name}')
    async_add_entities(
        [
            AmbientWeatherSensor(mac_address, station_name, description)
            for description in SENSOR_DESCRIPTIONS
            if description.key in SUPPORTED_TYPES
        ]
    )


class AmbientWeatherSensor(AmbientWeatherEntity, SensorEntity):
    """Define an Ambient sensor."""

    def __init__(
        self,
        mac_address: str,
        station_name: str,
        description: EntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(mac_address, station_name, description)

        if description.key == TYPE_SOLARRADIATION_LX:
            # Since TYPE_SOLARRADIATION and TYPE_SOLARRADIATION_LX will have the same
            # name in the UI, we influence the entity ID of TYPE_SOLARRADIATION_LX here
            # to differentiate them:
            self.entity_id = f"sensor.{station_name}_solar_rad_lx"

    @callback
    def update_from_latest_data(self, raw=None) -> None:
        """Fetch new state data for the sensor."""
        if self.entity_description.key == TYPE_LASTRAIN:
            self._attr_native_value = datetime.strptime(raw, "%Y-%m-%dT%H:%M:%S.%f%z")
        else:
            self._attr_native_value = raw