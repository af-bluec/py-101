"""
Package initialization file for the utils module.

This file makes the utils directory a Python package and provides
convenient imports for all utility modules.
"""

# Import all modules for easy access
from . import math_operations
from . import data_structures  
from . import string_operations
from . import file_operations
from . import calculator
from . import decorators
from . import constants
from . import control_flow

# Version information
__version__ = "1.0.0"
__author__ = "Refactored Python Demo"

# Convenience imports for commonly used functions
from .math_operations import factorial, is_prime, fibonacci_sequence
from .string_operations import greet, demonstrate_string_operations
from .calculator import Calculator
from .constants import PI, E, GOLDEN_RATIO

__all__ = [
    'math_operations',
    'data_structures',
    'string_operations', 
    'file_operations',
    'calculator',
    'decorators',
    'constants',
    'control_flow',
    'factorial',
    'is_prime',
    'fibonacci_sequence',
    'greet',
    'demonstrate_string_operations',
    'Calculator',
    'PI',
    'E',
    'GOLDEN_RATIO'
]
