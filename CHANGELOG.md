# Changelog

All notable changes to this project will be documented in this file.

The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project uses [Semantic Versioning](https://semver.org/).

---

## [1.0.1] - 2026-03-06

### Fixed
- Removed overly strict function validation that evaluated `f(0)`, which prevented valid functions like `1/log(x)`.
- Fixed domain handling so functions with restricted domains (e.g., logarithms) can still be used.

### Added
- Added `ln(x)` as an alias for `log(x)` in function input.

---

## [1.0.0] - 2026-03-05

### Added
- Initial release of **NumInt**.
- Numerical approximation methods:
  - Left-hand Riemann sum
  - Right-hand Riemann sum
  - Midpoint (center) rule
  - Trapezoidal rule
  - Simpson’s rule
- Interactive mode for step-by-step input.
- Command-line interface for one-off calculations.
- Automatic computation of exact integral using **SymPy** when possible.
- Absolute error reporting when exact value is available.
- Support for mathematical constants `pi` and `e`.
- Prebuilt Windows executable.