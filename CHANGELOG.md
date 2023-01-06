# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

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
- Device class and native unit management (thanks [@mkmer]!); unit conversoins will now work
- Clarifiy actual sensor states as "Unavailable" instead of "Unknown" in README
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
[@mkmer]: (https://github.com/mkmer)

<!-- Versions -->

[unreleased]: https://github.com/tlskinneriv/awnet_local/compare/v0..0...HEAD
[0.3.0]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/tlskinneriv/awnet_local/releases/tag/v0.2.0
