from homeassistant import config_entries
from .const import DOMAIN, CONF_MAC, CONF_NAME

from homeassistant.helpers.device_registry import format_mac
import homeassistant.helpers.config_validation as cv

import voluptuous as vol
import logging

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
            self._name = user_input[CONF_NAME]
            self._mac = format_mac(user_input[CONF_MAC])
            
            await self.async_set_unique_id(self._mac)
            self._abort_if_unique_id_configured(
                updates={CONF_MAC: self._mac}
            )
            
            return self.async_create_entry(
                title=f'{self._name} - {self._mac}',
                data={
                    CONF_NAME: self._name,
                    CONF_MAC: self._mac
                }
            )
        
        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )