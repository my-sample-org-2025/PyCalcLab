"""
Basic arithmetic operations for PyCalcLab

This module provides fundamental arithmetic operations and basic mathematical functions.
"""

import math
from typing import Union, List

Number = Union[int, float]


class BasicCalculator:
    """Basic calculator with fundamental arithmetic operations."""
    
    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """Subtract b from a."""
        return a - b
    
    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a: Number, b: Number) -> Number:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    @staticmethod
    def power(base: Number, exponent: Number) -> Number:
        """Raise base to the power of exponent."""
        return pow(base, exponent)
    
    @staticmethod
    def square_root(x: Number) -> Number:
        """Calculate square root of x."""
        if x < 0:
            raise ValueError("Square root of negative number is not real")
        return math.sqrt(x)
    
    @staticmethod
    def absolute(x: Number) -> Number:
        """Calculate absolute value of x."""
        return abs(x)
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial of n."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(n)
    
    @staticmethod
    def percentage(value: Number, percentage: Number) -> Number:
        """Calculate percentage of a value."""
        return (value * percentage) / 100
    
    @staticmethod
    def sum_list(numbers: List[Number]) -> Number:
        """Calculate sum of a list of numbers."""
        return sum(numbers)
    
    @staticmethod
    def average(numbers: List[Number]) -> Number:
        """Calculate average of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        return sum(numbers) / len(numbers)