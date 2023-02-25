"""Helper Classes

These classes provide helpers for determining valid states and descriptions as code
"""

from typing import Literal
from dataclasses import dataclass

from homeassistant.components.binary_sensor import BinarySensorEntityDescription


@dataclass
class AmbientBinarySensorDescriptionMixin:
    """Define an entity description mixin for binary sensors."""

    on_state: Literal[0, 1]


@dataclass
class AmbientBinarySensorDescription(
    BinarySensorEntityDescription, AmbientBinarySensorDescriptionMixin
):
    """Describe an Ambient PWS binary sensor."""
