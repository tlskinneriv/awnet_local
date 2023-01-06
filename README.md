# Ambient Weather Station - Local

## Overview

You can use this integration to take advantage of the new "Custom Server" feature in AWNET available in Firmware [4.2.8](https://ambientweather.com/support) on the WS-2902A, WS-2902B, WS-2902C, WS-2000 And WS-5000. I have tested this using my WS-2902C. It receives service calls from the [AWNET](https://github.com/tlskinneriv/hassio-addons/tree/master/awnet) add-on and updates entities associated with the WS device. The implementation of this integration is based largely on the built-in Ambient Weather Station component already available in Home Assistant.

## Installation

Place the `custom_components` folder in your configuration directory (or add its contents to an existing `custom_components` folder). Alternatively install via [HACS](https://hacs.xyz/) using a custom repository.

## Configuration

Configuration is performed via the Home Assistant user interface. You will need the following information:

- Name: a friendly name for the device to display in Home Assistant
- MAC: the MAC address for the device

Once configured, setup the accompanying add-on [AWNET](https://github.com/tlskinneriv/hassio-addons/tree/master/awnet) (see the [docs](https://github.com/tlskinneriv/hassio-addons/blob/master/awnet/DOCS.md) for direct instructions).

## Known Issues

Currently, there is not a method implemented to determine what sensors a weather station supports.
Therefore, all possible supported sensors are populated for the integration (this list was
originally pulled from the [cloud-based
integration](https://github.com/home-assistant/core/tree/dev/homeassistant/components/ambient_station)).
The sensors will populate as "Unavailable" until a value is received from the add-on. Sensors not
populated by the device will remain in the "Unavailable" state. Recommendation is to disable the
unsupported sensors until such a method is implemented. Many uncommon sensors are disabled by default.
