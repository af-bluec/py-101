# Python 101 - Comprehensive Learning Toolkit

A well-structured, modular Python learning and demonstration project that showcases fundamental to advanced Python programming concepts.

## 🎯 Overview

This project has been **completely refactored** from a single monolithic file into a clean, modular codebase that demonstrates Python best practices while teaching core programming concepts.

### ✨ What's New in v2.0

- **Modular Architecture**: Code separated into logical modules and packages
- **Type Hints**: Full type annotation support for better code clarity
- **Comprehensive Documentation**: Detailed docstrings for all functions and classes
- **Error Handling**: Robust exception handling patterns and examples
- **Interactive Menu**: User-friendly interface for exploring different concepts
- **Multiple Example Categories**: Basic, advanced, and error handling demonstrations
- **Configuration Management**: Centralized configuration and constants
- **Professional Structure**: Follows Python packaging best practices

## 📁 Project Structure

```
py-101/
├── src/                           # Core source modules
│   ├── math_utils.py             # Mathematical functions (factorial, fibonacci, primes)
│   ├── calculator.py             # Calculator classes (basic & scientific)
│   ├── data_utils.py             # Data manipulation utilities
│   ├── decorators.py             # Decorator patterns and examples
│   └── advanced_features.py      # Advanced Python features (generators, context managers)
├── examples/                      # Example and demonstration scripts
│   ├── basic_examples.py         # Fundamental Python concepts
│   ├── advanced_examples.py      # Advanced language features
│   └── error_handling_examples.py # Exception handling patterns
├── utils/                         # Utility modules (reserved for future use)
├── config.py                      # Configuration constants and settings
├── main.py                        # Main entry point with interactive menu
├── README.md                      # This file
└── TODO_refactor_py101.md        # Refactoring progress tracker
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd py-101
```

2. Run the main script:
```bash
python main.py
```

## 💻 Usage

### Interactive Mode (Default)

Run the main script to access the interactive menu:

```bash
python main.py
```

This provides a menu-driven interface to explore different Python concepts:

- **Basic Examples**: Variables, control flow, data structures
- **Advanced Examples**: Decorators, generators, context managers
- **Error Handling**: Exception patterns and recovery strategies
- **Individual Demonstrations**: Specific topic deep-dives

### Command Line Interface

Run specific demonstrations directly:

```bash
# Run all basic examples
python main.py basic

# Run advanced examples
python main.py advanced

# Run error handling examples
python main.py errors

# Run all demonstrations
python main.py all

# Show help
python main.py help
```

### Module Usage

Import and use individual modules in your own code:

```python
from src.math_utils import factorial, fibonacci_sequence, is_prime
from src.calculator import Calculator
from src.data_utils import process_text, analyze_list

# Use mathematical functions
print(factorial(5))                    # 120
print(fibonacci_sequence(10))          # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(is_prime(17))                   # True

# Use calculator
calc = Calculator()
result = calc.add(10, 5)              # 15

# Process data
stats = analyze_list([1, 2, 3, 4, 5])
print(stats)                          # {'count': 5, 'sum': 15, 'min': 1, 'max': 5, 'average': 3.0, 'range': 4}
```

## 📚 What You'll Learn

### 🔢 Mathematical Operations
- Factorial calculations with recursion
- Prime number detection algorithms
- Fibonacci sequence generation
- Mathematical utility functions

### 🧮 Object-Oriented Programming
- Class design and implementation
- Inheritance patterns
- Property decorators
- Method chaining

### 📊 Data Manipulation
- List and dictionary operations
- Set theory applications
- String processing techniques
- Data analysis functions

### 🎨 Advanced Python Features
- **Decorators**: Timing, logging, caching, validation
- **Generators**: Memory-efficient iteration patterns
- **Context Managers**: Resource management
- **Lambda Functions**: Functional programming concepts
- **Comprehensions**: Pythonic data transformations

### ⚠️ Error Handling
- Exception hierarchy and custom exceptions
- Try-catch-finally patterns
- Exception chaining and context
- Graceful error recovery
- Logging and debugging techniques

### 🔧 Best Practices
- Type hints and annotations
- Documentation standards
- Code organization and modularity
- Configuration management
- Testing patterns (demonstrated)

## 🎛️ Configuration

The `config.py` file contains centralized configuration including:

- **Constants**: Mathematical constants, application metadata
- **Sample Data**: Pre-configured datasets for demonstrations
- **Feature Flags**: Enable/disable specific features
- **Color Schemes**: Terminal output styling
- **Error Messages**: Standardized error messaging
- **Performance Settings**: Thresholds and limits

Example configuration usage:

```python
from config import SAMPLE_DATA, format_colored_text, is_feature_enabled

# Use sample data
numbers = SAMPLE_DATA['numbers']

# Colored output (if enabled)
if is_feature_enabled('enable_colors'):
    print(format_colored_text("Success!", 'green'))
```

## 📈 Features Demonstrated

### Core Python Concepts
- ✅ Variables and data types
- ✅ Control structures (if/else, loops)
- ✅ Functions and parameters
- ✅ Data structures (lists, dicts, sets, tuples)
- ✅ String manipulation
- ✅ File I/O simulation

### Intermediate Concepts
- ✅ List comprehensions
- ✅ Dictionary comprehensions
- ✅ Lambda functions
- ✅ Map, filter, reduce operations
- ✅ Exception handling
- ✅ Regular expressions (patterns)

### Advanced Concepts
- ✅ Decorators and metaclasses
- ✅ Generators and iterators
- ✅ Context managers
- ✅ Async programming concepts
- ✅ Functional programming patterns
- ✅ Design patterns (Singleton, Factory)

## 🧪 Testing and Validation

Each module includes comprehensive error handling and validation:

- **Input Validation**: Type checking and range validation
- **Error Recovery**: Graceful handling of edge cases
- **Logging**: Structured logging for debugging
- **Documentation**: Complete docstring coverage

## 🤝 Contributing

This project is designed for learning and exploration. Feel free to:

1. Add new modules to the `src/` directory
2. Create additional examples in `examples/`
3. Extend the configuration in `config.py`
4. Enhance the interactive menu in `main.py`

## 📝 License

This project is created for educational purposes and is open for learning and modification.

## 🎉 Acknowledgments

This refactored version demonstrates:
- Clean code principles
- Pythonic programming patterns  
- Professional project structure
- Comprehensive documentation
- Modular design patterns

---

**Happy Learning! 🐍✨**

Start exploring Python concepts with:
```bash
python main.py
```
