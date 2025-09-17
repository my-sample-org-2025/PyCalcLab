# Changelog

All notable changes to PyCalcLab will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- GUI interface using PyQt/Tkinter
- Advanced plotting and visualization features
- Symbolic mathematics integration with SymPy
- Web API for remote calculations
- Mobile application support

## [0.1.0] - 2024-12-17

### Added
- **Core calculation modules:**
  - BasicCalculator: Fundamental arithmetic operations
  - TrigonometricCalculator: Complete trigonometric function suite
  - LogarithmicCalculator: Logarithmic and exponential functions
  - MatrixCalculator: Linear algebra and matrix operations
  - UnitConverter: Comprehensive unit conversion system

- **Mathematical functions:**
  - Basic arithmetic: add, subtract, multiply, divide, power, square root
  - Advanced arithmetic: factorial, percentage, absolute value
  - Trigonometric: sin, cos, tan, asin, acos, atan, atan2
  - Hyperbolic: sinh, cosh, tanh
  - Logarithmic: natural log, common log, binary log, custom base
  - Exponential: exp, exp2, exp10, general power functions
  - Matrix operations: addition, subtraction, multiplication, transpose
  - Determinant calculation for 2x2 and 3x3 matrices
  - Vector operations: dot product, cross product, magnitude, normalization

- **Unit conversions:**
  - Length: metric and imperial units (mm, cm, m, km, in, ft, yd, mi)
  - Mass: metric and imperial units (mg, g, kg, ton, oz, lb, stone)
  - Temperature: Celsius, Fahrenheit, Kelvin, Rankine
  - Pressure: Pa, kPa, MPa, bar, atm, psi, torr, mmHg
  - Energy: J, kJ, MJ, cal, kcal, Wh, kWh, BTU, ft_lb
  - Power: W, kW, MW, hp, BTU/hr
  - Area and volume conversions

- **Engineering applications:**
  - Beam deflection calculations
  - AC electrical circuit analysis
  - Heat transfer calculations
  - Structural stress analysis
  - Fluid flow calculations
  - Vibration analysis

- **Development infrastructure:**
  - Comprehensive test suite with unittest
  - Type hints throughout codebase
  - Detailed API documentation
  - Real-world engineering examples
  - Modern Python packaging (setup.py, pyproject.toml)
  - Development guidelines and contribution documentation

- **Documentation:**
  - Complete README with usage examples
  - API reference documentation
  - Installation guide
  - Contributing guidelines
  - Example scripts for basic usage and engineering calculations

### Technical Details
- **Python compatibility:** 3.7+
- **Dependencies:** NumPy, SciPy, SymPy, Matplotlib
- **Testing:** 18 unit tests covering core functionality
- **Code quality:** PEP 8 compliant with type hints
- **License:** MIT License

### Examples Added
- `basic_usage.py`: Demonstrates all core functionality
- `engineering_calculations.py`: Real-world engineering examples including:
  - Structural beam deflection
  - Electrical circuit impedance
  - Heat transfer through composite walls
  - Stress analysis with safety factors
  - Pressure drop in pipe flow
  - Natural frequency calculations

### Project Structure
```
PyCalcLab/
├── src/pycalclab/           # Main package
├── tests/                   # Test suite  
├── examples/                # Usage examples
├── docs/                    # Documentation
├── requirements.txt         # Dependencies
├── setup.py                # Package setup
├── pyproject.toml          # Modern packaging
├── LICENSE                 # MIT license
├── README.md               # Project overview
├── CONTRIBUTING.md         # Contribution guidelines
└── CHANGELOG.md            # This file
```

---

## Version History Notes

### Version 0.1.0 Goals Achieved ✅
- [x] Complete core mathematical functionality
- [x] Comprehensive unit conversion system  
- [x] Real-world engineering examples
- [x] Robust testing framework
- [x] Professional documentation
- [x] Modern Python packaging
- [x] Clear development guidelines

### Next Version (0.2.0) Goals
- [ ] GUI interface development
- [ ] Enhanced visualization capabilities
- [ ] Statistical functions module
- [ ] Symbolic mathematics integration
- [ ] Performance optimizations
- [ ] Additional engineering modules