"""
Provides functions that help with creating a mathematically accurate model of a rocket flight.
"""

from numpy import float64

def burnout_time(propellant_mass: float64, mass_flow: float64) -> float64:
    """
    Calculates the time until the rocket's propellant is exhausted.
    :param propellant_mass:
    :param mass_flow:
    :return: Time in seconds until the rocket's propellant is exhausted.
    """

    return propellant_mass / mass_flow