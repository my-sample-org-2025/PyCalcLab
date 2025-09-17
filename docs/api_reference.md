# API Reference

## BasicCalculator

### Class: `pycalclab.BasicCalculator`

Provides fundamental arithmetic operations.

#### Methods

##### `add(a, b)`
Add two numbers.
- **Parameters:** `a`, `b` (int or float) - Numbers to add
- **Returns:** Sum of a and b
- **Example:** `calc.add(2, 3)` returns `5`

##### `subtract(a, b)` 
Subtract b from a.
- **Parameters:** `a`, `b` (int or float) - Numbers for subtraction
- **Returns:** Difference a - b
- **Example:** `calc.subtract(5, 3)` returns `2`

##### `multiply(a, b)`
Multiply two numbers.
- **Parameters:** `a`, `b` (int or float) - Numbers to multiply
- **Returns:** Product of a and b
- **Example:** `calc.multiply(4, 5)` returns `20`

##### `divide(a, b)`
Divide a by b.
- **Parameters:** `a`, `b` (int or float) - Dividend and divisor
- **Returns:** Quotient a / b
- **Raises:** `ValueError` if b is zero
- **Example:** `calc.divide(10, 2)` returns `5`

##### `power(base, exponent)`
Raise base to the power of exponent.
- **Parameters:** `base`, `exponent` (int or float)
- **Returns:** base^exponent
- **Example:** `calc.power(2, 3)` returns `8`

##### `square_root(x)`
Calculate square root of x.
- **Parameters:** `x` (int or float) - Non-negative number
- **Returns:** Square root of x
- **Raises:** `ValueError` if x is negative
- **Example:** `calc.square_root(9)` returns `3`

##### `factorial(n)`
Calculate factorial of n.
- **Parameters:** `n` (int) - Non-negative integer
- **Returns:** n! (factorial of n)
- **Raises:** `ValueError` if n is negative or not an integer
- **Example:** `calc.factorial(5)` returns `120`

---

## TrigonometricCalculator

### Class: `pycalclab.TrigonometricCalculator`

Provides trigonometric functions.

#### Methods

##### `sin(x, degrees=False)`
Calculate sine of x.
- **Parameters:** 
  - `x` (int or float) - Angle
  - `degrees` (bool) - If True, x is in degrees; if False, x is in radians
- **Returns:** Sine of x
- **Example:** `trig.sin(90, degrees=True)` returns `1.0`

##### `cos(x, degrees=False)`
Calculate cosine of x.
- **Parameters:** 
  - `x` (int or float) - Angle
  - `degrees` (bool) - If True, x is in degrees; if False, x is in radians
- **Returns:** Cosine of x
- **Example:** `trig.cos(0, degrees=True)` returns `1.0`

##### `tan(x, degrees=False)`
Calculate tangent of x.
- **Parameters:** 
  - `x` (int or float) - Angle
  - `degrees` (bool) - If True, x is in degrees; if False, x is in radians
- **Returns:** Tangent of x
- **Example:** `trig.tan(45, degrees=True)` returns `1.0`

---

## LogarithmicCalculator

### Class: `pycalclab.LogarithmicCalculator`

Provides logarithmic and exponential functions.

#### Methods

##### `ln(x)`
Calculate natural logarithm of x.
- **Parameters:** `x` (int or float) - Positive number
- **Returns:** Natural logarithm of x
- **Raises:** `ValueError` if x <= 0
- **Example:** `log_calc.ln(math.e)` returns `1.0`

##### `log10(x)`
Calculate common logarithm (base 10) of x.
- **Parameters:** `x` (int or float) - Positive number
- **Returns:** Base-10 logarithm of x
- **Raises:** `ValueError` if x <= 0
- **Example:** `log_calc.log10(100)` returns `2.0`

##### `exp(x)`
Calculate e^x.
- **Parameters:** `x` (int or float) - Exponent
- **Returns:** e raised to the power of x
- **Example:** `log_calc.exp(1)` returns `2.718...`

---

## MatrixCalculator

### Class: `pycalclab.MatrixCalculator`

Provides matrix operations.

#### Methods

##### `add_matrices(matrix1, matrix2)`
Add two matrices.
- **Parameters:** `matrix1`, `matrix2` (List[List[Number]]) - Matrices of same dimensions
- **Returns:** Sum of the matrices
- **Raises:** `ValueError` if matrices have different dimensions
- **Example:** `matrix_calc.add_matrices([[1,2],[3,4]], [[5,6],[7,8]])` returns `[[6,8],[10,12]]`

##### `multiply_matrices(matrix1, matrix2)`
Multiply two matrices.
- **Parameters:** `matrix1`, `matrix2` (List[List[Number]]) - Compatible matrices
- **Returns:** Product of the matrices
- **Raises:** `ValueError` if matrices are not compatible for multiplication
- **Example:** Matrix multiplication following standard rules

##### `determinant_2x2(matrix)`
Calculate determinant of a 2x2 matrix.
- **Parameters:** `matrix` (List[List[Number]]) - 2x2 matrix
- **Returns:** Determinant value
- **Raises:** `ValueError` if matrix is not 2x2
- **Example:** `matrix_calc.determinant_2x2([[1,2],[3,4]])` returns `-2`

---

## UnitConverter

### Class: `pycalclab.UnitConverter`

Provides unit conversions for various physical quantities.

#### Methods

##### `convert_length(value, from_unit, to_unit)`
Convert between length units.
- **Parameters:** 
  - `value` (int or float) - Value to convert
  - `from_unit` (str) - Source unit (e.g., 'm', 'ft', 'km')
  - `to_unit` (str) - Target unit
- **Returns:** Converted value
- **Example:** `converter.convert_length(1, 'm', 'ft')` returns `3.28084`

##### `convert_temperature(value, from_unit, to_unit)`
Convert between temperature units.
- **Parameters:**
  - `value` (int or float) - Temperature value
  - `from_unit` (str) - Source unit ('C', 'F', 'K', 'R')
  - `to_unit` (str) - Target unit
- **Returns:** Converted temperature
- **Example:** `converter.convert_temperature(0, 'C', 'F')` returns `32.0`

##### `get_available_units(unit_type)`
Get available units for a unit type.
- **Parameters:** `unit_type` (str) - Type of units ('length', 'mass', 'temperature', etc.)
- **Returns:** List of available units
- **Example:** `converter.get_available_units('length')` returns `['mm', 'cm', 'm', 'km', ...]`

## Supported Units

### Length
- Metric: mm, cm, m, km, μm, nm
- Imperial: in, ft, yd, mi, mil

### Mass  
- Metric: mg, g, kg, ton
- Imperial: oz, lb, stone

### Temperature
- C (Celsius), F (Fahrenheit), K (Kelvin), R (Rankine)

### Pressure
- Pa, kPa, MPa, bar, atm, psi, torr, mmHg

### Energy
- J, kJ, MJ, cal, kcal, Wh, kWh, BTU, ft_lb

### Power
- W, kW, MW, hp, BTU/hr

For complete API documentation, see the docstrings in the source code.