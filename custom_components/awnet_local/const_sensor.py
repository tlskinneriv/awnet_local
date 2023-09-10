"""Constants: Sensors

Contains definitions for all of the sensor types that the integration supports
"""

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)

from homeassistant.const import (
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_MILLION,
    DEGREE,
    LIGHT_LUX,
    PERCENTAGE,
    UnitOfLength,
    UnitOfIrradiance,
    UnitOfPrecipitationDepth,
    UnitOfPressure,
    UnitOfSpeed,
    UnitOfTemperature,
    UnitOfTime,
    UnitOfVolumetricFlux,
)

from homeassistant.helpers.entity import EntityCategory

# Sensor Types
TYPE_24HOURRAININ = "24hourrainin"
TYPE_AQI_PM10_IN_24H_AQIN = "aqi_pm10_in_24h_aqin"
TYPE_AQI_PM10_IN_AQIN = "aqi_pm10_in_aqin"
TYPE_AQI_PM25 = "aqi_pm25"
TYPE_AQI_PM25_24H = "aqi_pm25_24h"
TYPE_AQI_PM25_24H_AQIN = "aqi_pm25_24h_aqin"
TYPE_AQI_PM25_AQIN = "aqi_pm25_aqin"
TYPE_AQI_PM25_IN = "aqi_pm25_in"
TYPE_AQI_PM25_IN_24H = "aqi_pm25_in_24h"
TYPE_AQI_PM25_IN_24H_AQIN = "aqi_pm25_in_24h_aqin"
TYPE_AQI_PM25_IN_AQIN = "aqi_pm25_in_aqin"
TYPE_BAROMABSIN = "baromabsin"
TYPE_BAROMRELIN = "baromrelin"
TYPE_CO2 = "co2"
TYPE_CO2_IN = "co2_in"
TYPE_CO2_IN_24H = "co2_in_24h"
TYPE_CO2_IN_24H_AQIN = "co2_in_24h_aqin"
TYPE_CO2_IN_AQIN = "co2_in_aqin"
TYPE_DAILYRAININ = "dailyrainin"
TYPE_DATEUTC = "dateutc"
TYPE_DEWPOINT = "dewPoint"
TYPE_DEWPOINT_IN = "dewPointin"
TYPE_ETOS = "etos"
TYPE_ETRS = "etrs"
TYPE_EVENTRAININ = "eventrainin"
TYPE_FEELSLIKE = "feelsLike"
TYPE_FEELSLIKE_IN = "feelsLikein"
TYPE_GDD = "gdd"
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
TYPE_LEAFWETNESS1 = "leafwetness1"
TYPE_LEAFWETNESS2 = "leafwetness2"
TYPE_LEAFWETNESS3 = "leafwetness3"
TYPE_LEAFWETNESS4 = "leafwetness4"
TYPE_LEAFWETNESS5 = "leafwetness5"
TYPE_LEAFWETNESS6 = "leafwetness6"
TYPE_LEAFWETNESS7 = "leafwetness7"
TYPE_LEAFWETNESS8 = "leafwetness8"
TYPE_LIGHTNING_DISTANCE = "lightning_distance"
TYPE_LIGHTNING_PER_DAY = "lightning_day"
TYPE_LIGHTNING_PER_HOUR = "lightning_hour"
TYPE_LIGHTNING_TIME = "lightning_time"
TYPE_MAXDAILYGUST = "maxdailygust"
TYPE_MONTHLYRAININ = "monthlyrainin"
TYPE_PM_IN_HUMIDITY = "pm_in_humidity"
TYPE_PM_IN_HUMIDITY_AQIN = "pm_in_humidity_aqin"
TYPE_PM_IN_TEMP = "pm_in_temp"
TYPE_PM_IN_TEMP_AQIN = "pm_in_temp_aqin"
TYPE_PM10_IN = "pm10_in"
TYPE_PM10_IN_24H = "pm10_in_24h"
TYPE_PM10_IN_24H_AQIN = "pm10_in_24h_aqin"
TYPE_PM10_IN_AQIN = "pm10_in_aqin"
TYPE_PM25 = "pm25"
TYPE_PM25_24H = "pm25_24h"
TYPE_PM25_IN = "pm25_in"
TYPE_PM25_IN_24H = "pm25_in_24h"
TYPE_PM25_IN_24H_AQIN = "pm25_in_24h_aqin"
TYPE_PM25_IN_AQIN = "pm25_in_aqin"
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
TYPE_SOILTENS1 = "soiltens1"
TYPE_SOILTENS2 = "soiltens2"
TYPE_SOILTENS3 = "soiltens3"
TYPE_SOILTENS4 = "soiltens4"
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
TYPE_WINDDIR_CARD = "winddir_card"
TYPE_WINDDIR_AVG10M = "winddir_Avg10m"
TYPE_WINDDIR_AVG2M = "winddir_Avg2m"
TYPE_WINDGUSTDIR = "windgustdir"
TYPE_WINDGUSTDIR_CARD = "windgustdir_card"
TYPE_WINDGUSTMPH = "windgustmph"
TYPE_WINDSPDMPH_AVG10M = "windspdmph_Avg10m"
TYPE_WINDSPDMPH_AVG2M = "windspdmph_Avg2m"
TYPE_WINDSPEEDMPH = "windspeedmph"
TYPE_YEARLYRAININ = "yearlyrainin"

