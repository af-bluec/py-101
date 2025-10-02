"""
py101 - A Python educational package demonstrating basic concepts.

This package provides modules for mathematical operations, calculations,
utility functions, and Python feature demonstrations.
"""

__version__ = "1.0.0"
__author__ = "py101 Project"
__email__ = "example@example.com"

# Import main classes and functions for easy access
from .math_ops import factorial, is_prime, fibonacci_sequence
from .calculator import Calculator
from .utils import greet, generate_random_number, string_operations
from .demos import PythonFeatureDemo

__all__ = [
    'factorial',
    'is_prime', 
    'fibonacci_sequence',
    'Calculator',
    'greet',
    'generate_random_number',
    'string_operations',
    'PythonFeatureDemo'
]
