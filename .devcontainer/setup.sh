#!/bin/bash
mkdir -p config

source bin/activate
hass --script ensure_config -c config

if ! grep -R "logger" config/configuration.yaml >> /dev/null;then
echo "
logger:
  default: info
  logs:
    homeassistant.components.cloud: debug
    custom_components.awnet_local: debug
" >> config/configuration.yaml
fi