SUPPORTED_SENSOR_TYPES = [
    TYPE_24HOURRAININ,
    TYPE_AQI_PM10_IN_24H_AQIN,
    TYPE_AQI_PM10_IN_AQIN,
    TYPE_AQI_PM25_24H_AQIN,
    TYPE_AQI_PM25_24H,
    TYPE_AQI_PM25_AQIN,
    TYPE_AQI_PM25_IN_24H_AQIN,
    TYPE_AQI_PM25_IN_24H,
    TYPE_AQI_PM25_IN_AQIN,
    TYPE_AQI_PM25_IN,
    TYPE_AQI_PM25,
    TYPE_BAROMABSIN,
    TYPE_BAROMRELIN,
    TYPE_CO2_IN_24H_AQIN,
    TYPE_CO2_IN_24H,
    TYPE_CO2_IN_AQIN,
    TYPE_CO2_IN,
    TYPE_CO2,
    TYPE_DAILYRAININ,
    TYPE_DATEUTC,
    TYPE_DEWPOINT_IN,
    TYPE_DEWPOINT,
    TYPE_ETOS,
    TYPE_ETRS,
    TYPE_EVENTRAININ,
    TYPE_FEELSLIKE_IN,
    TYPE_FEELSLIKE,
    TYPE_GDD,
    TYPE_HOURLYRAININ,
    TYPE_HUMIDITY,
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
    TYPE_HUMIDITYIN,
    TYPE_LASTRAIN,
    TYPE_LEAFWETNESS1,
    TYPE_LEAFWETNESS2,
    TYPE_LEAFWETNESS3,
    TYPE_LEAFWETNESS4,
    TYPE_LEAFWETNESS5,
    TYPE_LEAFWETNESS6,
    TYPE_LEAFWETNESS7,
    TYPE_LEAFWETNESS8,
    TYPE_LIGHTNING_DISTANCE,
    TYPE_LIGHTNING_PER_DAY,
    TYPE_LIGHTNING_PER_HOUR,
    TYPE_LIGHTNING_TIME,
    TYPE_MAXDAILYGUST,
    TYPE_MONTHLYRAININ,
    TYPE_PM_IN_HUMIDITY_AQIN,
    TYPE_PM_IN_HUMIDITY,
    TYPE_PM_IN_TEMP_AQIN,
    TYPE_PM_IN_TEMP,
    TYPE_PM10_IN_24H_AQIN,
    TYPE_PM10_IN_24H,
    TYPE_PM10_IN_AQIN,
    TYPE_PM10_IN,
    TYPE_PM25_24H,
    TYPE_PM25_IN_24H_AQIN,
    TYPE_PM25_IN_24H,
    TYPE_PM25_IN_AQIN,
    TYPE_PM25_IN,
    TYPE_PM25,
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
    TYPE_SOILTENS1,
    TYPE_SOILTENS2,
    TYPE_SOILTENS3,
    TYPE_SOILTENS4,
    TYPE_SOLARRADIATION_LX,
    TYPE_SOLARRADIATION,
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
    TYPE_TEMPF,
    TYPE_TEMPINF,
    TYPE_TOTALRAININ,
    TYPE_UV,
    TYPE_WEEKLYRAININ,
    TYPE_WINDDIR_AVG10M,
    TYPE_WINDDIR_AVG2M,
    TYPE_WINDDIR,
    TYPE_WINDDIR_CARD,
    TYPE_WINDGUSTDIR,
    TYPE_WINDGUSTDIR_CARD,
    TYPE_WINDGUSTMPH,
    TYPE_WINDSPDMPH_AVG10M,
    TYPE_WINDSPDMPH_AVG2M,
    TYPE_WINDSPEEDMPH,
    TYPE_YEARLYRAININ,
]

