"""Constants: Binary Sensors

Contains definitions for all of the binary sensor types that the integration supports
"""

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.helpers.entity import EntityCategory
from .helpers import AmbientBinarySensorDescription

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
TYPE_BATTR1 = "battr1"
TYPE_BATTR10 = "battr10"
TYPE_BATTR2 = "battr2"
TYPE_BATTR3 = "battr3"
TYPE_BATTR4 = "battr4"
TYPE_BATTR5 = "battr5"
TYPE_BATTR6 = "battr6"
TYPE_BATTR7 = "battr7"
TYPE_BATTR8 = "battr8"
TYPE_BATTR9 = "battr9"
TYPE_BATTRAIN = "battrain"

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
    TYPE_BATTR1,
    TYPE_BATTR10,
    TYPE_BATTR2,
    TYPE_BATTR3,
    TYPE_BATTR4,
    TYPE_BATTR5,
    TYPE_BATTR6,
    TYPE_BATTR7,
    TYPE_BATTR8,
    TYPE_BATTR9,
    TYPE_BATTRAIN,
]

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
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT2,
        name="Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT3,
        name="Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT4,
        name="Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT5,
        name="Battery 5",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT6,
        name="Battery 6",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT7,
        name="Battery 7",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT8,
        name="Battery 8",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT9,
        name="Battery 9",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
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
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK1,
        name="Leak Detector Battery 1",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK2,
        name="Leak Detector Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK3,
        name="Leak Detector Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LEAK4,
        name="Leak Detector Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM1,
        name="Soil Monitor Battery 1",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM2,
        name="Soil Monitor Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM3,
        name="Soil Monitor Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM4,
        name="Soil Monitor Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM5,
        name="Soil Monitor Battery 5",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM6,
        name="Soil Monitor Battery 6",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM7,
        name="Soil Monitor Battery 7",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM8,
        name="Soil Monitor Battery 8",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM9,
        name="Soil Monitor Battery 9",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_SM10,
        name="Soil Monitor Battery 10",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_CO2,
        name="CO2 Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATT_LIGHTNING,
        name="Lightning Detector Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK1,
        name="Leak Detector 1",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK2,
        name="Leak Detector 2",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK3,
        name="Leak Detector 3",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_LEAK4,
        name="Leak Detector 4",
        device_class=BinarySensorDeviceClass.MOISTURE,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_PM25IN_BATT,
        name="PM25 Indoor Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_PM25_BATT,
        name="PM25 Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY1,
        name="Relay 1",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY2,
        name="Relay 2",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY3,
        name="Relay 3",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY4,
        name="Relay 4",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY5,
        name="Relay 5",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY6,
        name="Relay 6",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY7,
        name="Relay 7",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY8,
        name="Relay 8",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY9,
        name="Relay 9",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_RELAY10,
        name="Relay 10",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=1,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTRAIN,
        name="Rain Guage Battery",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR1,
        name="Relay Battery 1",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR2,
        name="Relay Battery 2",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR3,
        name="Relay Battery 3",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR4,
        name="Relay Battery 4",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR5,
        name="Relay Battery 5",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR6,
        name="Relay Battery 6",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR7,
        name="Relay Battery 7",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR8,
        name="Relay Battery 8",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR9,
        name="Relay Battery 9",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
    AmbientBinarySensorDescription(
        key=TYPE_BATTR10,
        name="Relay Battery 10",
        device_class=BinarySensorDeviceClass.BATTERY,
        entity_category=EntityCategory.DIAGNOSTIC,
        on_state=0,
    ),
)
