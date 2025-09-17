"""
Test cases for BasicCalculator module
"""

import unittest
import sys
import os

# Add src to path for import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pycalclab.basic import BasicCalculator


class TestBasicCalculator(unittest.TestCase):
    """Test cases for BasicCalculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = BasicCalculator()
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 4), -3)
        self.assertAlmostEqual(self.calc.subtract(0.5, 0.2), 0.3, places=10)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.4), 0.2, places=10)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 3), 7/3)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2)
    
    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        
        # Test negative input
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_absolute(self):
        """Test absolute value operation."""
        self.assertEqual(self.calc.absolute(-5), 5)
        self.assertEqual(self.calc.absolute(3), 3)
        self.assertEqual(self.calc.absolute(0), 0)
    
    def test_factorial(self):
        """Test factorial operation."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        
        # Test negative input
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        
        # Test non-integer input
        with self.assertRaises(ValueError):
            self.calc.factorial(3.5)
    
    def test_percentage(self):
        """Test percentage calculation."""
        self.assertEqual(self.calc.percentage(100, 50), 50)
        self.assertEqual(self.calc.percentage(200, 25), 50)
        self.assertEqual(self.calc.percentage(80, 12.5), 10)
    
    def test_sum_list(self):
        """Test sum of list."""
        self.assertEqual(self.calc.sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(self.calc.sum_list([]), 0)
        self.assertEqual(self.calc.sum_list([-1, 1, -2, 2]), 0)
    
    def test_average(self):
        """Test average calculation."""
        self.assertEqual(self.calc.average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.calc.average([10, 20, 30]), 20)
        
        # Test empty list
        with self.assertRaises(ValueError):
            self.calc.average([])


if __name__ == '__main__':
    unittest.main()