"""
Test cases for UnitConverter module
"""

import unittest
import sys
import os

# Add src to path for import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pycalclab.unit_converter import UnitConverter


class TestUnitConverter(unittest.TestCase):
    """Test cases for UnitConverter class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.converter = UnitConverter()
    
    def test_length_conversions(self):
        """Test length unit conversions."""
        # Meter to various units
        self.assertAlmostEqual(self.converter.convert_length(1, 'm', 'cm'), 100)
        self.assertAlmostEqual(self.converter.convert_length(1, 'm', 'mm'), 1000)
        self.assertAlmostEqual(self.converter.convert_length(1000, 'm', 'km'), 1)
        
        # Imperial conversions
        self.assertAlmostEqual(self.converter.convert_length(1, 'ft', 'in'), 12)
        self.assertAlmostEqual(self.converter.convert_length(1, 'yd', 'ft'), 3)
        self.assertAlmostEqual(self.converter.convert_length(1, 'mi', 'ft'), 5280)
        
        # Mixed conversions
        self.assertAlmostEqual(self.converter.convert_length(1, 'm', 'ft'), 3.28084, places=5)
        self.assertAlmostEqual(self.converter.convert_length(1, 'in', 'cm'), 2.54)
    
    def test_mass_conversions(self):
        """Test mass unit conversions."""
        # Metric conversions
        self.assertAlmostEqual(self.converter.convert_mass(1, 'kg', 'g'), 1000)
        self.assertAlmostEqual(self.converter.convert_mass(1000, 'g', 'kg'), 1)
        
        # Imperial conversions
        self.assertAlmostEqual(self.converter.convert_mass(1, 'lb', 'oz'), 16)
        
        # Mixed conversions
        self.assertAlmostEqual(self.converter.convert_mass(1, 'kg', 'lb'), 2.20462, places=5)
    
    def test_temperature_conversions(self):
        """Test temperature unit conversions."""
        # Celsius to Fahrenheit
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'C', 'F'), 32)
        self.assertAlmostEqual(self.converter.convert_temperature(100, 'C', 'F'), 212)
        
        # Fahrenheit to Celsius
        self.assertAlmostEqual(self.converter.convert_temperature(32, 'F', 'C'), 0)
        self.assertAlmostEqual(self.converter.convert_temperature(212, 'F', 'C'), 100)
        
        # Kelvin conversions
        self.assertAlmostEqual(self.converter.convert_temperature(273.15, 'K', 'C'), 0)
        self.assertAlmostEqual(self.converter.convert_temperature(0, 'C', 'K'), 273.15)
    
    def test_pressure_conversions(self):
        """Test pressure unit conversions."""
        # Basic conversions
        self.assertAlmostEqual(self.converter.convert_pressure(1, 'bar', 'Pa'), 100000)
        self.assertAlmostEqual(self.converter.convert_pressure(1, 'atm', 'Pa'), 101325)
        
        # Engineering units
        self.assertAlmostEqual(self.converter.convert_pressure(1, 'bar', 'psi'), 14.5038, places=4)
    
    def test_energy_conversions(self):
        """Test energy unit conversions."""
        # Basic conversions
        self.assertAlmostEqual(self.converter.convert_energy(1, 'kJ', 'J'), 1000)
        self.assertAlmostEqual(self.converter.convert_energy(1, 'kWh', 'J'), 3600000)
        
        # Calories
        self.assertAlmostEqual(self.converter.convert_energy(1, 'kcal', 'J'), 4184)
    
    def test_invalid_units(self):
        """Test handling of invalid units."""
        with self.assertRaises(ValueError):
            self.converter.convert_length(1, 'invalid_unit', 'm')
        
        with self.assertRaises(ValueError):
            self.converter.convert_mass(1, 'kg', 'invalid_unit')
        
        with self.assertRaises(ValueError):
            self.converter.convert_temperature(1, 'invalid_temp', 'C')
    
    def test_get_available_units(self):
        """Test getting available units for each type."""
        length_units = self.converter.get_available_units('length')
        self.assertIn('m', length_units)
        self.assertIn('ft', length_units)
        self.assertIn('km', length_units)
        
        mass_units = self.converter.get_available_units('mass')
        self.assertIn('kg', mass_units)
        self.assertIn('lb', mass_units)
        
        with self.assertRaises(ValueError):
            self.converter.get_available_units('invalid_type')


if __name__ == '__main__':
    unittest.main()