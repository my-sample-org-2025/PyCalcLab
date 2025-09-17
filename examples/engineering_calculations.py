#!/usr/bin/env python3
"""
Engineering calculation examples using PyCalcLab

This script demonstrates practical engineering applications of the PyCalcLab library.
"""

import sys
import os
import math

# Add src to path for import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pycalclab import (
    BasicCalculator,
    TrigonometricCalculator,
    LogarithmicCalculator,
    MatrixCalculator,
    UnitConverter
)


def beam_deflection_calculation():
    """Calculate deflection of a simply supported beam with point load."""
    print("=== Beam Deflection Calculation ===")
    print("Simply supported beam with point load at center")
    
    # Input parameters
    load = 1000  # N (force)
    length = 4.0  # m (beam length)
    E = 200e9  # Pa (Young's modulus for steel)
    I = 8.33e-6  # m^4 (second moment of area)
    
    calc = BasicCalculator()
    
    # Maximum deflection formula: δ = PL³/(48EI)
    deflection = calc.divide(
        calc.multiply(load, calc.power(length, 3)),
        calc.multiply(48, calc.multiply(E, I))
    )
    
    print(f"Load: {load} N")
    print(f"Beam length: {length} m")
    print(f"Young's modulus: {E/1e9:.0f} GPa")
    print(f"Second moment of area: {I*1e6:.2f} cm^4")
    print(f"Maximum deflection: {deflection*1000:.2f} mm")
    print()


def electrical_circuit_analysis():
    """Analyze AC electrical circuit parameters."""
    print("=== AC Electrical Circuit Analysis ===")
    print("RLC circuit impedance calculation")
    
    # Circuit parameters
    R = 50  # Ohms (resistance)
    L = 0.01  # H (inductance)
    C = 100e-6  # F (capacitance)
    f = 60  # Hz (frequency)
    
    calc = BasicCalculator()
    trig = TrigonometricCalculator()
    
    # Angular frequency
    omega = calc.multiply(2 * math.pi, f)
    
    # Reactances
    X_L = calc.multiply(omega, L)  # Inductive reactance
    X_C = calc.divide(1, calc.multiply(omega, C))  # Capacitive reactance
    X = calc.subtract(X_L, X_C)  # Net reactance
    
    # Impedance magnitude
    Z = calc.square_root(calc.add(calc.power(R, 2), calc.power(X, 2)))
    
    # Phase angle
    phase_rad = trig.atan(calc.divide(X, R))
    phase_deg = trig.radians_to_degrees(phase_rad)
    
    print(f"Resistance: {R} Ω")
    print(f"Inductance: {L*1000:.1f} mH")
    print(f"Capacitance: {C*1e6:.0f} μF")
    print(f"Frequency: {f} Hz")
    print(f"Inductive reactance: {X_L:.2f} Ω")
    print(f"Capacitive reactance: {X_C:.2f} Ω")
    print(f"Impedance magnitude: {Z:.2f} Ω")
    print(f"Phase angle: {phase_deg:.2f}°")
    print()


def heat_transfer_calculation():
    """Calculate heat transfer through a wall."""
    print("=== Heat Transfer Calculation ===")
    print("Conductive heat transfer through composite wall")
    
    # Wall parameters
    thickness_1 = 0.1  # m (brick layer)
    thickness_2 = 0.05  # m (insulation layer)
    k_1 = 0.7  # W/m·K (thermal conductivity of brick)
    k_2 = 0.04  # W/m·K (thermal conductivity of insulation)
    area = 20  # m² (wall area)
    T_hot = 30  # °C (indoor temperature)
    T_cold = -10  # °C (outdoor temperature)
    
    calc = BasicCalculator()
    converter = UnitConverter()
    
    # Thermal resistances
    R_1 = calc.divide(thickness_1, k_1)
    R_2 = calc.divide(thickness_2, k_2)
    R_total = calc.add(R_1, R_2)
    
    # Heat transfer rate
    delta_T = calc.subtract(T_hot, T_cold)
    q = calc.divide(calc.multiply(area, delta_T), R_total)
    
    # Convert to different units
    q_btu = converter.convert_power(q, 'W', 'BTU/hr')
    
    print(f"Brick layer thickness: {thickness_1*100:.0f} cm")
    print(f"Insulation layer thickness: {thickness_2*100:.0f} cm")
    print(f"Brick thermal conductivity: {k_1} W/m·K")
    print(f"Insulation thermal conductivity: {k_2} W/m·K")
    print(f"Wall area: {area} m²")
    print(f"Temperature difference: {delta_T}°C")
    print(f"Total thermal resistance: {R_total:.3f} m²·K/W")
    print(f"Heat transfer rate: {q:.1f} W ({q_btu:.1f} BTU/hr)")
    print()


