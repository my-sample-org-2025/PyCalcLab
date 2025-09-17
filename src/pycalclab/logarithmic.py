"""
Logarithmic and exponential functions for PyCalcLab

This module provides logarithmic, exponential, and related mathematical operations.
"""

import math
from typing import Union

Number = Union[int, float]


class LogarithmicCalculator:
    """Calculator for logarithmic and exponential operations."""
    
    # Logarithmic functions
    @staticmethod
    def log(x: Number, base: Number = math.e) -> float:
        """Calculate logarithm of x with given base (default: natural log)."""
        if x <= 0:
            raise ValueError("Logarithm input must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        
        if base == math.e:
            return math.log(x)
        else:
            return math.log(x) / math.log(base)
    
    @staticmethod
    def ln(x: Number) -> float:
        """Calculate natural logarithm (base e) of x."""
        if x <= 0:
            raise ValueError("Natural logarithm input must be positive")
        return math.log(x)
    
    @staticmethod
    def log10(x: Number) -> float:
        """Calculate common logarithm (base 10) of x."""
        if x <= 0:
            raise ValueError("Logarithm input must be positive")
        return math.log10(x)
    
    @staticmethod
    def log2(x: Number) -> float:
        """Calculate binary logarithm (base 2) of x."""
        if x <= 0:
            raise ValueError("Logarithm input must be positive")
        return math.log2(x)
    
    # Exponential functions
    @staticmethod
    def exp(x: Number) -> float:
        """Calculate e^x (exponential function)."""
        return math.exp(x)
    
    @staticmethod
    def exp2(x: Number) -> float:
        """Calculate 2^x."""
        return pow(2, x)
    
    @staticmethod
    def exp10(x: Number) -> float:
        """Calculate 10^x."""
        return pow(10, x)
    
    @staticmethod
    def power_general(base: Number, exponent: Number) -> float:
        """Calculate base^exponent for any base and exponent."""
        if base == 0 and exponent <= 0:
            raise ValueError("0 cannot be raised to non-positive power")
        if base < 0 and not isinstance(exponent, int):
            raise ValueError("Negative base with non-integer exponent results in complex number")
        return pow(base, exponent)
    
    # Special mathematical constants and functions
    @staticmethod
    def e_constant() -> float:
        """Return Euler's number (e ≈ 2.71828)."""
        return math.e
    
    @staticmethod
    def pi_constant() -> float:
        """Return pi (π ≈ 3.14159)."""
        return math.pi
    
    @staticmethod
    def exponential_growth(initial: Number, rate: Number, time: Number) -> float:
        """
        Calculate exponential growth: initial * e^(rate * time)
        
        Args:
            initial: Initial value
            rate: Growth rate
            time: Time period
        """
        return initial * math.exp(rate * time)
    
    @staticmethod
    def compound_interest(principal: Number, rate: Number, times_compounded: int, years: Number) -> float:
        """
        Calculate compound interest: P(1 + r/n)^(nt)
        
        Args:
            principal: Initial amount
            rate: Annual interest rate (as decimal)
            times_compounded: Number of times interest is compounded per year
            years: Number of years
        """
        if times_compounded <= 0:
            raise ValueError("Compounding frequency must be positive")
        return principal * pow(1 + rate / times_compounded, times_compounded * years)
    
    @staticmethod
    def continuous_compound_interest(principal: Number, rate: Number, years: Number) -> float:
        """
        Calculate continuous compound interest: P * e^(rt)
        
        Args:
            principal: Initial amount
            rate: Annual interest rate (as decimal)
            years: Number of years
        """
        return principal * math.exp(rate * years)