"""Constants

Covers constant values used in the integration that have not already been defined elsewhere and are
not definitions of sensors. Usually strings we don't want to accidentally mistype.
"""

# domain
DOMAIN = "awnet_local"

# configuration parameters
CONF_MAC = "station_mac"
CONF_NAME = "station_name"

# Attributes
ATTR_PASSKEY = "PASSKEY"
ATTR_MAC = "MAC"
ATTR_LAST_DATA = "last_data"
ATTR_KNOWN_SENSORS = "known_sensors"
ATTR_SENSOR_UPDATE_IN_PROGRESS = "sensor_update_in_progress"
ATTR_STATIONTYPE = "stationtype"
ATTR_LIGHTNING_DATA = "lightning_data"

# Regular Expressions
MAC_REGEX = r"^(?:[A-Fa-f0-9]{2}[-:]?){5}[A-Fa-f0-9]{2}$|^(?:[A-Fa-f0-9]{4}\.){2}[A-Fa-f0-9]{4}$"

# Configuration error keys
CONF_MAC_REGEX_ERROR = "station_mac_regex_error"