# Each sensor listed here is calculated server-side and depends on the list of
# sensors it is a key for
CALCULATED_SENSOR_TYPES = {
    TYPE_LASTRAIN: [TYPE_DATEUTC, TYPE_HOURLYRAININ],
    TYPE_FEELSLIKE: [TYPE_TEMPF, TYPE_WINDSPEEDMPH, TYPE_HUMIDITY],
    TYPE_DEWPOINT: [TYPE_TEMPF, TYPE_HUMIDITY],
    TYPE_SOLARRADIATION_LX: [TYPE_SOLARRADIATION],
    TYPE_FEELSLIKE_IN: [TYPE_TEMPINF, TYPE_HUMIDITYIN],
    TYPE_DEWPOINT_IN: [TYPE_TEMPINF, TYPE_HUMIDITYIN],
    TYPE_LIGHTNING_PER_HOUR: [TYPE_LIGHTNING_PER_DAY, TYPE_DATEUTC],
    TYPE_WINDDIR_CARD: [TYPE_WINDDIR],
    TYPE_WINDGUSTDIR_CARD: [TYPE_WINDGUSTDIR],
}

# Each sensor listed here is converted server-side from the native unit to the unit that HA supports
CONVERTED_SENSOR_TYPES = [TYPE_LIGHTNING_TIME, TYPE_DATEUTC]

# Each sensor listed here should be restored on a restart of HA since it is a timestamp type sensor
RESTORE_SENSOR_TYPES = [TYPE_LIGHTNING_TIME, TYPE_LASTRAIN]

