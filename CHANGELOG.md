# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

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

[unreleased]: https://github.com/tlskinneriv/awnet_local/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/tlskinneriv/awnet_local/releases/tag/v0.2.0