def structural_stress_analysis():
    """Analyze stress in a structural member."""
    print("=== Structural Stress Analysis ===")
    print("Axial stress and safety factor calculation")
    
    # Material and geometry
    force = 50000  # N (applied force)
    diameter = 0.025  # m (rod diameter)
    yield_strength = 250e6  # Pa (yield strength of steel)
    safety_factor_required = 2.5
    
    calc = BasicCalculator()
    converter = UnitConverter()
    
    # Cross-sectional area
    radius = calc.divide(diameter, 2)
    area = calc.multiply(math.pi, calc.power(radius, 2))
    
    # Axial stress
    stress = calc.divide(force, area)
    
    # Safety factor
    safety_factor = calc.divide(yield_strength, stress)
    
    # Convert units for display
    stress_mpa = converter.convert_pressure(stress, 'Pa', 'MPa')
    yield_mpa = converter.convert_pressure(yield_strength, 'Pa', 'MPa')
    force_kn = force / 1000
    
    print(f"Applied force: {force_kn:.1f} kN")
    print(f"Rod diameter: {diameter*1000:.1f} mm")
    print(f"Cross-sectional area: {area*1e6:.2f} mm²")
    print(f"Axial stress: {stress_mpa:.1f} MPa")
    print(f"Yield strength: {yield_mpa:.0f} MPa")
    print(f"Safety factor: {safety_factor:.2f}")
    print(f"Required safety factor: {safety_factor_required}")
    
    if safety_factor >= safety_factor_required:
        print("✓ Design is SAFE")
    else:
        print("✗ Design is UNSAFE - increase cross-section or reduce load")
    print()


def fluid_flow_calculation():
    """Calculate pressure drop in pipe flow."""
    print("=== Fluid Flow Calculation ===")
    print("Pressure drop in circular pipe (Darcy-Weisbach equation)")
    
    # Pipe and fluid parameters
    diameter = 0.1  # m (pipe diameter)
    length = 100  # m (pipe length)
    velocity = 2.0  # m/s (fluid velocity)
    density = 1000  # kg/m³ (water density)
    friction_factor = 0.02  # dimensionless (Darcy friction factor)
    
    calc = BasicCalculator()
    converter = UnitConverter()
    
    # Pressure drop calculation: ΔP = f × (L/D) × (ρv²/2)
    l_over_d = calc.divide(length, diameter)
    velocity_head = calc.divide(calc.multiply(density, calc.power(velocity, 2)), 2)
    pressure_drop = calc.multiply(
        calc.multiply(friction_factor, l_over_d),
        velocity_head
    )
    
    # Convert to different units
    pressure_drop_bar = converter.convert_pressure(pressure_drop, 'Pa', 'bar')
    pressure_drop_psi = converter.convert_pressure(pressure_drop, 'Pa', 'psi')
    
    print(f"Pipe diameter: {diameter*1000:.0f} mm")
    print(f"Pipe length: {length} m")
    print(f"Flow velocity: {velocity} m/s")
    print(f"Fluid density: {density} kg/m³")
    print(f"Friction factor: {friction_factor}")
    print(f"Pressure drop: {pressure_drop:.0f} Pa")
    print(f"Pressure drop: {pressure_drop_bar:.4f} bar")
    print(f"Pressure drop: {pressure_drop_psi:.2f} psi")
    print()


def vibration_analysis():
    """Analyze natural frequency of a cantilever beam."""
    print("=== Vibration Analysis ===")
    print("Natural frequency of cantilever beam")
    
    # Beam properties
    length = 1.0  # m
    width = 0.05  # m
    thickness = 0.01  # m
    E = 200e9  # Pa (Young's modulus)
    density = 7850  # kg/m³ (steel density)
    
    calc = BasicCalculator()
    
    # Cross-sectional properties
    area = calc.multiply(width, thickness)
    I = calc.divide(calc.multiply(width, calc.power(thickness, 3)), 12)
    
    # Mass per unit length
    mass_per_length = calc.multiply(density, area)
    
    # First natural frequency (fundamental mode)
    # f₁ = (λ₁²/2π) × √(EI/μL⁴) where λ₁ = 1.875 for cantilever
    lambda_1 = 1.875
    coefficient = calc.divide(calc.power(lambda_1, 2), 2 * math.pi)
    frequency = calc.multiply(
        coefficient,
        calc.square_root(
            calc.divide(
                calc.multiply(E, I),
                calc.multiply(mass_per_length, calc.power(length, 4))
            )
        )
    )
    
    print(f"Beam length: {length*1000:.0f} mm")
    print(f"Beam width: {width*1000:.0f} mm")
    print(f"Beam thickness: {thickness*1000:.0f} mm")
    print(f"Young's modulus: {E/1e9:.0f} GPa")
    print(f"Density: {density} kg/m³")
    print(f"Second moment of area: {I*1e9:.3f} mm⁴")
    print(f"Mass per unit length: {mass_per_length:.2f} kg/m")
    print(f"First natural frequency: {frequency:.2f} Hz")
    print()


def main():
    """Main function to run all engineering calculations."""
    print("PyCalcLab - Engineering Calculation Examples")
    print("=" * 50)
    print()
    
    beam_deflection_calculation()
    electrical_circuit_analysis()
    heat_transfer_calculation()
    structural_stress_analysis()
    fluid_flow_calculation()
    vibration_analysis()
    
    print("These examples demonstrate practical applications of PyCalcLab")
    print("in various engineering disciplines!")


if __name__ == "__main__":
    main()