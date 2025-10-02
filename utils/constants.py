"""
Constants module.

This module contains various constants used throughout the application.
"""

import math

# Mathematical constants
PI = 3.14159
E = 2.71828
GOLDEN_RATIO = 1.618

# More precise mathematical constants
PRECISE_PI = math.pi
PRECISE_E = math.e

# Application constants
DEFAULT_FIBONACCI_LENGTH = 10
DEFAULT_COUNTDOWN_START = 3
MAX_FACTORIAL_INPUT = 1000

# String constants
DEFAULT_GREETING_NAME = "World"
SAMPLE_TEXT = "Python is fun!"

# Numeric constants
DEFAULT_RANDOM_MIN = 1
DEFAULT_RANDOM_MAX = 100

# Error messages
ERROR_NEGATIVE_FACTORIAL = "Factorial is not defined for negative numbers"
ERROR_DIVISION_BY_ZERO = "Division by zero"
ERROR_INVALID_LENGTH = "Length must be at least 1"

# Status messages
SUCCESS_MESSAGE = "Operation completed successfully"
CLEANUP_MESSAGE = "Cleanup done"
SCRIPT_COMPLETION_MESSAGE = "Script execution completed."

# File simulation constants
DEFAULT_FILENAME = "sample.txt"
SAMPLE_FILE_CONTENT = "This is sample content."
NONEXISTENT_FILE = "nonexistent.txt"

# Data structure examples
SAMPLE_PERSON = {"name": "Alice", "age": 30}
SAMPLE_SCORES = {"math": 95, "science": 88}
SAMPLE_FRUITS = ["apple", "banana", "cherry"]
SAMPLE_POINT = (10, 20)
