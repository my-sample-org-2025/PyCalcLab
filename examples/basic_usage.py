#!/usr/bin/env python3
"""
Basic usage examples for PyCalcLab

This script demonstrates the basic functionality of the PyCalcLab library.
"""

import sys
import os

# Add src to path for import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pycalclab import (
    BasicCalculator,
    TrigonometricCalculator,
    LogarithmicCalculator,
    MatrixCalculator,
    UnitConverter
)


def demonstrate_basic_operations():
    """Demonstrate basic arithmetic operations."""
    print("=== Basic Arithmetic Operations ===")
    calc = BasicCalculator()
    
    print(f"Addition: 15 + 25 = {calc.add(15, 25)}")
    print(f"Subtraction: 100 - 37 = {calc.subtract(100, 37)}")
    print(f"Multiplication: 7 × 8 = {calc.multiply(7, 8)}")
    print(f"Division: 84 ÷ 12 = {calc.divide(84, 12)}")
    print(f"Power: 2^10 = {calc.power(2, 10)}")
    print(f"Square root: √144 = {calc.square_root(144)}")
    print(f"Factorial: 5! = {calc.factorial(5)}")
    print(f"Percentage: 15% of 200 = {calc.percentage(200, 15)}")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Sum of {numbers} = {calc.sum_list(numbers)}")
    print(f"Average of {numbers} = {calc.average(numbers)}")
    print()


def demonstrate_trigonometric_functions():
    """Demonstrate trigonometric operations."""
    print("=== Trigonometric Functions ===")
    trig = TrigonometricCalculator()
    
    # Using degrees
    angle_deg = 45
    print(f"sin({angle_deg}°) = {trig.sin(angle_deg, degrees=True):.6f}")
    print(f"cos({angle_deg}°) = {trig.cos(angle_deg, degrees=True):.6f}")
    print(f"tan({angle_deg}°) = {trig.tan(angle_deg, degrees=True):.6f}")
    
    # Using radians
    import math
    angle_rad = math.pi / 4
    print(f"sin(π/4) = {trig.sin(angle_rad):.6f}")
    print(f"cos(π/4) = {trig.cos(angle_rad):.6f}")
    print(f"tan(π/4) = {trig.tan(angle_rad):.6f}")
    
    # Inverse functions
    print(f"arcsin(0.707) = {trig.asin(0.707, degrees=True):.2f}°")
    print(f"arccos(0.707) = {trig.acos(0.707, degrees=True):.2f}°")
    print(f"arctan(1) = {trig.atan(1, degrees=True):.2f}°")
    
    # Hyperbolic functions
    print(f"sinh(1) = {trig.sinh(1):.6f}")
    print(f"cosh(1) = {trig.cosh(1):.6f}")
    print(f"tanh(1) = {trig.tanh(1):.6f}")
    print()


def demonstrate_logarithmic_functions():
    """Demonstrate logarithmic and exponential operations."""
    print("=== Logarithmic & Exponential Functions ===")
    log_calc = LogarithmicCalculator()
    
    print(f"Natural log: ln(10) = {log_calc.ln(10):.6f}")
    print(f"Common log: log₁₀(1000) = {log_calc.log10(1000)}")
    print(f"Binary log: log₂(256) = {log_calc.log2(256)}")
    print(f"Custom base: log₅(125) = {log_calc.log(125, 5)}")
    
    print(f"Exponential: e^2 = {log_calc.exp(2):.6f}")
    print(f"Power of 2: 2^8 = {log_calc.exp2(8)}")
    print(f"Power of 10: 10^3 = {log_calc.exp10(3)}")
    
    # Mathematical constants
    print(f"Euler's number (e) = {log_calc.e_constant():.6f}")
    print(f"Pi (π) = {log_calc.pi_constant():.6f}")
    
    # Financial calculations
    principal = 1000
    rate = 0.05  # 5% annual interest
    years = 10
    compound_freq = 12  # monthly compounding
    
    compound_amount = log_calc.compound_interest(principal, rate, compound_freq, years)
    continuous_amount = log_calc.continuous_compound_interest(principal, rate, years)
    
    print(f"Compound interest (monthly): ${compound_amount:.2f}")
    print(f"Continuous compound interest: ${continuous_amount:.2f}")
    print()


