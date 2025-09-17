# Installation Guide

## Requirements

PyCalcLab requires Python 3.7 or higher and the following dependencies:

- NumPy >= 1.21.0
- SciPy >= 1.7.0
- SymPy >= 1.9.0
- Matplotlib >= 3.5.0

## Installation from Source

1. Clone the repository:
```bash
git clone https://github.com/my-sample-org-2025/PyCalcLab.git
cd PyCalcLab
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install PyCalcLab in development mode:
```bash
pip install -e .
```

## Installation from PyPI (Future)

Once published to PyPI, you'll be able to install with:

```bash
pip install pycalclab
```

## Optional Dependencies

For additional features, you can install optional dependencies:

### Development Tools
```bash
pip install pycalclab[dev]
```

### Documentation Tools
```bash
pip install pycalclab[docs]
```

### GUI Support
```bash
pip install pycalclab[gui]
```

### Visualization Tools
```bash
pip install pycalclab[visualization]
```

## Verification

To verify your installation, run:

```python
import pycalclab
from pycalclab import BasicCalculator

calc = BasicCalculator()
print(f"2 + 3 = {calc.add(2, 3)}")
```

If you see `2 + 3 = 5`, your installation is successful!

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure you're in the correct virtual environment and all dependencies are installed.

2. **Permission errors**: On some systems, you might need to use `sudo` or run as administrator.

3. **Python version**: Ensure you're using Python 3.7 or higher.

For more help, please visit our [GitHub Issues](https://github.com/my-sample-org-2025/PyCalcLab/issues) page.