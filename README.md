# Refactored Python Demo

## Overview

This repository has been refactored from a single monolithic `main.py` file into a well-organized, modular structure with reusable components and clear separation of concerns.

## Project Structure

```
/
├── README.md                 # This file
├── main_refactored.py       # New main application file
├── main.py                  # Original monolithic file (kept for reference)
└── utils/                   # Utilities package
    ├── __init__.py          # Package initialization
    ├── math_operations.py   # Mathematical functions
    ├── data_structures.py   # Data structure operations
    ├── string_operations.py # String manipulation functions
    ├── file_operations.py   # File handling utilities
    ├── calculator.py        # Calculator class and lambda functions
    ├── decorators.py        # Decorator examples and utilities
    ├── constants.py         # Application constants
    └── control_flow.py      # Control flow demonstrations
```

## Features

### 🔢 Mathematical Operations
- Factorial calculation (with error handling)
- Prime number checking
- Fibonacci sequence generation
- Safe division operations
- Recursive countdown function

### 📝 String Operations
- Greeting functions
- Comprehensive string manipulation
- Person information formatting
- Bytes operations

### 📊 Data Structures
- List operations and comprehensions
- Dictionary operations
- Set operations (union, intersection)
- Tuple unpacking examples
- Generator expressions

### 🧮 Calculator
- Object-oriented Calculator class
- Basic arithmetic operations
- Lambda function examples
- Error handling for division by zero

### 🎭 Decorators
- Simple decorator examples
- Timing decorator
- Retry decorator with configurable attempts
- Function call logging decorator

### 📁 File Operations
- File reading/writing simulation
- Context manager examples
- Proper exception handling

### 🔄 Control Flow
- Loop demonstrations (for, while)
- Conditional statements
- Exception handling patterns
- Random number generation
- Date operations

## Key Improvements

1. **Modularity**: Code is organized into logical modules by functionality
2. **Reusability**: Functions are designed to be reused across different contexts
3. **Documentation**: All functions include comprehensive docstrings
4. **Error Handling**: Proper exception handling with meaningful error messages
5. **Type Hints**: Functions include parameter and return type information
6. **Constants**: Magic numbers and strings moved to a constants module
7. **Testing Ready**: Modular structure makes unit testing straightforward

## Usage

Run the refactored application:

```bash
python3 main_refactored.py
```

## Module Usage Examples

You can also import and use individual modules:

```python
from utils.math_operations import factorial, fibonacci_sequence
from utils.calculator import Calculator
from utils.string_operations import greet

# Use mathematical functions
print(factorial(5))
print(fibonacci_sequence(10))

# Use calculator
calc = Calculator()
print(calc.add(5, 3))

# Use string operations
greet("Alice")
```

## Benefits of Refactoring

- **Maintainability**: Easier to update and maintain individual components
- **Testability**: Each module can be tested independently
- **Readability**: Clear organization makes code easier to understand
- **Scalability**: New features can be added as separate modules
- **Collaboration**: Multiple developers can work on different modules
- **Code Reuse**: Functions can be imported and used in other projects

## Original vs Refactored

- **Original**: 200+ lines in a single file with mixed concerns
- **Refactored**: Organized into 8+ specialized modules with clear responsibilities
- **Functionality**: All original functionality preserved and enhanced
- **Structure**: Professional, maintainable codebase following Python best practices