SENSOR_DESCRIPTIONS = (
    SensorEntityDescription(
        key=TYPE_24HOURRAININ,
        name="24 Hr Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM10_IN_AQIN,
        name="AQI PM10 Indoor (AQIN Sensor)",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM10_IN_24H_AQIN,
        name="AQI PM10 Indoor 24h Avg (AQIN Sensor)",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_AQIN,
        name="AQI PM2.5 (AQIN)",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25,
        name="AQI PM2.5",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_24H_AQIN,
        name="AQI PM2.5 24h Avg (AQIN)",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_24H,
        name="AQI PM2.5 24h Avg",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_IN,
        name="AQI PM2.5 Indoor",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_IN_24H,
        name="AQI PM2.5 Indoor 24h Avg",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_IN_AQIN,
        name="AQI PM2.5 Indoor (AQIN Sensor)",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_AQI_PM25_IN_24H_AQIN,
        name="AQI PM2.5 Indoor 24h Avg (AQIN Sensor)",
        device_class=SensorDeviceClass.AQI,
        state_class=SensorStateClass.MEASUREMENT,
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
        name="CO2",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_CO2_IN_AQIN,
        name="CO2 Indoor (AQIN)",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_CO2_IN,
        name="CO2 Indoor",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_CO2_IN_24H_AQIN,
        name="CO2 Indoor 24h Avg (AQIN)",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_CO2_IN_24H,
        name="CO2 Indoor 24h Avg",
        native_unit_of_measurement=CONCENTRATION_PARTS_PER_MILLION,
        device_class=SensorDeviceClass.CO2,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_DAILYRAININ,
        name="Daily Rain",
        native_unit_of_measurement=UnitOfPrecipitationDepth.INCHES,
        device_class=SensorDeviceClass.PRECIPITATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key=TYPE_DATEUTC,
        name="Last Data Date",
        device_class=SensorDeviceClass.TIMESTAMP,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key=TYPE_DEWPOINT,
        name="Dew Point",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_DEWPOINT_IN,
        name="Dew Point Indoor",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_ETOS,
        name="Evapotranspiration Short",
        icon="mdi:waves-arrow-up",
        native_unit_of_measurement=UnitOfVolumetricFlux.INCHES_PER_DAY,
        device_class=SensorDeviceClass.PRECIPITATION_INTENSITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_ETRS,
        name="Evapotranspiration Tall",
        icon="mdi:waves-arrow-up",
        native_unit_of_measurement=UnitOfVolumetricFlux.INCHES_PER_DAY,
        device_class=SensorDeviceClass.PRECIPITATION_INTENSITY,
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
        key=TYPE_FEELSLIKE_IN,
        name="Feels Like Indoor",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_GDD,
        name="Growing Degree Days",
        icon="mdi:sprout",
        native_unit_of_measurement=UnitOfTime.DAYS,
        device_class=SensorDeviceClass.DURATION,
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
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY1,
        name="Humidity 1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY2,
        name="Humidity 2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY3,
        name="Humidity 3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY4,
        name="Humidity 4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY5,
        name="Humidity 5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY6,
        name="Humidity 6",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY7,
        name="Humidity 7",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY8,
        name="Humidity 8",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_HUMIDITY9,
        name="Humidity 9",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
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
    ),
    SensorEntityDescription(
        key=TYPE_LASTRAIN,
        name="Last Rain",
        icon="mdi:water",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS1,
        name="Leaf Wetness 1",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS2,
        name="Leaf Wetness 2",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS3,
        name="Leaf Wetness 3",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS4,
        name="Leaf Wetness 4",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS5,
        name="Leaf Wetness 5",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS6,
        name="Leaf Wetness 6",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS7,
        name="Leaf Wetness 7",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LEAFWETNESS8,
        name="Leaf Wetness 8",
        icon="mdi:leaf",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.MOISTURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LIGHTNING_DISTANCE,
        name="Lightning Strike Distance",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfLength.KILOMETERS,
        device_class=SensorDeviceClass.DISTANCE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_LIGHTNING_PER_DAY,
        name="Daily Lightning Strikes",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement="strikes",
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key=TYPE_LIGHTNING_PER_HOUR,
        name="Lightning Strikes Last Hour",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement="strikes",
        state_class=SensorStateClass.TOTAL,
    ),
    SensorEntityDescription(
        key=TYPE_LIGHTNING_TIME,
        name="Last Lightning Strike",
        icon="mdi:lightning-bolt",
        device_class=SensorDeviceClass.TIMESTAMP,
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
        key=TYPE_PM_IN_HUMIDITY_AQIN,
        name="PM Indoor Humidity (AQIN)",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM_IN_HUMIDITY,
        name="PM Indoor Humidity",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM_IN_TEMP_AQIN,
        name="PM Indoor Temp (AQIN)",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM_IN_TEMP,
        name="PM Indoor Temp",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM10_IN,
        name="PM10 Indoor",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM10,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM10_IN_24H,
        name="PM10 Indoor 24h Avg",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM10,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM10_IN_AQIN,
        name="PM10 Indoor (AQIN Sensor)",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM10,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM10_IN_24H_AQIN,
        name="PM10 Indoor 24h Avg (AQIN Sensor)",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM10,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_24H,
        name="PM25 24h Avg",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
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
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_IN_AQIN,
        name="PM25 Indoor (AQIN Sensor)",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_PM25_IN_24H_AQIN,
        name="PM25 Indoor 24h Avg (AQIN Sensor)",
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        device_class=SensorDeviceClass.PM25,
        state_class=SensorStateClass.MEASUREMENT,
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
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM1,
        name="Soil Humidity 1",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM2,
        name="Soil Humidity 2",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM3,
        name="Soil Humidity 3",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM4,
        name="Soil Humidity 4",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM5,
        name="Soil Humidity 5",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM6,
        name="Soil Humidity 6",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM7,
        name="Soil Humidity 7",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM8,
        name="Soil Humidity 8",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILHUM9,
        name="Soil Humidity 9",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP10F,
        name="Soil Temp 10",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP1F,
        name="Soil Temp 1",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP2F,
        name="Soil Temp 2",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP3F,
        name="Soil Temp 3",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP4F,
        name="Soil Temp 4",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP5F,
        name="Soil Temp 5",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP6F,
        name="Soil Temp 6",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP7F,
        name="Soil Temp 7",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP8F,
        name="Soil Temp 8",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTEMP9F,
        name="Soil Temp 9",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTENS1,
        name="Soil Tension 1",
        native_unit_of_measurement=UnitOfPressure.CBAR,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTENS2,
        name="Soil Tension 2",
        native_unit_of_measurement=UnitOfPressure.CBAR,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTENS3,
        name="Soil Tension 3",
        native_unit_of_measurement=UnitOfPressure.CBAR,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_SOILTENS4,
        name="Soil Tension 4",
        native_unit_of_measurement=UnitOfPressure.CBAR,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
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
    ),
    SensorEntityDescription(
        key=TYPE_TEMP1F,
        name="Temp 1",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP2F,
        name="Temp 2",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP3F,
        name="Temp 3",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP4F,
        name="Temp 4",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP5F,
        name="Temp 5",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP6F,
        name="Temp 6",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP7F,
        name="Temp 7",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP8F,
        name="Temp 8",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_TEMP9F,
        name="Temp 9",
        native_unit_of_measurement=UnitOfTemperature.FAHRENHEIT,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
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
        name="Wind Direction",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_CARD,
        name="Wind Direction Cardinal",
        icon="mdi:weather-windy",
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_AVG10M,
        name="Wind Dir Avg 10m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDDIR_AVG2M,
        name="Wind Dir Avg 2m",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDGUSTDIR,
        name="Gust Direction",
        icon="mdi:weather-windy",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=TYPE_WINDGUSTDIR_CARD,
        name="Gust Direction Cardinal",
        icon="mdi:weather-windy",
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
    ),
    SensorEntityDescription(
        key=TYPE_WINDSPDMPH_AVG2M,
        name="Wind Avg 2m",
        native_unit_of_measurement=UnitOfSpeed.MILES_PER_HOUR,
        device_class=SensorDeviceClass.WIND_SPEED,
        state_class=SensorStateClass.MEASUREMENT,
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
