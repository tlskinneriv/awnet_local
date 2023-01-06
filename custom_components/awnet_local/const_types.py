from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)

from homeassistant.const import (
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_MILLION,
    DEGREE,
    IRRADIATION_WATTS_PER_SQUARE_METER,
    LIGHT_LUX,
    PERCENTAGE,
    UnitOfIrradiance,
    UnitOfPrecipitationDepth,
    UnitOfPressure,
    UnitOfSpeed,
    UnitOfTemperature,
    UnitOfVolumetricFlux,
)
from homeassistant.helpers.entity import EntityCategory

from .helpers import AmbientBinarySensorDescription

# Sensor Types
TYPE_24HOURRAININ = "24hourrainin"
TYPE_AQI_PM25 = "aqi_pm25"
TYPE_AQI_PM25_24H = "aqi_pm25_24h"
TYPE_AQI_PM25_IN = "aqi_pm25_in"
TYPE_AQI_PM25_IN_24H = "aqi_pm25_in_24h"
TYPE_BAROMABSIN = "baromabsin"
TYPE_BAROMRELIN = "baromrelin"
TYPE_CO2 = "co2"
TYPE_DAILYRAININ = "dailyrainin"
TYPE_DEWPOINT = "dewPoint"
TYPE_EVENTRAININ = "eventrainin"
TYPE_FEELSLIKE = "feelsLike"
TYPE_HOURLYRAININ = "hourlyrainin"
TYPE_HUMIDITY = "humidity"
TYPE_HUMIDITY1 = "humidity1"
TYPE_HUMIDITY10 = "humidity10"
TYPE_HUMIDITY2 = "humidity2"
TYPE_HUMIDITY3 = "humidity3"
TYPE_HUMIDITY4 = "humidity4"
TYPE_HUMIDITY5 = "humidity5"
TYPE_HUMIDITY6 = "humidity6"
TYPE_HUMIDITY7 = "humidity7"
TYPE_HUMIDITY8 = "humidity8"
TYPE_HUMIDITY9 = "humidity9"
TYPE_HUMIDITYIN = "humidityin"
TYPE_LASTRAIN = "lastRain"
TYPE_LIGHTNING_PER_DAY = "lightning_day"
TYPE_LIGHTNING_PER_HOUR = "lightning_hour"
TYPE_MAXDAILYGUST = "maxdailygust"
TYPE_MONTHLYRAININ = "monthlyrainin"
TYPE_PM25 = "pm25"
TYPE_PM25_24H = "pm25_24h"
TYPE_PM25_IN = "pm25_in"
TYPE_PM25_IN_24H = "pm25_in_24h"
TYPE_SOILHUM1 = "soilhum1"
TYPE_SOILHUM10 = "soilhum10"
TYPE_SOILHUM2 = "soilhum2"
TYPE_SOILHUM3 = "soilhum3"
TYPE_SOILHUM4 = "soilhum4"
TYPE_SOILHUM5 = "soilhum5"
TYPE_SOILHUM6 = "soilhum6"
TYPE_SOILHUM7 = "soilhum7"
TYPE_SOILHUM8 = "soilhum8"
TYPE_SOILHUM9 = "soilhum9"
TYPE_SOILTEMP10F = "soiltemp10f"
TYPE_SOILTEMP1F = "soiltemp1f"
TYPE_SOILTEMP2F = "soiltemp2f"
TYPE_SOILTEMP3F = "soiltemp3f"
TYPE_SOILTEMP4F = "soiltemp4f"
TYPE_SOILTEMP5F = "soiltemp5f"
TYPE_SOILTEMP6F = "soiltemp6f"
TYPE_SOILTEMP7F = "soiltemp7f"
TYPE_SOILTEMP8F = "soiltemp8f"
TYPE_SOILTEMP9F = "soiltemp9f"
TYPE_SOLARRADIATION = "solarradiation"
TYPE_SOLARRADIATION_LX = "solarradiation_lx"
TYPE_TEMP10F = "temp10f"
TYPE_TEMP1F = "temp1f"
TYPE_TEMP2F = "temp2f"
TYPE_TEMP3F = "temp3f"
TYPE_TEMP4F = "temp4f"
TYPE_TEMP5F = "temp5f"
TYPE_TEMP6F = "temp6f"
TYPE_TEMP7F = "temp7f"
TYPE_TEMP8F = "temp8f"
TYPE_TEMP9F = "temp9f"
TYPE_TEMPF = "tempf"
TYPE_TEMPINF = "tempinf"
TYPE_TOTALRAININ = "totalrainin"
TYPE_UV = "uv"
TYPE_WEEKLYRAININ = "weeklyrainin"
TYPE_WINDDIR = "winddir"
TYPE_WINDDIR_AVG10M = "winddir_avg10m"
TYPE_WINDDIR_AVG2M = "winddir_avg2m"
TYPE_WINDGUSTDIR = "windgustdir"
TYPE_WINDGUSTMPH = "windgustmph"
TYPE_WINDSPDMPH_AVG10M = "windspdmph_avg10m"
TYPE_WINDSPDMPH_AVG2M = "windspdmph_avg2m"
TYPE_WINDSPEEDMPH = "windspeedmph"
TYPE_YEARLYRAININ = "yearlyrainin"

