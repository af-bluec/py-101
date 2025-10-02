"""
Configuration constants and settings for the py-101 project.

This module contains application-wide constants, configuration values,
and settings that are used throughout the project.
"""

import math
from typing import Dict, Any

# Mathematical constants
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875

# Application metadata
APP_NAME = "Python 101 Demo"
VERSION = "2.0.0"
AUTHOR = "Refactored Code Base"
DESCRIPTION = "A comprehensive Python learning and demonstration toolkit"

# Default values
DEFAULT_FIBONACCI_LENGTH = 10
DEFAULT_PRIME_LIMIT = 100
DEFAULT_RANDOM_RANGE = (1, 100)

# Error messages
ERROR_MESSAGES = {
    'negative_factorial': "Factorial is not defined for negative numbers",
    'negative_sqrt': "Cannot calculate square root of negative number",
    'division_by_zero': "Cannot divide by zero",
    'empty_list': "Cannot process empty list",
    'invalid_input': "Invalid input provided",
    'file_not_found': "File not found",
    'network_error': "Network connection failed",
    'validation_error': "Data validation failed"
}

# Success messages
SUCCESS_MESSAGES = {
    'calculation_complete': "Calculation completed successfully",
    'data_processed': "Data processed successfully",
    'file_saved': "File saved successfully",
    'operation_complete': "Operation completed successfully"
}

# Color codes for terminal output (ANSI)
COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}

# Example data sets for demonstrations
SAMPLE_DATA = {
    'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'fruits': ['apple', 'banana', 'cherry', 'date', 'elderberry'],
    'colors': ['red', 'green', 'blue', 'yellow', 'purple', 'orange'],
    'names': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'temperatures': [23.5, 18.2, 31.7, 14.9, 27.3, 19.8],
    'coordinates': [(0, 0), (1, 2), (3, 4), (5, 6), (7, 8)],
    'mixed_types': [1, 'hello', 3.14, True, None, [1, 2, 3]]
}

# Configuration for examples
EXAMPLE_CONFIG = {
    'basic': {
        'show_types': True,
        'verbose': True,
        'delay': 0.1
    },
    'advanced': {
        'include_timings': True,
        'show_memory_usage': False,
        'detailed_output': True
    },
    'error_handling': {
        'log_errors': True,
        'show_traceback': True,
        'retry_attempts': 3
    }
}

# File paths and directories
PATHS = {
    'src': 'src',
    'examples': 'examples',
    'utils': 'utils',
    'logs': 'logs',
    'temp': 'temp',
    'output': 'output'
}

# Limits and constraints
LIMITS = {
    'max_factorial': 1000,
    'max_fibonacci_length': 100,
    'max_prime_limit': 10000,
    'max_list_size': 1000000,
    'max_string_length': 10000,
    'max_retry_attempts': 5,
    'timeout_seconds': 30
}

# Regular expressions
PATTERNS = {
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'phone': r'^\+?1?-?\.?\s?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$',
    'url': r'^https?://[^\s/$.?#].[^\s]*$',
    'integer': r'^-?\d+$',
    'float': r'^-?\d*\.?\d+$',
    'word': r'^\w+$'
}

# Feature flags
FEATURES = {
    'enable_logging': True,
    'enable_caching': True,
    'enable_profiling': False,
    'enable_debug': False,
    'enable_colors': True,
    'enable_sound': False
}

# Database configuration (simulated)
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'name': 'py101_demo',
    'user': 'demo_user',
    'password': 'demo_password',
    'timeout': 30,
    'pool_size': 10
}

# API configuration (simulated)
API_CONFIG = {
    'base_url': 'https://api.example.com',
    'version': 'v1',
    'timeout': 10,
    'max_retries': 3,
    'rate_limit': 100  # requests per minute
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'py101.log',
    'max_size': '10MB',
    'backup_count': 5
}

# Performance thresholds
PERFORMANCE = {
    'slow_function_threshold': 1.0,  # seconds
    'memory_warning_threshold': 100,  # MB
    'cpu_warning_threshold': 80,  # percent
    'cache_size_limit': 1000  # items
}

# Testing configuration
TEST_CONFIG = {
    'run_slow_tests': False,
    'mock_external_services': True,
    'test_data_size': 100,
    'random_seed': 42
}


def get_config(section: str) -> Dict[str, Any]:
    """
    Get configuration for a specific section.
    
    Args:
        section: Configuration section name
        
    Returns:
        Configuration dictionary for the section
        
    Raises:
        KeyError: If section doesn't exist
    """
    configs = {
        'example': EXAMPLE_CONFIG,
        'paths': PATHS,
        'limits': LIMITS,
        'features': FEATURES,
        'database': DATABASE_CONFIG,
        'api': API_CONFIG,
        'logging': LOGGING_CONFIG,
        'performance': PERFORMANCE,
        'test': TEST_CONFIG
    }
    
    if section not in configs:
        raise KeyError(f"Configuration section '{section}' not found")
    
    return configs[section]


def is_feature_enabled(feature: str) -> bool:
    """
    Check if a feature is enabled.
    
    Args:
        feature: Feature name
        
    Returns:
        True if feature is enabled, False otherwise
    """
    return FEATURES.get(feature, False)


def get_color_code(color: str) -> str:
    """
    Get ANSI color code for terminal output.
    
    Args:
        color: Color name
        
    Returns:
        ANSI color code string
    """
    return COLORS.get(color, COLORS['reset'])


def format_colored_text(text: str, color: str) -> str:
    """
    Format text with color for terminal output.
    
    Args:
        text: Text to color
        color: Color name
        
    Returns:
        Formatted text with color codes
    """
    if not is_feature_enabled('enable_colors'):
        return text
    
    color_code = get_color_code(color)
    reset_code = get_color_code('reset')
    return f"{color_code}{text}{reset_code}"


# Export commonly used items
__all__ = [
    'PI', 'E', 'GOLDEN_RATIO',
    'APP_NAME', 'VERSION', 'AUTHOR', 'DESCRIPTION',
    'ERROR_MESSAGES', 'SUCCESS_MESSAGES',
    'SAMPLE_DATA', 'EXAMPLE_CONFIG',
    'get_config', 'is_feature_enabled',
    'get_color_code', 'format_colored_text'
]
