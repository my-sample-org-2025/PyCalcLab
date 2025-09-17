"""
Trigonometric functions for PyCalcLab

This module provides comprehensive trigonometric operations including
standard trig functions, inverse functions, and hyperbolic functions.
"""

import math
from typing import Union

Number = Union[int, float]


class TrigonometricCalculator:
    """Calculator for trigonometric operations."""
    
    # Standard trigonometric functions
    @staticmethod
    def sin(x: Number, degrees: bool = False) -> float:
        """Calculate sine of x."""
        if degrees:
            x = math.radians(x)
        return math.sin(x)
    
    @staticmethod
    def cos(x: Number, degrees: bool = False) -> float:
        """Calculate cosine of x."""
        if degrees:
            x = math.radians(x)
        return math.cos(x)
    
    @staticmethod
    def tan(x: Number, degrees: bool = False) -> float:
        """Calculate tangent of x."""
        if degrees:
            x = math.radians(x)
        return math.tan(x)
    
    # Inverse trigonometric functions
    @staticmethod
    def asin(x: Number, degrees: bool = False) -> float:
        """Calculate arcsine of x."""
        if not -1 <= x <= 1:
            raise ValueError("asin input must be between -1 and 1")
        result = math.asin(x)
        return math.degrees(result) if degrees else result
    
    @staticmethod
    def acos(x: Number, degrees: bool = False) -> float:
        """Calculate arccosine of x."""
        if not -1 <= x <= 1:
            raise ValueError("acos input must be between -1 and 1")
        result = math.acos(x)
        return math.degrees(result) if degrees else result
    
    @staticmethod
    def atan(x: Number, degrees: bool = False) -> float:
        """Calculate arctangent of x."""
        result = math.atan(x)
        return math.degrees(result) if degrees else result
    
    @staticmethod
    def atan2(y: Number, x: Number, degrees: bool = False) -> float:
        """Calculate arctangent of y/x considering quadrant."""
        result = math.atan2(y, x)
        return math.degrees(result) if degrees else result
    
    # Hyperbolic functions
    @staticmethod
    def sinh(x: Number) -> float:
        """Calculate hyperbolic sine of x."""
        return math.sinh(x)
    
    @staticmethod
    def cosh(x: Number) -> float:
        """Calculate hyperbolic cosine of x."""
        return math.cosh(x)
    
    @staticmethod
    def tanh(x: Number) -> float:
        """Calculate hyperbolic tangent of x."""
        return math.tanh(x)
    
    # Utility functions
    @staticmethod
    def degrees_to_radians(degrees: Number) -> float:
        """Convert degrees to radians."""
        return math.radians(degrees)
    
    @staticmethod
    def radians_to_degrees(radians: Number) -> float:
        """Convert radians to degrees."""
        return math.degrees(radians)
    
    @staticmethod
    def secant(x: Number, degrees: bool = False) -> float:
        """Calculate secant (1/cos) of x."""
        cos_val = TrigonometricCalculator.cos(x, degrees)
        if cos_val == 0:
            raise ValueError("Secant is undefined when cosine is zero")
        return 1 / cos_val
    
    @staticmethod
    def cosecant(x: Number, degrees: bool = False) -> float:
        """Calculate cosecant (1/sin) of x."""
        sin_val = TrigonometricCalculator.sin(x, degrees)
        if sin_val == 0:
            raise ValueError("Cosecant is undefined when sine is zero")
        return 1 / sin_val
    
    @staticmethod
    def cotangent(x: Number, degrees: bool = False) -> float:
        """Calculate cotangent (1/tan) of x."""
        tan_val = TrigonometricCalculator.tan(x, degrees)
        if tan_val == 0:
            raise ValueError("Cotangent is undefined when tangent is zero")
        return 1 / tan_val