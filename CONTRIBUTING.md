# Contributing to PyCalcLab

Thank you for your interest in contributing to PyCalcLab! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Development Setup

1. **Fork and clone the repository:**
```bash
git clone https://github.com/your-username/PyCalcLab.git
cd PyCalcLab
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install development dependencies:**
```bash
pip install -r requirements.txt
pip install -e .
```

4. **Install optional development tools:**
```bash
pip install pytest pytest-cov black flake8 mypy
```

### Running Tests

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python -m unittest tests.test_basic

# Check code coverage (if pytest-cov is installed)
python -m pytest tests/ --cov=pycalclab --cov-report=html
```

### Code Quality

```bash
# Format code
black src/ tests/ examples/

# Check style
flake8 src/ tests/ examples/

# Type checking
mypy src/
```

## 📝 Contribution Guidelines

### Code Style

- Follow [PEP 8](https://pep8.org/) Python style guide
- Use `black` for automatic code formatting
- Maximum line length: 88 characters
- Use type hints for all function parameters and return values
- Write comprehensive docstrings for all public functions and classes

### Testing

- Write tests for all new functionality
- Ensure existing tests continue to pass
- Aim for high test coverage
- Use descriptive test names that explain what is being tested
- Test edge cases and error conditions

### Documentation

- Update docstrings for any modified functions
- Update API documentation if needed
- Add examples for new features
- Update README.md if adding major features

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add matrix determinant calculation for 3x3 matrices
fix: handle division by zero in unit conversion
docs: update API reference for trigonometric functions
test: add comprehensive tests for logarithmic functions
```

### Pull Request Process

1. **Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes with tests and documentation**

3. **Ensure code quality:**
```bash
python -m unittest discover tests/
black src/ tests/ examples/
flake8 src/ tests/ examples/
```

4. **Commit your changes:**
```bash
git add .
git commit -m "feat: descriptive commit message"
```

5. **Push to your fork:**
```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request** with a clear description of your changes

## 🎯 Areas for Contribution

### High Priority
- **Additional Mathematical Functions**: More specialized engineering functions
- **Unit Conversions**: Additional unit types and conversions
- **Error Handling**: Improved error messages and edge case handling
- **Performance Optimization**: Speed improvements for large calculations
- **Documentation**: Examples, tutorials, and API improvements

### Medium Priority
- **GUI Development**: Desktop application using PyQt or Tkinter
- **Visualization**: Plotting and graphing capabilities
- **Statistical Functions**: Descriptive and inferential statistics
- **Numerical Methods**: Root finding, integration, differential equations
- **File I/O**: Import/export functionality for calculations

### Future Features
- **Web API**: REST API for remote calculations  
- **Mobile Support**: Cross-platform mobile application
- **Cloud Integration**: Cloud-based calculation services
- **Plugin System**: Architecture for custom modules

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, please include:

- **Python version** and operating system  
- **PyCalcLab version**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Code sample** that demonstrates the issue
- **Error messages** (full traceback if applicable)

### Feature Requests

When requesting features, please include:

- **Clear description** of the proposed feature
- **Use case** - why would this be useful?
- **Examples** of how it would be used
- **References** to similar functionality in other libraries

## 📚 Development Resources

### Project Structure
```
PyCalcLab/
├── src/pycalclab/           # Main package source
├── tests/                   # Test suite
├── examples/                # Usage examples
├── docs/                    # Documentation
├── requirements.txt         # Dependencies
├── setup.py                # Package setup
└── pyproject.toml          # Modern Python packaging
```

### Key Modules
- `basic.py` - Fundamental arithmetic operations
- `trigonometric.py` - Trigonometric functions
- `logarithmic.py` - Logarithmic and exponential functions
- `matrix_ops.py` - Matrix and linear algebra operations
- `unit_converter.py` - Unit conversion utilities

### Dependencies
- **NumPy**: Numerical computing
- **SciPy**: Scientific computing  
- **SymPy**: Symbolic mathematics
- **Matplotlib**: Plotting and visualization

## 🤝 Community Guidelines

### Code of Conduct

- **Be respectful** and inclusive to all contributors
- **Be constructive** in feedback and discussions
- **Help others** learn and grow
- **Ask questions** when you need clarification
- **Give credit** where credit is due

### Communication

- **GitHub Issues**: For bug reports and feature requests
- **Pull Requests**: For code contributions
- **Discussions**: For general questions and ideas

## 🏆 Recognition

Contributors will be recognized in:

- **Contributors section** of README.md
- **Release notes** for significant contributions  
- **Documentation** for major feature additions

## ❓ Questions?

If you have questions about contributing:

- **Check existing issues** to see if your question has been asked
- **Create a new issue** with the "question" label
- **Email the maintainers** at contributors@pycalclab.org

---

Thank you for helping make PyCalcLab better for everyone! 🚀