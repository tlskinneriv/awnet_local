from typing import Dict
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.device_registry import format_mac
import homeassistant.helpers.config_validation as cv

from .const import (
    DOMAIN,
    CONF_MAC,
    CONF_NAME
)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_MAC): cv.string
    }
)

class AWNConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """AWNET Config Flow"""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle user step."""
        errors: Dict[str, str] = {}
        if user_input is not None:
            _LOGGER.info(user_input)
            name = user_input[CONF_NAME]
            mac = format_mac(user_input[CONF_MAC])

            await self.async_set_unique_id(mac)
            self._abort_if_unique_id_configured(
                updates={CONF_MAC: mac}
            )

            return self.async_create_entry(
                title=f'{name} - {mac}',
                data={
                    CONF_NAME: name,
                    CONF_MAC: mac
                }
            )

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )