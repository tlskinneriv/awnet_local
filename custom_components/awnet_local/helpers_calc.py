"""Helper Calculations

These classes provide the calculation methods for the calculated sensors in this integration. All of
the calculated sensors call the "calculate" method, which then determines which calculation to
perform based on the sensor type.
"""

from datetime import datetime, timezone
import math

from .const_sensor import (
    TYPE_FEELSLIKE,
    TYPE_HOURLYRAININ,
    TYPE_LASTRAIN,
    TYPE_SOLARRADIATION,
    TYPE_SOLARRADIATION_LX,
    TYPE_TEMPF,
    TYPE_WINDSPEEDMPH,
    TYPE_HUMIDITY,
    TYPE_DEWPOINT,
    TYPE_LIGHTNING_TIME,
    TYPE_FEELSLIKE_IN,
    TYPE_DEWPOINT_IN,
    TYPE_TEMPINF,
    TYPE_HUMIDITYIN,
)


class AmbientSensorCalculations:
    """Class full of static methods for calculating sensor values with data provided from the
    Ambient Weather stations
    """

    @staticmethod
    def calculate(entity_key: str, station_values: dict) -> object:
        """Calls the correct calculation function and returns the data for it

        Args:
            entity_key (str): key for the entity to find in the station data
            station_values (dict): station data to lookup values in

        Returns:
            any: calculated value for the field
        """
        if entity_key == TYPE_SOLARRADIATION_LX:
            return AmbientSensorCalculations.solar_rad_wm2_to_lux(
                float(station_values[TYPE_SOLARRADIATION])
            )
        if entity_key == TYPE_LASTRAIN:
            return AmbientSensorCalculations.last_rain(
                float(station_values.get(TYPE_HOURLYRAININ))
            )
        if entity_key == TYPE_FEELSLIKE:
            return AmbientSensorCalculations.feels_like(
                float(station_values.get(TYPE_TEMPF)),
                float(station_values.get(TYPE_WINDSPEEDMPH)),
                float(station_values.get(TYPE_HUMIDITY)),
            )
        if entity_key == TYPE_DEWPOINT:
            return AmbientSensorCalculations.dew_point(
                float(station_values.get(TYPE_TEMPF)),
                float(station_values.get(TYPE_HUMIDITY)),
            )
        if entity_key == TYPE_FEELSLIKE_IN:
            return AmbientSensorCalculations.heat_index(
                float(station_values.get(TYPE_TEMPINF)),
                float(station_values.get(TYPE_HUMIDITYIN)),
            )
        if entity_key == TYPE_DEWPOINT_IN:
            return AmbientSensorCalculations.dew_point(
                float(station_values.get(TYPE_TEMPINF)),
                float(station_values.get(TYPE_HUMIDITYIN)),
            )
        raise NotImplementedError(f"Calculation for {entity_key} is not implemented")

    @staticmethod
    def solar_rad_wm2_to_lux(solar_rad_wm2: float) -> float:
        """Converts solar radiation measured in W/M^2 to lux; reference for this value from
        https://ambientweather.com/faqs/question/view/id/1452/

        Args:
            solar_rad_wm2 (float): Value of solar radiation in W/M^2

        Returns:
            float: Value of solar radiation in lux
        """
        return float(round(solar_rad_wm2 * 126.7, 0))

    @staticmethod
    def last_rain(hourly_rain_in: float) -> any:
        """Calculates the last rain timestamp from the last time that houlry rain had a value
        greater than 0 per https://github.com/ambient-weather/api-docs/wiki/Device-Data-Specs

        Args:
            last_rain_timestamp (str): string timestamp provided by the station
            hourly_rain_in (float): last hourly rain value provided by the weather station

        Returns:
            any: timestamp if there is data to report; None if it's not raining
        """
        if hourly_rain_in > 0:
            return datetime.now(timezone.utc)
        return None

    @staticmethod
    def feels_like(tempf: float, wind_mph: float, rel_humid_percent: float) -> float:
        """Calculates the feels-like temperature based on temperature, wind speed, and relative
        humidity.
        Formulas used come from weather.gov calculators

        Args:
            tempf (float): temperature in Fahrenheit
            wind_mph (float): wind speed in MPH
            rel_humid_percent (float): relative humidity in percentage (0-100)

        Returns:
            float: feel like temperature in Fahrenheit
        """
        if tempf > 68:
            return AmbientSensorCalculations.heat_index(tempf, rel_humid_percent)
        return AmbientSensorCalculations.wind_chill(tempf, wind_mph)

    @staticmethod
    def wind_chill(tempf: float, wind_mph: float) -> float:
        """Calculates the wind chill. Below 50 F and 3+ mph wind calls for wind chill calc,
        otherwise return the temperature passed.

        Args:
            tempf (float): temperature in Fahrenheit
            wind_mph (float): wind speed in MPH

        Returns:
            float: wind chill in Fahrenheit
        """
        if tempf < 50 and wind_mph >= 3:
            # calculate the wind chill
            return float(
                round(
                    (
                        35.74
                        + (0.6215 * tempf)
                        - (35.75 * math.pow(wind_mph, 0.16))
                        + (0.4275 * tempf * math.pow(wind_mph, 0.16))
                    ),
                    1,
                )
            )
        # outside the range, return the temp
        return tempf

    @staticmethod
    def heat_index(tempf: float, rel_humid_percent: float) -> float:
        """Calculates the heat index. Above 68 F calls for heat index calc, otherwise return the
        temperature passed.

        Args:
            tempf (float): temperature in Fahrenheit
            rel_humid_percent (float): relative humidity in percentage

        Returns:
            float: heat index in Fahrenheit
        """
        if tempf > 68:
            # calculate the heat index
            rel_humid_dec = rel_humid_percent
            return float(
                round(
                    (
                        -42.379
                        + (2.04901523 * tempf)
                        + (10.14333127 * rel_humid_dec)
                        - (0.22475541 * tempf * rel_humid_dec)
                        - (0.00683783 * math.pow(tempf, 2))
                        - (0.05481717 * math.pow(rel_humid_dec, 2))
                        + (0.00122874 * math.pow(tempf, 2) * rel_humid_dec)
                        + (0.00085282 * tempf * math.pow(rel_humid_dec, 2))
                        - (0.00000199 * math.pow(tempf, 2) * math.pow(rel_humid_dec, 2))
                    ),
                    1,
                )
            )
        # outside the range, return the temp
        return tempf

    @staticmethod
    def dew_point(tempf: float, rel_humid_percent: float) -> float:
        """Calculates the dew point from the temperature in Farenheit and relative humidity using
        the Arden Buck equation mentioned here:
        https://ambientweather.com/faqs/question/view/id/1869/

        Args:
            tempf (float): temperature in Farenheit
            rel_humid_percent (float): relative humidity percentage

        Returns:
            float: dew point in Farenheit
        """
        tempc = (tempf - 32) * 5 / 9
        const_b = 18.678
        const_c = 257.14
        const_d = 234.5
        gamma_t_rh = math.log(
            (rel_humid_percent / 100)
            * math.pow(
                math.e, (const_b - (tempc / const_d)) * (tempc / (const_c + tempc))
            )
        )
        dew_pt_c = (const_c * gamma_t_rh) / (const_b - gamma_t_rh)
        return float(round(dew_pt_c * 9 / 5 + 32, 1))


class AmbientSensorConversions:
    """Class full of static methods for performing conversions from native units to HA units where
    the raw unit is not supported by HA
    """

    @staticmethod
    def convert(entity_key: str, value: object) -> object:
        """Calls the correct calculation function and returns the data for it

        Args:
            entity_key (str): key for the entity to find in the station data
            value (object): data value to convert

        Returns:
            any: converted value for the field
        """
        if entity_key == TYPE_LIGHTNING_TIME:
            return AmbientSensorConversions.epoch_to_datetime(int(value))
        raise NotImplementedError(f"Conversion for {entity_key} is not implemented")

    @staticmethod
    def epoch_to_datetime(epoch: int) -> str:
        return datetime.fromtimestamp(epoch, timezone.utc)
