# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [unreleased] - 2023-02-25

### Added

- Minimum Home Assistant version (currently 2023.1.0) for unit compatibility
- New sensors based on the information at https://ambientweather.com/faqs/question/view/id/1857/
  - CO2 Indoor
  - CO2 Indoor 24h Avg
  - Lightning Strike Distance
  - Lightning Strike Timestamp
  - PM Indoor Humidity
  - PM Indoor Temp
  - PM10 Indoor
  - PM10 Indoor 24h Avg
- New sensors based on new information at
  https://github.com/ambient-weather/api-docs/wiki/Device-Data-Specs#data-timing
  - Leaf Wetness 1-8
  - Soil Tension 1-4
  - Evapotranspiration Short
  - Evapotranspiration Tall
  - Growing Degree Days
  - PM2.5 Indoor AQIN
  - PM10 Indoor AQIN
  - AQI from PM2.5 Indoor AQIN
  - AQI from PM10 Indoor AQIN
- New calculated sensors based on new information at
  https://github.com/ambient-weather/api-docs/wiki/Device-Data-Specs#data-timing
  - Dew Point Indoor
  - Feels Like Indoor
- New binary sensors based on the information at
  https://ambientweather.com/faqs/question/view/id/1857/
  - Rain Guage Battery
  - Relay 1-10 Battery

### Changed

- New entity name format (thanks @mkmer!)
- Updated default sensor names for case consistency
- Average values now MEASUREMENT instead of TOTAL_INCREASING

### Housekeeping

- Updated dev environment
- Bump to Python 3.10 for devcontainer
- Adopt black as formatter for Python code
- Add missing inline documentation
- Break sensor and binary_sensor constants into separate files

## [0.3.0] - 2023-01-06

### Added

- New sensors pulled from the native HA Ambient Weather integration:
  - AQI PM2.5
  - AQI PM2.5 24h avg
  - AQI PM2.5 indoor
  - AQI PM2.5 indoor 24h avg
  - Lightning Strikes Per Day
  - Lightning Strikes Per Hour
- New binary sensors pulled from the native HA Ambient Weather integration:
  - Interior Battery
  - Leak Detector 1-4
  - Leak Detector Battery 1-4
  - Lightning Detector Battery
  - Soil Monitor Battery 1-10
- Default icon for UV Index sensor

### Changed

- Remove underscore from default sensor names
- Device class and native unit management (thanks @mkmer!); unit conversions will now work
- Clarify actual sensor states as "Unavailable" instead of "Unknown" in README
- Less common sensors are disabled by default
- Update manifest fields

### Removed

- Default icons where no longer needed:
  - 24 Hr Rain
  - Daily Rain
  - Event Rain
  - Hourly Rain Rate
  - Lifetime Rain
  - Max Gust
  - Monthly Rain
  - Weekly Rain
  - Wind Avg 10m
  - Wind Avg 2m
  - Wind Gust
  - Wind Speed
  - Yearly Rain

## [0.2.2] - 2022-08-15

### Added

- Calculations for the following sensors:
  - Dew Point
  - Feels Like
  - Solar Radiation (Lux)
  - Last Rain

### Fixed

- Fix for VS code pylint missing Home Assistant code
- Formatting fixes

## [0.2.1] - 2022-07-31

### Added

- Support for alternate MAC dictionary key for the MAC address to support WS-5000

### Fixed

- Check for properly formatted MAC, throw useful error messages if not
- Errors that were showing for entities that are enabled but don't have data in a previous data update
- Set VS code formatter and fix some formatting

## [0.2.0] - 2022-01-23

### Added

- VS Code devcontainer definition
- Support all sensors supported by the cloud-based Ambient Weather component, unavailable by default

### Changed

- Sensors now unavailable by default until data is received

### Fixed

- 'None' handling for raw datetime parsing in TYPE_LASTRAIN data

## [0.1.0] - 2022-01-01

- initial release

<!-- Links -->

[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html

<!-- Versions -->

[unreleased]: https://github.com/tlskinneriv/awnet_local/compare/v0..0...HEAD
[0.3.0]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/tlskinneriv/awnet_local/releases/tag/v0.2.0
