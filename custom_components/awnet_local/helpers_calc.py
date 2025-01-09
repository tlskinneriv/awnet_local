"""Helper Calculations

These classes provide the calculation methods for the calculated sensors in this integration. All of
the calculated sensors call the "calculate" method, which then determines which calculation to
perform based on the sensor type.
"""

from datetime import datetime, timezone, timedelta
import logging, math

from .const import ATTR_LAST_DATA, ATTR_LIGHTNING_DATA

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
    TYPE_LIGHTNING_PER_HOUR,
    TYPE_LIGHTNING_PER_DAY,
    TYPE_DATEUTC,
    TYPE_WINDDIR,
    TYPE_WINDDIR_CARD,
    TYPE_WINDGUSTDIR,
    TYPE_WINDGUSTDIR_CARD,
)

_LOGGER = logging.getLogger(__name__)


class AmbientSensorCalculations:
    """Class full of static methods for calculating sensor values with data provided from the
    Ambient Weather stations
    """

    @staticmethod
    def calculate(entity_key: str, station_data: dict[str, object]) -> object:
        """Calls the correct calculation function and returns the data for it

        Args:
            entity_key (str): key for the entity to find in the station data
            station_values (dict): station data to lookup values in

        Returns:
            any: calculated value for the field
        """
        station_values = station_data[ATTR_LAST_DATA]

        if entity_key == TYPE_SOLARRADIATION_LX:
            return AmbientSensorCalculations.solar_rad_wm2_to_lux(
                float(station_values[TYPE_SOLARRADIATION])
            )
        if entity_key == TYPE_LASTRAIN:
            return AmbientSensorCalculations.last_rain(
                str(station_values.get(TYPE_DATEUTC)),
                float(station_values.get(TYPE_HOURLYRAININ)),
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
        if entity_key == TYPE_LIGHTNING_PER_HOUR:
            return AmbientSensorCalculations.lightning_hour(
                str(station_values.get(TYPE_DATEUTC)),
                int(station_values.get(TYPE_LIGHTNING_PER_DAY)),
                station_data[ATTR_LIGHTNING_DATA],
            )
        if entity_key == TYPE_WINDDIR_CARD:
            return AmbientSensorCalculations.degree_to_cardinal(
                float(station_values.get(TYPE_WINDDIR))
            )
        if entity_key == TYPE_WINDGUSTDIR_CARD:
            return AmbientSensorCalculations.degree_to_cardinal(
                float(station_values.get(TYPE_WINDGUSTDIR))
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
    def last_rain(lightning_time: str, hourly_rain_in: float) -> any:
        """Calculates the last rain timestamp from the last time that houlry rain had a value
        greater than 0 per https://github.com/ambient-weather/api-docs/wiki/Device-Data-Specs

        Args:
            last_rain_timestamp (str): string timestamp provided by the station
            hourly_rain_in (float): last hourly rain value provided by the weather station

        Returns:
            any: timestamp if there is data to report; None if it's not raining
        """
        if hourly_rain_in > 0:
            return AmbientSensorConversions.mysql_timestamp_to_datetime(lightning_time)
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
    def lightning_hour(
        lightning_time: str,
        lightning_current_count: int,
        lightning_data: dict[str, int],
    ) -> int:
        """Calculates lighting strikes in the last hour based on lightning_data collected in the
        last hour

        Args:
            lightning_time (str): timestamp of the data coming in
            lightning_current_count (int): number of lightning strikes
            lightning_data (dict[float, int]): dictionary of timestamps with strike counts

        Returns:
            int: number of lightning strikes that have happened in the last hour
        """
        lightning_datetime = AmbientSensorConversions.mysql_timestamp_to_datetime(
            lightning_time
        )
        lightning_data[str(lightning_datetime.timestamp())] = lightning_current_count

        # find the time closest to an hour ago to get the count of lightning strikes from
        lightning_data_times = list(lightning_data.keys())
        search_datetime = lightning_datetime - timedelta(hours=1)
        lightning_data_closest_times = {
            abs(
                search_datetime.timestamp() - float(test_datetime)
            ): datetime.fromtimestamp(float(test_datetime))
            for test_datetime in lightning_data_times
        }
        lightning_data_closest_time = lightning_data_closest_times[
            min(lightning_data_closest_times.keys())
        ]
        _LOGGER.debug(
            "Closest time to %s determined to be %s",
            search_datetime,
            lightning_data_closest_time,
        )

        # calculate the value of the number of strikes that happened in the last hour
        lightning_previous_count = lightning_data[
            str(lightning_data_closest_time.timestamp())
        ]
        if lightning_previous_count > lightning_current_count:
            _LOGGER.debug(
                "Previous lightning value is greater than current value, \
                we must have rolled in the last hour."
            )
            lightning_current_count = lightning_current_count + max(
                lightning_data.values()
            )
        lightning_past_hour = lightning_current_count - lightning_previous_count

        # cleanup the old entries in the lightning_data dict
        for date in [
            timestamp
            for timestamp in lightning_data.keys()
            if float(timestamp) < search_datetime.timestamp()
        ]:
            _LOGGER.debug("Removing old entry for %s", date)
            del lightning_data[date]

        return lightning_past_hour

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
        """Calculates the dew point from the temperature in Fahrenheit and relative humidity using
        the Arden Buck equation mentioned here:
        https://ambientweather.com/faqs/question/view/id/1869/

        Args:
            tempf (float): temperature in Fahrenheit
            rel_humid_percent (float): relative humidity percentage

        Returns:
            float: dew point in Fahrenheit
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

    @staticmethod
    def degree_to_cardinal(direction_degree: float) -> str:
        """Converts a direction in degrees to its cardinal equivalent

        Args:
            direction_degree (float): Direction in degrees

        Returns:
            str: Cardinal direction
        """
        direction = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW",
            "N",
        ]
        return direction[int((direction_degree + 11.25) / 22.5)]


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
        if entity_key == TYPE_DATEUTC:
            return AmbientSensorConversions.mysql_timestamp_to_datetime(str(value))
        raise NotImplementedError(f"Conversion for {entity_key} is not implemented")

    @staticmethod
    def epoch_to_datetime(epoch: int) -> datetime:
        """Converts epoch time to a datetime object in UTC

        Args:
            epoch (int): epoch time

        Returns:
            datetime: datetime object representing the epoch time in UTC
        """
        return datetime.fromtimestamp(epoch, timezone.utc)

    @staticmethod
    def mysql_timestamp_to_datetime(mysql_timestamp: str) -> datetime:
        """Converts a MySQL timestamp string into a datetime object in UTC

        Args:
            mysql_timestamp (str): MySQL timestamp string

        Returns:
            datetime: datetime object representing the MySQL timestamp string in UTC
        """
        try:
            return datetime.strptime(mysql_timestamp, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=timezone.utc
            )
        except ValueError as error:
            _LOGGER.error(
                'Failed to convert timestamp "%s" to datetime: %s',
                mysql_timestamp,
                error,
            )
            return datetime.fromtimestamp(0, timezone.utc)
