"""
PyCalcLab - Python Engineering Calculator Library

A comprehensive engineering calculator library for Python with support for
advanced mathematical operations, scientific computing, and engineering calculations.

Author: PyCalcLab Contributors
License: MIT
"""

__version__ = "0.1.0"
__author__ = "PyCalcLab Contributors"
__email__ = "contributors@pycalclab.org"

from .basic import BasicCalculator
from .trigonometric import TrigonometricCalculator
from .logarithmic import LogarithmicCalculator
from .matrix_ops import MatrixCalculator
from .unit_converter import UnitConverter

__all__ = [
    "BasicCalculator",
    "TrigonometricCalculator", 
    "LogarithmicCalculator",
    "MatrixCalculator",
    "UnitConverter"
]