def demonstrate_matrix_operations():
    """Demonstrate matrix and linear algebra operations."""
    print("=== Matrix Operations ===")
    matrix_calc = MatrixCalculator()
    
    # Create sample matrices
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    print("Matrix A:")
    for row in matrix_a:
        print(f"  {row}")
    
    print("Matrix B:")
    for row in matrix_b:
        print(f"  {row}")
    
    # Matrix addition
    result_add = matrix_calc.add_matrices(matrix_a, matrix_b)
    print("A + B:")
    for row in result_add:
        print(f"  {row}")
    
    # Matrix multiplication
    matrix_c = [[1, 2], [3, 4]]
    matrix_d = [[5, 6], [7, 8]]
    
    result_mult = matrix_calc.multiply_matrices(matrix_c, matrix_d)
    print("Matrix multiplication example:")
    print(f"C = {matrix_c}")
    print(f"D = {matrix_d}")
    print(f"C × D = {result_mult}")
    
    # Determinant
    matrix_2x2 = [[3, 8], [4, 6]]
    det_2x2 = matrix_calc.determinant_2x2(matrix_2x2)
    print(f"Determinant of {matrix_2x2} = {det_2x2}")
    
    # Vector operations
    vector_1 = [3, 4, 5]
    vector_2 = [1, 2, 3]
    
    dot_prod = matrix_calc.dot_product(vector_1, vector_2)
    cross_prod = matrix_calc.cross_product_3d(vector_1, vector_2)
    magnitude = matrix_calc.vector_magnitude(vector_1)
    
    print(f"Vector 1: {vector_1}")
    print(f"Vector 2: {vector_2}")
    print(f"Dot product: {dot_prod}")
    print(f"Cross product: {cross_prod}")
    print(f"Magnitude of vector 1: {magnitude:.6f}")
    print()


def demonstrate_unit_conversions():
    """Demonstrate unit conversion capabilities."""
    print("=== Unit Conversions ===")
    converter = UnitConverter()
    
    # Length conversions
    print("Length conversions:")
    print(f"1 meter = {converter.convert_length(1, 'm', 'ft'):.4f} feet")
    print(f"1 inch = {converter.convert_length(1, 'in', 'cm'):.4f} cm")
    print(f"1 mile = {converter.convert_length(1, 'mi', 'km'):.4f} km")
    
    # Mass conversions
    print("\nMass conversions:")
    print(f"1 kg = {converter.convert_mass(1, 'kg', 'lb'):.4f} pounds")
    print(f"1 ounce = {converter.convert_mass(1, 'oz', 'g'):.4f} grams")
    
    # Temperature conversions
    print("\nTemperature conversions:")
    print(f"0°C = {converter.convert_temperature(0, 'C', 'F'):.2f}°F")
    print(f"100°F = {converter.convert_temperature(100, 'F', 'C'):.2f}°C")
    print(f"273.15 K = {converter.convert_temperature(273.15, 'K', 'C'):.2f}°C")
    
    # Engineering units
    print("\nEngineering units:")
    print(f"1 bar = {converter.convert_pressure(1, 'bar', 'psi'):.2f} psi")
    print(f"1 kWh = {converter.convert_energy(1, 'kWh', 'J'):.0f} Joules")
    print(f"1 horsepower = {converter.convert_power(1, 'hp', 'W'):.1f} Watts")
    print()


def main():
    """Main function to run all demonstrations."""
    print("PyCalcLab - Python Engineering Calculator Library")
    print("=" * 50)
    print()
    
    demonstrate_basic_operations()
    demonstrate_trigonometric_functions()
    demonstrate_logarithmic_functions()
    demonstrate_matrix_operations()
    demonstrate_unit_conversions()
    
    print("For more examples and advanced usage, check the documentation!")


if __name__ == "__main__":
    main()