# Binary Sensor Types
TYPE_BATT1 = "batt1"
TYPE_BATT10 = "batt10"
TYPE_BATT2 = "batt2"
TYPE_BATT3 = "batt3"
TYPE_BATT4 = "batt4"
TYPE_BATT5 = "batt5"
TYPE_BATT6 = "batt6"
TYPE_BATT7 = "batt7"
TYPE_BATT8 = "batt8"
TYPE_BATT9 = "batt9"
TYPE_BATT_CO2 = "batt_co2"
TYPE_BATTIN = "battin"
TYPE_BATTOUT = "battout"
TYPE_PM25_BATT = "batt_25"
TYPE_BATT_LEAK1 = "batleak1"
TYPE_BATT_LEAK2 = "batleak2"
TYPE_BATT_LEAK3 = "batleak3"
TYPE_BATT_LEAK4 = "batleak4"
TYPE_BATT_LIGHTNING = "batt_lightning"
TYPE_BATT_SM1 = "battsm1"
TYPE_BATT_SM10 = "battsm10"
TYPE_BATT_SM2 = "battsm2"
TYPE_BATT_SM3 = "battsm3"
TYPE_BATT_SM4 = "battsm4"
TYPE_BATT_SM5 = "battsm5"
TYPE_BATT_SM6 = "battsm6"
TYPE_BATT_SM7 = "battsm7"
TYPE_BATT_SM8 = "battsm8"
TYPE_BATT_SM9 = "battsm9"
TYPE_LEAK1 = "leak1"
TYPE_LEAK2 = "leak2"
TYPE_LEAK3 = "leak3"
TYPE_LEAK4 = "leak4"
TYPE_PM25IN_BATT = "batt_25in"
TYPE_RELAY1 = "relay1"
TYPE_RELAY10 = "relay10"
TYPE_RELAY2 = "relay2"
TYPE_RELAY3 = "relay3"
TYPE_RELAY4 = "relay4"
TYPE_RELAY5 = "relay5"
TYPE_RELAY6 = "relay6"
TYPE_RELAY7 = "relay7"
TYPE_RELAY8 = "relay8"
TYPE_RELAY9 = "relay9"

SUPPORTED_SENSOR_TYPES = [
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
    TYPE_UV,
    TYPE_24HOURRAININ,
    TYPE_AQI_PM25,
    TYPE_AQI_PM25_24H,
    TYPE_AQI_PM25_IN,
    TYPE_AQI_PM25_IN_24H,
    TYPE_CO2,
    TYPE_DEWPOINT,
    TYPE_FEELSLIKE,
    TYPE_HUMIDITY1,
    TYPE_HUMIDITY10,
    TYPE_HUMIDITY2,
    TYPE_HUMIDITY3,
    TYPE_HUMIDITY4,
    TYPE_HUMIDITY5,
    TYPE_HUMIDITY6,
    TYPE_HUMIDITY7,
    TYPE_HUMIDITY8,
    TYPE_HUMIDITY9,
    TYPE_LASTRAIN,
    TYPE_LIGHTNING_PER_DAY,
    TYPE_LIGHTNING_PER_HOUR,
    TYPE_PM25,
    TYPE_PM25_24H,
    TYPE_PM25_IN,
    TYPE_PM25_IN_24H,
    TYPE_SOILHUM1,
    TYPE_SOILHUM10,
    TYPE_SOILHUM2,
    TYPE_SOILHUM3,
    TYPE_SOILHUM4,
    TYPE_SOILHUM5,
    TYPE_SOILHUM6,
    TYPE_SOILHUM7,
    TYPE_SOILHUM8,
    TYPE_SOILHUM9,
    TYPE_SOILTEMP10F,
    TYPE_SOILTEMP1F,
    TYPE_SOILTEMP2F,
    TYPE_SOILTEMP3F,
    TYPE_SOILTEMP4F,
    TYPE_SOILTEMP5F,
    TYPE_SOILTEMP6F,
    TYPE_SOILTEMP7F,
    TYPE_SOILTEMP8F,
    TYPE_SOILTEMP9F,
    TYPE_SOLARRADIATION_LX,
    TYPE_TEMP10F,
    TYPE_TEMP1F,
    TYPE_TEMP2F,
    TYPE_TEMP3F,
    TYPE_TEMP4F,
    TYPE_TEMP5F,
    TYPE_TEMP6F,
    TYPE_TEMP7F,
    TYPE_TEMP8F,
    TYPE_TEMP9F,
    TYPE_WINDDIR_AVG10M,
    TYPE_WINDDIR_AVG2M,
    TYPE_WINDGUSTDIR,
    TYPE_WINDGUSTMPH,
    TYPE_WINDSPDMPH_AVG10M,
    TYPE_WINDSPDMPH_AVG2M,
    TYPE_YEARLYRAININ,
]

