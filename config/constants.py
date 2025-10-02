"""
Configuration constants and application settings.
"""

# Mathematical constants
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875

# Application settings
APP_NAME = "Python Demo Application"
VERSION = "2.0.0"
AUTHOR = "Refactored Code Team"

# Default values
DEFAULT_FIBONACCI_LENGTH = 10
DEFAULT_PRIME_LIMIT = 100
DEFAULT_RANDOM_RANGE = (1, 100)
DEFAULT_BATCH_SIZE = 5

# String constants
GREETING_TEMPLATE = "Hello, {}!"
WELCOME_MESSAGE = "Welcome to this Python demo script!"
COMPLETION_MESSAGE = "Script execution completed."

# Error messages
ERROR_NEGATIVE_FACTORIAL = "Factorial is not defined for negative numbers"
ERROR_DIVISION_BY_ZERO = "Division by zero is not allowed"
ERROR_NEGATIVE_SQRT = "Cannot calculate square root of negative number"
ERROR_INVALID_PRIME = "Number must be positive for prime checking"

# Display settings
SEPARATOR = "=" * 50
SUBSEPARATOR = "-" * 30

# File extensions and patterns
PYTHON_EXTENSIONS = ['.py', '.pyw']
TEXT_EXTENSIONS = ['.txt', '.md', '.rst']

# Color codes for console output (ANSI)
class Colors:
    """ANSI color codes for console output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

# Configuration for demonstrations
DEMO_CONFIG = {
    'show_timing': True,
    'show_memory_usage': False,
    'verbose_output': True,
    'colored_output': True,
    'max_display_items': 20
}

# Data structure limits
MAX_LIST_SIZE = 1000
MAX_DICT_SIZE = 100
MAX_SET_SIZE = 100

# Numerical limits
MAX_FACTORIAL_INPUT = 100
MAX_FIBONACCI_LENGTH = 1000
MAX_PRIME_LIMIT = 10000

# Default test data
SAMPLE_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
SAMPLE_NUMBERS = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55]
SAMPLE_WORDS = ["python", "programming", "refactoring", "modularity", "reusability"]

# Environment settings
DEVELOPMENT_MODE = True
DEBUG_MODE = False
LOG_LEVEL = "INFO"
