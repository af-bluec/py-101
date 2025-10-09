# Development Guide

## Python 101 - Developer's Guide

This guide provides detailed information for developers who want to contribute to or extend the Python 101 project.

---

## Table of Contents
- [Development Environment Setup](#development-environment-setup)
- [Project Architecture](#project-architecture)
- [Coding Standards](#coding-standards)
- [Development Workflow](#development-workflow)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Standards](#documentation-standards)
- [Performance Considerations](#performance-considerations)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)

---

## Development Environment Setup

### Prerequisites

**Required:**
- Python 3.6 or higher
- Git for version control
- Text editor or IDE

**Recommended:**
- Python 3.8+ for best performance
- VS Code with Python extension
- GitHub CLI for easier collaboration

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/py-101.git
cd py-101

# Verify Python installation
python --version

# Test the project
python main.py

# Run tests
python tests/test_functions.py
```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv py101_dev

# Activate virtual environment
# Windows:
py101_dev\Scripts\activate

# macOS/Linux:
source py101_dev/bin/activate

# Verify activation
which python

# Deactivate when done
deactivate
```

### IDE Configuration

#### Visual Studio Code

Create `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./py101_dev/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

#### PyCharm

1. Open project folder
2. Configure Python interpreter: File → Settings → Project → Python Interpreter
3. Enable code style checks: File → Settings → Editor → Code Style → Python
4. Configure test runner: File → Settings → Tools → Python Integrated Tools

---

## Project Architecture

### Directory Structure

```
py-101/
├── main.py                     # Entry point and core demonstrations
├── utils/                      # Utility modules
│   ├── __init__.py            # Package initialization  
│   ├── string_utils.py        # String manipulation functions
│   ├── math_utils.py          # Mathematical operations
│   ├── data_structures.py     # Data structure helpers
│   ├── file_utils.py          # File I/O operations
│   └── validators.py          # Input validation
├── examples/                   # Usage examples
│   ├── string_examples.py     # String utility examples
│   ├── math_examples.py       # Math utility examples
│   └── data_examples.py       # Data structure examples
├── tests/                      # Test files
│   └── test_functions.py      # Main test suite
├── docs/                       # Documentation
│   ├── API.md                 # API documentation
│   ├── EXAMPLES.md            # Usage examples
│   ├── INSTALLATION.md        # Installation guide
│   ├── CONTRIBUTING.md        # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md     # Community standards
│   ├── CHANGELOG.md           # Version history
│   └── DEVELOPMENT.md         # This file
├── README.md                   # Project overview
├── LICENSE                     # MIT license
└── requirements.txt           # Dependencies (currently none)
```

### Module Design Principles

#### Single Responsibility
Each module has a focused purpose:
- `string_utils.py` - String manipulation only
- `math_utils.py` - Mathematical operations only
- `data_structures.py` - Data structure helpers only

#### Functional Programming Style
```python
# Pure functions - no side effects
def clean_text(text: str) -> str:
    """Clean text without modifying input."""
    return text.strip()

# Avoid global state
# Functions should be predictable and testable
```

#### Error Handling Strategy
```python
def safe_function(input_value):
    """Function with comprehensive error handling."""
    # Input validation
    if not isinstance(input_value, int):
        raise TypeError("Expected integer input")
    
    if input_value < 0:
        raise ValueError("Input must be non-negative")
    
    try:
        # Main logic here
        result = process_input(input_value)
        return result
    except Exception as e:
        # Log error for debugging
        print(f"Unexpected error in safe_function: {e}")
        raise
```

---

## Coding Standards

### Python Style Guide (PEP 8)

#### Naming Conventions
```python
# Functions and variables: snake_case
def calculate_factorial(number):
    result_value = 1
    return result_value

# Constants: UPPER_CASE  
MAX_ITERATIONS = 1000
DEFAULT_THRESHOLD = 0.5

# Classes: PascalCase (when needed)
class DataProcessor:
    def __init__(self):
        pass

# Private functions: _leading_underscore
def _internal_helper():
    pass
```

#### Function Structure
```python
def example_function(param1: int, param2: str = "default") -> bool:
    """
    Brief description of what the function does.
    
    Longer description if needed, explaining the purpose,
    algorithm, or important details.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter with default
        
    Returns:
        Description of return value
        
    Raises:
        TypeError: When param1 is not an integer
        ValueError: When param1 is negative
        
    Example:
        >>> example_function(5, "test")
        True
    """
    # Input validation
    if not isinstance(param1, int):
        raise TypeError("param1 must be an integer")
    
    if param1 < 0:
        raise ValueError("param1 must be non-negative")
    
    # Main logic with clear variable names
    processed_value = param1 * 2
    condition_met = processed_value > len(param2)
    
    return condition_met
```

#### Import Organization
```python
# Standard library imports first
import os
import sys
from typing import List, Optional, Dict, Any

# Third-party imports (none currently in this project)
# import requests
# import numpy as np

# Local imports last
from .string_utils import clean_text
from .math_utils import gcd
```

### Type Hints

Use type hints for better code clarity:
```python
from typing import List, Dict, Optional, Union, Tuple

def process_data(
    items: List[int], 
    config: Dict[str, Any], 
    threshold: Optional[float] = None
) -> Tuple[List[int], bool]:
    """Process data with type hints."""
    # Implementation here
    pass

# For complex types
DataPoint = Dict[str, Union[int, str, float]]
ProcessingResult = Tuple[List[DataPoint], Dict[str, int]]
```

### Docstring Standards

#### Function Docstrings
```python
def fibonacci_sequence(length: int) -> List[int]:
    """
    Generate a Fibonacci sequence of specified length.
    
    This function creates a list containing the first 'length' numbers
    in the Fibonacci sequence, starting with 0 and 1.
    
    Args:
        length: Number of Fibonacci numbers to generate.
                Must be a non-negative integer.
    
    Returns:
        A list containing the first 'length' Fibonacci numbers.
        Returns empty list if length is 0.
    
    Raises:
        TypeError: If length is not an integer.
        ValueError: If length is negative.
    
    Example:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        
        >>> fibonacci_sequence(0)
        []
    
    Note:
        Time complexity: O(n)
        Space complexity: O(n)
    """
    # Implementation here
```

#### Module Docstrings
```python
"""
String manipulation utilities for the Python 101 project.

This module provides functions for common string operations including
text cleaning, palindrome detection, and word manipulation. All functions
are designed to be educational and demonstrate Python string handling
best practices.

Functions:
    clean_text: Remove extra whitespace
    is_palindrome: Check if text reads same forwards/backwards  
    count_words: Count words in text
    capitalize_words: Capitalize each word
    reverse_words: Reverse word order

Example:
    from utils.string_utils import clean_text, is_palindrome
    
    text = "  hello world  "
    clean = clean_text(text)  # "hello world"
    is_palin = is_palindrome("racecar")  # True
"""
```

---

## Development Workflow

### Feature Development Process

#### 1. Planning Phase
```bash
# Create issue for feature/bug
# Discuss implementation approach
# Plan API design and tests

# Example feature: Add text similarity function
# API design:
def text_similarity(text1: str, text2: str) -> float:
    """Calculate similarity between two texts (0.0 to 1.0)"""
```

#### 2. Implementation Phase
```bash
# Create feature branch
git checkout -b feature/text-similarity

# Implement function with tests
# utils/string_utils.py - add function
# tests/test_functions.py - add tests
# examples/string_examples.py - add example

# Test implementation
python tests/test_functions.py
python examples/string_examples.py
```

#### 3. Documentation Phase
```bash
# Update documentation
# docs/API.md - add function details
# docs/EXAMPLES.md - add usage examples
# README.md - update function table if needed
```

#### 4. Review and Merge
```bash
# Commit changes
git add .
git commit -m "Add text similarity function

- Implement text_similarity() using character frequency
- Add comprehensive tests for edge cases  
- Include usage examples and documentation
- Maintain O(n) time complexity"

# Push and create pull request
git push origin feature/text-similarity
```

### Debugging Workflow

#### Print Debugging
```python
def debug_function(data):
    print(f"DEBUG: Input data type: {type(data)}")
    print(f"DEBUG: Input data value: {data}")
    
    processed = process_data(data)
    print(f"DEBUG: Processed result: {processed}")
    
    return processed
```

#### Using Python Debugger
```python
import pdb

def complex_function(data):
    # Set breakpoint
    pdb.set_trace()
    
    # Process data
    result = []
    for item in data:
        processed = item * 2  # Examine variables here
        result.append(processed)
    
    return result

# Run with: python -m pdb script.py
```

#### Logging for Development
```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

def logged_function(data):
    logging.info(f"Processing {len(data)} items")
    
    results = []
    for i, item in enumerate(data):
        logging.debug(f"Processing item {i}: {item}")
        result = process_item(item)
        results.append(result)
    
    logging.info(f"Completed processing, got {len(results)} results")
    return results
```

---

## Testing Guidelines

### Test Structure

#### Organize Tests by Module
```python
# tests/test_string_utils.py

import unittest
from utils.string_utils import clean_text, is_palindrome, count_words

class TestStringUtils(unittest.TestCase):
    """Test cases for string utility functions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.sample_texts = [
            "  hello world  ",
            "Python is awesome!",
            "",
            "   "
        ]
    
    def test_clean_text_normal_cases(self):
        """Test clean_text with normal inputs."""
        # Test basic cleaning
        result = clean_text("  hello world  ")
        self.assertEqual(result, "hello world")
        
        # Test multiple spaces
        result = clean_text("hello    world")
        self.assertEqual(result, "hello world")
    
    def test_clean_text_edge_cases(self):
        """Test clean_text with edge cases."""
        # Empty string
        self.assertEqual(clean_text(""), "")
        
        # Only whitespace
        self.assertEqual(clean_text("   "), "")
        
        # No cleaning needed
        self.assertEqual(clean_text("hello"), "hello")
    
    def test_clean_text_error_cases(self):
        """Test clean_text error handling."""
        # Non-string input
        with self.assertRaises(TypeError):
            clean_text(123)
        
        with self.assertRaises(TypeError):
            clean_text(None)

if __name__ == '__main__':
    unittest.main()
```

#### Test Categories

**1. Unit Tests - Individual Functions**
```python
def test_factorial_valid_inputs(self):
    """Test factorial with valid inputs."""
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(1), 1)  
    self.assertEqual(factorial(5), 120)
    self.assertEqual(factorial(10), 3628800)

def test_factorial_invalid_inputs(self):
    """Test factorial error handling."""
    with self.assertRaises(ValueError):
        factorial(-1)
    
    with self.assertRaises(TypeError):
        factorial(3.14)
    
    with self.assertRaises(TypeError):
        factorial("5")
```

**2. Integration Tests - Function Combinations**
```python
def test_text_processing_pipeline(self):
    """Test combination of string functions."""
    # Raw input
    text = "  Hello World Python  "
    
    # Processing pipeline
    cleaned = clean_text(text)
    word_count = count_words(cleaned)
    is_palin = is_palindrome(cleaned)
    
    # Verify results
    self.assertEqual(cleaned, "Hello World Python")
    self.assertEqual(word_count, 3)
    self.assertFalse(is_palin)
```

**3. Performance Tests**
```python
import time

def test_prime_generation_performance(self):
    """Test prime generation performance."""
    start_time = time.time()
    primes = generate_primes(1000)
    end_time = time.time()
    
    # Should complete in reasonable time
    self.assertLess(end_time - start_time, 1.0)
    
    # Should find correct number of primes
    self.assertEqual(len(primes), 168)  # Known: 168 primes < 1000
```

### Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python tests/test_string_utils.py

# Run with verbose output
python -m unittest -v

# Run specific test method
python -m unittest tests.test_string_utils.TestStringUtils.test_clean_text
```

---

## Documentation Standards

### Code Documentation

#### Inline Comments
```python
def complex_algorithm(data):
    """Complex algorithm with step-by-step comments."""
    # Step 1: Validate and prepare data
    if not data:
        return []
    
    # Step 2: Initialize tracking variables  
    processed_items = []
    current_sum = 0
    
    # Step 3: Process each item
    for i, item in enumerate(data):
        # Apply transformation based on position
        if i % 2 == 0:
            # Even positions get doubled
            transformed = item * 2
        else:
            # Odd positions get squared
            transformed = item ** 2
        
        # Track cumulative sum for statistics
        current_sum += transformed
        processed_items.append(transformed)
    
    # Step 4: Return processed data
    return processed_items
```

#### Algorithm Documentation
```python
def sieve_of_eratosthenes(limit):
    """
    Generate prime numbers using Sieve of Eratosthenes algorithm.
    
    Algorithm:
    1. Create boolean array "prime[0..limit]" and initialize all as true
    2. Start with smallest prime p = 2
    3. Mark all multiples of p (except p itself) as not prime
    4. Find next number greater than p in array that is not marked
    5. Repeat steps 3-4 until p² > limit
    6. All numbers still marked as prime are prime numbers
    
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    
    Args:
        limit: Upper bound for prime generation
        
    Returns:
        List of prime numbers up to limit
    """
    # Implementation with step comments
```

### API Documentation

#### Function Reference Format
```markdown
### function_name(param1, param2=default)

Brief description of what the function does.

**Parameters:**
- `param1` (type): Description of parameter
- `param2` (type, optional): Description with default value

**Returns:**
- `return_type`: Description of return value

**Raises:**
- `ExceptionType`: When this exception occurs

**Example:**
```python
result = function_name(arg1, arg2)
print(result)  # Expected output
```

**Time Complexity:** O(notation)
**Space Complexity:** O(notation)
```

---

## Performance Considerations

### Optimization Guidelines

#### Choose Appropriate Data Structures
```python
# For membership testing - use sets
def find_common_elements(list1, list2):
    """Find common elements efficiently."""
    # Convert to set for O(1) lookup
    set1 = set(list1)
    return [item for item in list2 if item in set1]

# For counting - use Counter
from collections import Counter

def count_frequency(items):
    """Count item frequency efficiently."""
    return Counter(items)
```

#### Avoid Common Performance Pitfalls
```python
# BAD: String concatenation in loop
def build_string_bad(items):
    result = ""
    for item in items:
        result += str(item) + " "  # Creates new string each time
    return result

# GOOD: Use join for string building
def build_string_good(items):
    return " ".join(str(item) for item in items)

# BAD: Repeated list operations
def process_list_bad(items):
    result = []
    for item in items:
        if item > 0:
            result.append(item * 2)  # Multiple list operations
    return result

# GOOD: List comprehension
def process_list_good(items):
    return [item * 2 for item in items if item > 0]
```

#### Memory Management
```python
def process_large_data(filename):
    """Process large file efficiently."""
    # BAD: Load entire file into memory
    # with open(filename) as f:
    #     data = f.read()
    #     return process_all(data)
    
    # GOOD: Process line by line
    results = []
    with open(filename) as f:
        for line in f:  # Generator - memory efficient
            processed = process_line(line.strip())
            if processed:  # Only keep what we need
                results.append(processed)
    
    return results
```

### Performance Testing

#### Timing Functions
```python
import time
from functools import wraps

def timing_decorator(func):
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function(n):
    """Function to test performance."""
    return sum(i**2 for i in range(n))
```

#### Benchmarking
```python
def benchmark_algorithms():
    """Compare algorithm performance."""
    import timeit
    
    # Test data
    data = list(range(1000))
    
    # Test different approaches
    approach1_time = timeit.timeit(
        lambda: approach1(data), 
        number=1000
    )
    
    approach2_time = timeit.timeit(
        lambda: approach2(data),
        number=1000  
    )
    
    print(f"Approach 1: {approach1_time:.4f} seconds")
    print(f"Approach 2: {approach2_time:.4f} seconds")
    print(f"Speedup: {approach1_time/approach2_time:.2f}x")
```

---

## Debugging and Troubleshooting

### Common Issues and Solutions

#### Import Errors
```python
# Problem: ModuleNotFoundError: No module named 'utils'
# Solution: Ensure you're in the correct directory

# Check current directory
import os
print(os.getcwd())

# Add project root to path if needed
import sys
sys.path.insert(0, '/path/to/py-101')

# Or use relative imports properly
from .utils.string_utils import clean_text
```

#### Type Errors
```python
# Problem: Function expects int but gets string
def debug_type_issues(value):
    """Debug type-related issues."""
    print(f"Type: {type(value)}")
    print(f"Value: {repr(value)}")
    
    # Type checking
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            print(f"Cannot convert '{value}' to int")
            return None
    
    return value

# Usage
result = debug_type_issues("123")  # Debug output helps identify issue
```

#### Logic Errors
```python
def debug_logic_with_assertions(data):
    """Use assertions to catch logic errors."""
    # Pre-conditions
    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert len(data) > 0, "Data cannot be empty"
    
    # Process data
    result = []
    for item in data:
        processed = item * 2
        result.append(processed)
    
    # Post-conditions  
    assert len(result) == len(data), "Result length mismatch"
    assert all(r == d * 2 for r, d in zip(result, data)), "Processing error"
    
    return result
```

### Debugging Tools

#### Built-in Debugger
```python
import pdb

def function_to_debug(data):
    pdb.set_trace()  # Debugger will stop here
    
    # Commands in debugger:
    # n - next line
    # s - step into function
    # c - continue
    # l - list current code
    # p variable_name - print variable
    # pp variable_name - pretty print
    # h - help
    
    result = process_data(data)
    return result
```

#### Logging for Production Debugging
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def production_function(data):
    """Function with production-ready logging."""
    logger.info(f"Processing {len(data)} items")
    
    try:
        results = []
        for i, item in enumerate(data):
            logger.debug(f"Processing item {i}: {item}")
            
            result = complex_processing(item)
            results.append(result)
            
            if i % 100 == 0:  # Progress logging
                logger.info(f"Processed {i+1}/{len(data)} items")
        
        logger.info("Processing completed successfully")
        return results
        
    except Exception as e:
        logger.error(f"Error during processing: {e}", exc_info=True)
        raise
```

---

## Advanced Development Topics

### Design Patterns

#### Factory Pattern for Function Creation
```python
def create_validator(validation_type):
    """Factory function for creating validators."""
    validators = {
        'email': validate_email,
        'phone': validate_phone,  
        'positive_int': is_positive_integer
    }
    
    if validation_type not in validators:
        raise ValueError(f"Unknown validation type: {validation_type}")
    
    return validators[validation_type]

# Usage
email_validator = create_validator('email')
is_valid = email_validator("user@example.com")
```

#### Decorator Pattern
```python
def memoize(func):
    """Decorator to add memoization to expensive functions."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    
    wrapper.cache_clear = cache.clear
    return wrapper

@memoize  
def expensive_fibonacci(n):
    """Fibonacci with memoization."""
    if n < 2:
        return n
    return expensive_fibonacci(n-1) + expensive_fibonacci(n-2)
```

### Extension Points

#### Adding New Utility Modules
```python
# utils/new_module.py

"""
New utility module template.

Description of module purpose and functions.
"""

def new_function(param):
    """
    Template for new function.
    
    Args:
        param: Parameter description
        
    Returns:
        Return value description
    """
    # Implementation
    pass

# Update utils/__init__.py
from . import new_module
```

#### Plugin Architecture
```python
# Plugin system for extending functionality
class PluginManager:
    """Simple plugin manager."""
    
    def __init__(self):
        self.plugins = {}
    
    def register(self, name, plugin_func):
        """Register a new plugin function."""
        self.plugins[name] = plugin_func
    
    def execute(self, name, *args, **kwargs):
        """Execute a registered plugin."""
        if name not in self.plugins:
            raise ValueError(f"Plugin '{name}' not found")
        
        return self.plugins[name](*args, **kwargs)

# Usage
plugin_manager = PluginManager()
plugin_manager.register('custom_string_op', custom_function)
result = plugin_manager.execute('custom_string_op', "test")
```

---

This development guide provides a comprehensive foundation for contributing to and extending the Python 101 project. Follow these guidelines to maintain code quality and ensure a consistent development experience.

**Happy Developing! 🐍⚡**