SUPPORTED_BINARY_SENSOR_TYPES = [
    TYPE_BATT_CO2,
    TYPE_BATTOUT,
    TYPE_BATT1,
    TYPE_BATT10,
    TYPE_BATT2,
    TYPE_BATT3,
    TYPE_BATT4,
    TYPE_BATT5,
    TYPE_BATT6,
    TYPE_BATT7,
    TYPE_BATT8,
    TYPE_BATT9,
    TYPE_BATTIN,
    TYPE_PM25_BATT,
    TYPE_BATT_LEAK1,
    TYPE_BATT_LEAK2,
    TYPE_BATT_LEAK3,
    TYPE_BATT_LEAK4,
    TYPE_BATT_LIGHTNING,
    TYPE_BATT_SM1,
    TYPE_BATT_SM10,
    TYPE_BATT_SM2,
    TYPE_BATT_SM3,
    TYPE_BATT_SM4,
    TYPE_BATT_SM5,
    TYPE_BATT_SM6,
    TYPE_BATT_SM7,
    TYPE_BATT_SM8,
    TYPE_BATT_SM9,
    TYPE_LEAK1,
    TYPE_LEAK2,
    TYPE_LEAK3,
    TYPE_LEAK4,
    TYPE_PM25IN_BATT,
    TYPE_RELAY1,
    TYPE_RELAY10,
    TYPE_RELAY2,
    TYPE_RELAY3,
    TYPE_RELAY4,
    TYPE_RELAY5,
    TYPE_RELAY6,
    TYPE_RELAY7,
    TYPE_RELAY8,
    TYPE_RELAY9,
]

# Each sensor listed here is calculated server-side and depends on the list of
# sensors it is a key for
CALCULATED_SENSOR_TYPES = {
    TYPE_LASTRAIN: [TYPE_HOURLYRAININ],
    TYPE_FEELSLIKE: [TYPE_TEMPF, TYPE_WINDSPEEDMPH, TYPE_HUMIDITY],
    TYPE_DEWPOINT: [TYPE_TEMPF, TYPE_HUMIDITY],
    TYPE_SOLARRADIATION_LX: [TYPE_SOLARRADIATION],
}

