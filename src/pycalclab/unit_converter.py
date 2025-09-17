"""
Unit conversion utilities for PyCalcLab

This module provides comprehensive unit conversions for various physical quantities
commonly used in engineering and scientific calculations.
"""

from typing import Dict, Union

Number = Union[int, float]


class UnitConverter:
    """Comprehensive unit converter for engineering calculations."""
    
    # Conversion factors to base units
    LENGTH_CONVERSIONS = {
        # Base unit: meter (m)
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'mil': 0.0000254,
        'μm': 0.000001,
        'nm': 0.000000001,
    }
    
    MASS_CONVERSIONS = {
        # Base unit: kilogram (kg)
        'mg': 0.000001,
        'g': 0.001,
        'kg': 1.0,
        'ton': 1000.0,
        'oz': 0.0283495,
        'lb': 0.453592,
        'stone': 6.35029,
    }
    
    TIME_CONVERSIONS = {
        # Base unit: second (s)
        'ns': 0.000000001,
        'μs': 0.000001,
        'ms': 0.001,
        's': 1.0,
        'min': 60.0,
        'hr': 3600.0,
        'day': 86400.0,
        'week': 604800.0,
        'year': 31557600.0,  # 365.25 days
    }
    
    TEMPERATURE_CONVERSIONS = {
        # Special handling required for temperature
        'K': 'kelvin',
        'C': 'celsius',
        'F': 'fahrenheit',
        'R': 'rankine',
    }
    
    AREA_CONVERSIONS = {
        # Base unit: square meter (m²)
        'mm2': 0.000001,
        'cm2': 0.0001,
        'm2': 1.0,
        'km2': 1000000.0,
        'in2': 0.00064516,
        'ft2': 0.092903,
        'yd2': 0.836127,
        'acre': 4046.86,
        'ha': 10000.0,  # hectare
    }
    
    VOLUME_CONVERSIONS = {
        # Base unit: cubic meter (m³)
        'mm3': 0.000000001,
        'cm3': 0.000001,
        'm3': 1.0,
        'L': 0.001,  # liter
        'mL': 0.000001,
        'in3': 0.0000163871,
        'ft3': 0.0283168,
        'gal': 0.00378541,  # US gallon
        'qt': 0.000946353,  # US quart
        'pt': 0.000473176,  # US pint
        'cup': 0.000236588,
        'fl_oz': 0.0000295735,  # US fluid ounce
    }
    
    FORCE_CONVERSIONS = {
        # Base unit: Newton (N)
        'N': 1.0,
        'kN': 1000.0,
        'dyne': 0.00001,
        'lbf': 4.44822,  # pound-force
        'kgf': 9.80665,  # kilogram-force
    }
    
    PRESSURE_CONVERSIONS = {
        # Base unit: Pascal (Pa)
        'Pa': 1.0,
        'kPa': 1000.0,
        'MPa': 1000000.0,
        'bar': 100000.0,
        'atm': 101325.0,
        'psi': 6894.76,
        'torr': 133.322,
        'mmHg': 133.322,
    }
    
    ENERGY_CONVERSIONS = {
        # Base unit: Joule (J)
        'J': 1.0,
        'kJ': 1000.0,
        'MJ': 1000000.0,
        'cal': 4.184,  # thermochemical calorie
        'kcal': 4184.0,
        'Wh': 3600.0,  # watt-hour
        'kWh': 3600000.0,
        'BTU': 1055.06,
        'ft_lb': 1.35582,  # foot-pound
    }
    
    POWER_CONVERSIONS = {
        # Base unit: Watt (W)
        'W': 1.0,
        'kW': 1000.0,
        'MW': 1000000.0,
        'hp': 745.7,  # mechanical horsepower
        'BTU/hr': 0.293071,
    }
    
    @staticmethod
    def convert_length(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between length units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.LENGTH_CONVERSIONS)
    
    @staticmethod
    def convert_mass(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between mass units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.MASS_CONVERSIONS)
    
    @staticmethod
    def convert_time(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between time units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.TIME_CONVERSIONS)
    
    @staticmethod
    def convert_area(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between area units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.AREA_CONVERSIONS)
    
    @staticmethod
    def convert_volume(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between volume units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.VOLUME_CONVERSIONS)
    
    @staticmethod
    def convert_force(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between force units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.FORCE_CONVERSIONS)
    
    @staticmethod
    def convert_pressure(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between pressure units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.PRESSURE_CONVERSIONS)
    
    @staticmethod
    def convert_energy(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between energy units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.ENERGY_CONVERSIONS)
    
    @staticmethod
    def convert_power(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between power units."""
        return UnitConverter._convert_linear(value, from_unit, to_unit, UnitConverter.POWER_CONVERSIONS)
    
    @staticmethod
    def convert_temperature(value: Number, from_unit: str, to_unit: str) -> float:
        """Convert between temperature units."""
        # Convert from source to Kelvin first
        if from_unit == 'K':
            kelvin_value = value
        elif from_unit == 'C':
            kelvin_value = value + 273.15
        elif from_unit == 'F':
            kelvin_value = (value - 32) * 5/9 + 273.15
        elif from_unit == 'R':
            kelvin_value = value * 5/9
        else:
            raise ValueError(f"Unknown temperature unit: {from_unit}")
        
        # Convert from Kelvin to target unit
        if to_unit == 'K':
            return kelvin_value
        elif to_unit == 'C':
            return kelvin_value - 273.15
        elif to_unit == 'F':
            return (kelvin_value - 273.15) * 9/5 + 32
        elif to_unit == 'R':
            return kelvin_value * 9/5
        else:
            raise ValueError(f"Unknown temperature unit: {to_unit}")
    
    @staticmethod
    def _convert_linear(value: Number, from_unit: str, to_unit: str, conversion_dict: Dict[str, float]) -> float:
        """Generic linear conversion using conversion factors."""
        if from_unit not in conversion_dict:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in conversion_dict:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        # Convert to base unit, then to target unit
        base_value = value * conversion_dict[from_unit]
        return base_value / conversion_dict[to_unit]
    
    @staticmethod
    def get_available_units(unit_type: str) -> list:
        """Get list of available units for a given type."""
        unit_mappings = {
            'length': UnitConverter.LENGTH_CONVERSIONS,
            'mass': UnitConverter.MASS_CONVERSIONS,
            'time': UnitConverter.TIME_CONVERSIONS,
            'area': UnitConverter.AREA_CONVERSIONS,
            'volume': UnitConverter.VOLUME_CONVERSIONS,
            'force': UnitConverter.FORCE_CONVERSIONS,
            'pressure': UnitConverter.PRESSURE_CONVERSIONS,
            'energy': UnitConverter.ENERGY_CONVERSIONS,
            'power': UnitConverter.POWER_CONVERSIONS,
            'temperature': UnitConverter.TEMPERATURE_CONVERSIONS,
        }
        
        if unit_type not in unit_mappings:
            raise ValueError(f"Unknown unit type: {unit_type}")
        
        return list(unit_mappings[unit_type].keys())