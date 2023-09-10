[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

# Ambient Weather Station - Local

## Overview

You can use this integration to take advantage of the new "Custom Server" feature in AWNET available in Firmware [4.2.8](https://ambientweather.com/support). It receives service calls from the [AWNET](https://github.com/tlskinneriv/hassio-addons/tree/master/awnet) add-on and updates entities associated with the WS device. The implementation of this integration is based largely on the built-in Ambient Weather Station component already available in Home Assistant.

## Known Working Devices

The following list of devices are known to work with this integration. This list may not be complete (please submit an issue if your device isn't listed and is working with the integration). The integration is currently tested using a WS-2902C.

- WS-2902A
- WS-2902B
- WS-2902C
- WS-2902D
- WS-2000
- WS-5000

## Installation

Place the `custom_components` folder in your configuration directory (or add its contents to an existing `custom_components` folder). Alternatively install via [HACS](https://hacs.xyz/).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=tlskinneriv&repository=awnet_local&category=integration)

## Configuration

Configuration is performed via the Home Assistant user interface. You will need the following information:

- Name: a friendly name for the device to display in Home Assistant
- MAC: the MAC address for the device

Once configured, setup the accompanying add-on
[AWNET](https://github.com/tlskinneriv/hassio-addons/tree/master/awnet) (see the
[docs](https://github.com/tlskinneriv/hassio-addons/blob/master/awnet/DOCS.md) for direct
instructions).

> NOTE: Entities for the device will not show up until the add-on referenced above is installed and
> the settings are properly configured on the Ambient Weather device. Currently, the integration
> supports only one weather station.

## Service

This integration provides a service that can be called (`awnet_local.update`) to update the values for
the sensors. The service requires at least the MAC address of the device to be entered into the
`PASSKEY` field. An example of a service call is below:

```yaml
service: awnet_local.update
data:
  stationtype: AMBWeatherV4.3.4
  PASSKEY: "123456123456"
  dateutc: "2021-12-30 16:08:46"
  humidityin: "59"
  baromrelin: "30.000"
  baromabsin: "29.929"
  tempf: "89.0"
  battout: "1"
  humidity: "40"
  winddir: "245"
  windspeedmph: "3.0"
  windgustmph: "0.0"
  maxdailygust: "8.1"
  hourlyrainin: "0.00"
  eventrainin: "0.000"
  dailyrainin: "0.000"
  weeklyrainin: "0.039"
  monthlyrainin: "0.039"
  totalrainin: "0.039"
  solarradiation: "135.4"
  uv: "1"
  batt_co2: "1"
  tempinf: "86.5"
```

Currently, the only fields exposed by the GUI are the `PASSKEY` and `stationtype` fields. This
service is called by the accompanying AWNET add-on, but can also be called separately via the HA API
or other methods in the case that the add-on is not used.