SENSOR_DESCRIPTIONS = (
    SensorEntityDescription(
        key=TYPE_24HOURRAININ,
        name="24 Hr Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25,
        name="AQI PM2.5",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_24H,
        name="AQI PM2.5 24h avg",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_IN,
        name="AQI PM2.5 indoor",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_IN_24H,
        name="AQI PM2.5 indoor 24h avg",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_BAROMABSIN,
        name="Abs Pressure",
        native_unit_of_measurement=UnitOfPressure.INHG,  # UnitOfPressure.INHG,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_BAROMRELIN,
        name="Rel Pressure",
        native_unit_of_measurement=UnitOfPressure.INHG,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_CO2,
        name="co2",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_DAILYRAININ,
        name="Daily Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TYPE_DEWPOINT,
        name="Dew Point",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_EVENTRAININ,
        name="Event Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_FEELSLIKE,
        name="Feels Like",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HOURLYRAININ,
        name="Hourly Rain Rate",
        native_unit_of_measurement=UnitOfVolumetricFlux.INCHES_PER_HOUR,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.PRECIPITATION_INTENSITY,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY10,
        name="Humidity 10",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY1,
        name="Humidity 1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY2,
        name="Humidity 2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY3,
        name="Humidity 3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY4,
        name="Humidity 4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY5,
        name="Humidity 5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY6,
        name="Humidity 6",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY7,
        name="Humidity 7",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY8,
        name="Humidity 8",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY9,
        name="Humidity 9",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY,
        name="Humidity",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITYIN,
        name="Humidity In",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_LASTRAIN,
        name="Last Rain",
        icon="mdi:water",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key=TYPE_LIGHTNING_PER_DAY,
        name="Lightning Strikes Per Day",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement="strikes",
        state_class=SensorStateClass.TOTAL,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_LIGHTNING_PER_HOUR,
        name="Lightning Strikes Per Hour",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement="strikes",
        state_class=SensorStateClass.TOTAL,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_MAXDAILYGUST,
        name="Max Gust",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_MONTHLYRAININ,
        name="Monthly Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_24H,
        name="PM25 24h Avg",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_IN,
        name="PM25 Indoor",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_IN_24H,
        name="PM25 Indoor 24h Avg",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_PM25,
        name="PM25",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM10,
        name="Soil Humidity 10",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM1,
        name="Soil Humidity 1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM2,
        name="Soil Humidity 2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM3,
        name="Soil Humidity 3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM4,
        name="Soil Humidity 4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM5,
        name="Soil Humidity 5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM6,
        name="Soil Humidity 6",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM7,
        name="Soil Humidity 7",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM8,
        name="Soil Humidity 8",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM9,
        name="Soil Humidity 9",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP10F,
        name="Soil Temp 10",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP1F,
        name="Soil Temp 1",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP2F,
        name="Soil Temp 2",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP3F,
        name="Soil Temp 3",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP4F,
        name="Soil Temp 4",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP5F,
        name="Soil Temp 5",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP6F,
        name="Soil Temp 6",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP7F,
        name="Soil Temp 7",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP8F,
        name="Soil Temp 8",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP9F,
        name="Soil Temp 9",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_SOLARRADIATION,
        name="Solar Rad",
        native_unit_of_measurement=UnitOfIrradiance.WATTS_PER_SQUARE_METER,
        device_class=SensorDeviceClass.IRRADIANCE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOLARRADIATION_LX,
        name="Solar Rad Lx",
        native_unit_of_measurement=LIGHT_LUX,
        device_class=SensorDeviceClass.ILLUMINANCE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP10F,
        name="Temp 10",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP1F,
        name="Temp 1",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP2F,
        name="Temp 2",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP3F,
        name="Temp 3",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP4F,
        name="Temp 4",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP5F,
        name="Temp 5",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP6F,
        name="Temp 6",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP7F,
        name="Temp 7",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP8F,
        name="Temp 8",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP9F,
        name="Temp 9",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_TEMPF,
        name="Temp",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMPINF,
        name="Inside Temp",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TOTALRAININ,
        name="Lifetime Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_UV,
        name="UV Index",
        icon="mdi:sun-wireless",
        native_unit_of_measurement="Index",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WEEKLYRAININ,
        name="Weekly Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR,
        name="Wind Dir",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_AVG10M,
        name="Wind Dir Avg 10m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_AVG2M,
        name="Wind Dir Avg 2m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_WINDGUSTDIR,
        name="Gust Dir",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDGUSTMPH,
        name="Wind Gust",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPDMPH_AVG10M,
        name="Wind Avg 10m",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPDMPH_AVG2M,
        name="Wind Avg 2m",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPEEDMPH,
        name="Wind Speed",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_YEARLYRAININ,
        name="Yearly Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
)

BINARY_SENSOR_DESCRIPTIONS = (
    AmbientBinarySensorDescription(
        key=TYPE_BATTOUT,
        name="Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT1,
        name="Battery 1",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT2,
        name="Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT3,
        name="Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT4,
        name="Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT5,
        name="Battery 5",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT6,
        name="Battery 6",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT7,
        name="Battery 7",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT8,
        name="Battery 8",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT9,
        name="Battery 9",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTIN,
        name="Interior Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT10,
        name="Battery 10",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK1,
        name="Leak Detector Battery 1",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK2,
        name="Leak Detector Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK3,
        name="Leak Detector Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK4,
        name="Leak Detector Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM1,
        name="Soil Monitor Battery 1",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM2,
        name="Soil Monitor Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM3,
        name="Soil Monitor Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM4,
        name="Soil Monitor Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM5,
        name="Soil Monitor Battery 5",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM6,
        name="Soil Monitor Battery 6",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM7,
        name="Soil Monitor Battery 7",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM8,
        name="Soil Monitor Battery 8",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM9,
        name="Soil Monitor Battery 9",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM10,
        name="Soil Monitor Battery 10",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_CO2,
        name="CO2 Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LIGHTNING,
        name="Lightning Detector Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK1,
        name="Leak Detector 1",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK2,
        name="Leak Detector 2",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK3,
        name="Leak Detector 3",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK4,
        name="Leak Detector 4",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_PM25IN_BATT,
        name="PM25 Indoor Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_PM25_BATT,
        name="PM25 Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY1,
        name="Relay 1",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY2,
        name="Relay 2",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY3,
        name="Relay 3",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY4,
        name="Relay 4",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY5,
        name="Relay 5",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY6,
        name="Relay 6",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY7,
        name="Relay 7",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY8,
        name="Relay 8",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY9,
        name="Relay 9",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY10,
        name="Relay 10",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
        entity_registry_enabled_default=False,
    ),
)
