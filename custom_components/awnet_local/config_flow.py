"""Configuration Flow

Handle the UI-based configuration of the integration.

The integration requires the following:
- Name: a friendly name for the device
- MAC: the MAC address of the device (take multiple formats supported by the format_mac method)
"""

from typing import Dict, Any
import logging
import re
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.device_registry import format_mac

from .const import (
    DOMAIN,
    CONF_MAC,
    CONF_NAME,
    CONF_MAC_REGEX_ERROR,
    MAC_REGEX,
)

_LOGGER = logging.getLogger(__name__)


class AWNConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """AWNET Config Flow"""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the AWNet Local config flow"""
        self.config: dict[str, Any] = {}
        self.retry_schema: dict[vol.Marker, Any] = {}

    async def async_step_user(self, user_input=None):
        """Handle user step."""

        errors: Dict[str, str] = {}

        if user_input is not None:
            _LOGGER.info(user_input)

            self.config = {
                CONF_NAME: user_input[CONF_NAME],
                CONF_MAC: user_input[CONF_MAC],
            }

            # validation checkS
            if not re.search(MAC_REGEX, user_input[CONF_MAC]):
                errors[CONF_MAC] = CONF_MAC_REGEX_ERROR

            # format the mac address
            self.config[CONF_MAC] = format_mac(self.config[CONF_MAC])

            # create the entry if no errors
            if len(errors) == 0:
                await self.async_set_unique_id(self.config[CONF_MAC])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=f"{self.config[CONF_NAME]} - {self.config[CONF_MAC]}",
                    data=self.config,
                )

        data = {
            vol.Required(CONF_NAME, default=self.config.get(CONF_NAME, "")): str,
            vol.Required(CONF_MAC, default=self.config.get(CONF_MAC, "")): str,
        }

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(data),
            errors=errors,
        )
