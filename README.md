# PyCalcLab - Python Engineering Calculator Library

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/my-sample-org-2025/PyCalcLab.svg)](https://github.com/my-sample-org-2025/PyCalcLab/issues)

PyCalcLab is a comprehensive Python library designed for engineering calculations and scientific computing. It provides an extensive collection of mathematical functions, unit conversions, and computational tools that are essential for engineering applications, scientific research, and educational purposes.

## 🚀 Key Features

### Core Calculation Modules
- **Basic Arithmetic**: Fundamental operations with enhanced precision and error handling
- **Trigonometric Functions**: Complete set of trigonometric, inverse, and hyperbolic functions
- **Logarithmic & Exponential**: Natural, common, and custom base logarithms with exponential functions
- **Matrix Operations**: Linear algebra operations including matrix arithmetic, determinants, and vector operations
- **Unit Conversions**: Comprehensive conversion system for length, mass, temperature, pressure, energy, and more

### Advanced Capabilities
- **Engineering Calculations**: Pre-built functions for common engineering problems
- **Financial Mathematics**: Compound interest, exponential growth calculations
- **Vector Operations**: Dot product, cross product, normalization
- **Scientific Constants**: Built-in access to mathematical and physical constants

### Educational and Learning Focus
- **Clear Documentation**: Comprehensive API reference and examples
- **Example Scripts**: Real-world engineering calculation examples
- **Error Handling**: Robust error checking with informative messages
- **Type Hints**: Full type annotation support for better development experience

## 📦 Installation

### Requirements
- Python 3.7 or higher
- NumPy >= 1.21.0
- SciPy >= 1.7.0  
- SymPy >= 1.9.0
- Matplotlib >= 3.5.0

### Install from Source
```bash
git clone https://github.com/my-sample-org-2025/PyCalcLab.git
cd PyCalcLab
pip install -r requirements.txt
pip install -e .
```

### Quick Verification
```python
import pycalclab
from pycalclab import BasicCalculator

calc = BasicCalculator()
print(f"2 + 3 = {calc.add(2, 3)}")  # Output: 2 + 3 = 5
```

## 🛠️ Technology Stack

- **Core Language**: Python 3.7+
- **Numerical Computing**: NumPy, SciPy
- **Symbolic Mathematics**: SymPy  
- **Visualization**: Matplotlib
- **Testing**: pytest
- **Documentation**: Sphinx
- **Code Quality**: black, flake8, mypy

## 📚 Usage Examples

### Basic Arithmetic Operations
```python
from pycalclab import BasicCalculator

calc = BasicCalculator()

# Basic operations
result = calc.add(15, 25)          # 40
result = calc.multiply(7, 8)       # 56
result = calc.power(2, 10)         # 1024
result = calc.square_root(144)     # 12.0
result = calc.factorial(5)         # 120

# List operations
numbers = [1, 2, 3, 4, 5]
total = calc.sum_list(numbers)     # 15
avg = calc.average(numbers)        # 3.0
```

### Trigonometric Functions
```python
from pycalclab import TrigonometricCalculator

trig = TrigonometricCalculator()

# Using degrees
angle = 45
sin_val = trig.sin(angle, degrees=True)    # 0.707...
cos_val = trig.cos(angle, degrees=True)    # 0.707...
tan_val = trig.tan(angle, degrees=True)    # 1.0

# Using radians
import math
angle_rad = math.pi / 4
sin_val = trig.sin(angle_rad)              # 0.707...

# Inverse functions
angle_back = trig.asin(0.707, degrees=True)  # ~45°
```

### Unit Conversions
```python
from pycalclab import UnitConverter

converter = UnitConverter()

# Length conversions
meters_to_feet = converter.convert_length(1, 'm', 'ft')      # 3.28084
inches_to_cm = converter.convert_length(1, 'in', 'cm')       # 2.54

# Temperature conversions  
celsius_to_fahrenheit = converter.convert_temperature(0, 'C', 'F')    # 32.0
fahrenheit_to_celsius = converter.convert_temperature(100, 'F', 'C')  # 37.78

# Engineering units
bar_to_psi = converter.convert_pressure(1, 'bar', 'psi')     # 14.5038
kwh_to_joules = converter.convert_energy(1, 'kWh', 'J')      # 3,600,000
```

### Matrix Operations
```python
from pycalclab import MatrixCalculator

matrix_calc = MatrixCalculator()

# Matrix creation and operations
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8, 9], [10, 11, 12]]

# Matrix addition
result = matrix_calc.add_matrices(matrix_a, matrix_b)

# Vector operations
vector1 = [3, 4, 5]
vector2 = [1, 2, 3]
dot_product = matrix_calc.dot_product(vector1, vector2)        # 26
cross_product = matrix_calc.cross_product_3d(vector1, vector2) # [2, -4, 2]
magnitude = matrix_calc.vector_magnitude(vector1)             # 7.071...
```

### Engineering Calculations Example
```python
from pycalclab import BasicCalculator, UnitConverter

# Beam deflection calculation
calc = BasicCalculator()
converter = UnitConverter()

# Parameters
load = 1000  # N
length = 4.0  # m  
E = 200e9    # Pa (Young's modulus)
I = 8.33e-6  # m^4 (second moment of area)

# Maximum deflection: δ = PL³/(48EI)
deflection = calc.divide(
    calc.multiply(load, calc.power(length, 3)),
    calc.multiply(48, calc.multiply(E, I))
)

deflection_mm = converter.convert_length(deflection, 'm', 'mm')
print(f"Maximum deflection: {deflection_mm:.2f} mm")
```

## 📁 Project Structure

```
PyCalcLab/
├── src/pycalclab/           # Main package source
│   ├── __init__.py          # Package initialization
│   ├── basic.py             # Basic arithmetic operations
│   ├── trigonometric.py     # Trigonometric functions
│   ├── logarithmic.py       # Logarithmic & exponential functions
│   ├── matrix_ops.py        # Matrix and linear algebra operations
│   └── unit_converter.py    # Unit conversion utilities
├── tests/                   # Test suite
│   ├── test_basic.py
│   ├── test_unit_converter.py
│   └── ...
├── examples/                # Usage examples
│   ├── basic_usage.py       # Basic functionality examples
│   └── engineering_calculations.py  # Real-world engineering examples
├── docs/                    # Documentation
│   ├── api_reference.md     # Complete API documentation
│   └── installation.md     # Installation guide
├── requirements.txt         # Dependencies
├── setup.py                # Package setup script
├── pyproject.toml          # Modern Python packaging
└── README.md               # This file
```

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_basic.py

# Run with coverage
python -m pytest tests/ --cov=pycalclab
```

## 📖 Documentation

- **[API Reference](docs/api_reference.md)**: Complete function documentation
- **[Installation Guide](docs/installation.md)**: Detailed setup instructions  
- **[Examples](examples/)**: Practical usage examples
- **Inline Documentation**: All functions include comprehensive docstrings

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with tests
4. Run tests: `python -m pytest`
5. Submit a pull request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/your-username/PyCalcLab.git
cd PyCalcLab

# Install development dependencies
pip install -e .[dev]

# Run tests and linting
python -m pytest
black src/ tests/
flake8 src/ tests/
mypy src/
```

### Contribution Guidelines
- **Code Style**: Follow PEP 8, use `black` for formatting
- **Testing**: Include tests for new functionality
- **Documentation**: Update docstrings and documentation
- **Commit Messages**: Use clear, descriptive commit messages

### Areas for Contribution
- 🧮 Additional mathematical functions
- 🔧 New engineering calculation modules
- 🌍 More unit conversion types
- 📊 Data visualization features
- 🖥️ GUI interface development
- 📚 Documentation improvements
- 🐛 Bug fixes and optimizations

## 🗺️ Roadmap

### Phase 1: Core Foundation ✅
- [x] Basic arithmetic operations
- [x] Trigonometric functions
- [x] Logarithmic functions
- [x] Matrix operations
- [x] Unit conversions
- [x] Comprehensive testing
- [x] Documentation

### Phase 2: Enhanced Features (Planned)
- [ ] **GUI Interface**: Desktop application using PyQt/Tkinter
- [ ] **Graph Visualization**: Plotting capabilities with matplotlib/plotly
- [ ] **Symbolic Mathematics**: Enhanced SymPy integration
- [ ] **Statistical Functions**: Descriptive and inferential statistics
- [ ] **Numerical Methods**: Root finding, integration, differential equations
- [ ] **Physical Constants**: Database of scientific constants

### Phase 3: Advanced Capabilities (Future)
- [ ] **Web API**: REST API for remote calculations
- [ ] **Mobile Support**: Cross-platform mobile app
- [ ] **Cloud Integration**: Cloud-based calculation services
- [ ] **Plugin System**: Extensible architecture for custom modules
- [ ] **3D Visualizations**: Advanced plotting and modeling
- [ ] **Machine Learning**: Basic ML utilities for engineering

### Phase 4: Specialized Modules (Long-term)
- [ ] **Electrical Engineering**: Circuit analysis, signal processing
- [ ] **Mechanical Engineering**: Stress analysis, fluid dynamics
- [ ] **Chemical Engineering**: Process calculations, thermodynamics
- [ ] **Civil Engineering**: Structural analysis, geotechnical calculations

## 🎓 Educational Applications

PyCalcLab is designed with education in mind:

- **Engineering Courses**: Ideal for engineering mathematics, physics, and applied sciences
- **Research Projects**: Reliable foundation for scientific computing
- **Homework Assistance**: Step-by-step calculation examples
- **Self-Learning**: Comprehensive documentation and examples
- **Industry Training**: Real-world engineering calculation examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Scientific Python Community**: NumPy, SciPy, SymPy, Matplotlib developers
- **Contributors**: All individuals who have contributed to this project
- **Educational Institutions**: Universities and schools promoting open-source education
- **Engineering Community**: Professional engineers providing real-world requirements

## 📞 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/my-sample-org-2025/PyCalcLab/issues)
- **Email**: contributors@pycalclab.org  
- **Documentation**: [Full documentation](https://pycalclab.readthedocs.io/)

---

**Made with ❤️ for engineers, scientists, and students worldwide.**

*PyCalcLab - Where Python meets Engineering Excellence*