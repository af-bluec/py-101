# py101 - Python Educational Package

A comprehensive Python package designed to demonstrate fundamental programming concepts and best practices. This project serves as both a learning resource and a practical example of well-structured Python code.

## 🚀 Features

- **Mathematical Operations**: Factorial calculation, prime number checking, Fibonacci sequence generation
- **Calculator**: Basic arithmetic operations with error handling
- **Utility Functions**: String manipulation, data structure operations, lambda examples
- **Python Demos**: Interactive demonstrations of Python language features
- **Comprehensive Testing**: Full test coverage with pytest
- **Type Hints**: Complete type annotations for better code clarity
- **Logging**: Structured logging throughout the application
- **CLI Interface**: Command-line interface with multiple execution modes

## 📁 Project Structure

```
py101/
├── py101/                      # Main package directory
│   ├── __init__.py            # Package initialization and exports
│   ├── math_ops/              # Mathematical operations module
│   │   └── __init__.py        # Factorial, prime, fibonacci functions
│   ├── calculator/            # Calculator module
│   │   └── __init__.py        # Calculator class with basic operations
│   ├── utils/                 # Utility functions module
│   │   └── __init__.py        # Helper functions and utilities
│   └── demos/                 # Python feature demonstrations
│       └── __init__.py        # Interactive demos and examples
├── tests/                     # Unit tests
│   ├── test_math_ops.py       # Tests for math operations
│   ├── test_calculator.py     # Tests for calculator
│   └── test_utils.py          # Tests for utilities
├── examples/                  # Example scripts and usage
├── docs/                      # Documentation
├── main.py                    # Main entry point
├── pyproject.toml            # Project configuration and dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore patterns
└── TODO_refactor.md         # Refactoring progress tracker
```

## 🛠 Installation

### Prerequisites
- Python 3.8 or higher

### Install from source
```bash
git clone <repository-url>
cd py101
pip install -e .
```

### Install development dependencies
```bash
pip install -e .[dev]
```

## 💻 Usage

### Command Line Interface

Run the complete demonstration:
```bash
python main.py
```

Run in interactive mode:
```bash
python main.py --mode interactive
```

Set logging level:
```bash
python main.py --log-level DEBUG
```

### As a Python Package

```python
from py101 import Calculator, factorial, fibonacci_sequence, greet

# Use the calculator
calc = Calculator()
result = calc.add(5, 3)
print(f"5 + 3 = {result}")

# Mathematical operations
print(f"Factorial of 5: {factorial(5)}")
print(f"First 10 Fibonacci numbers: {fibonacci_sequence(10)}")

# Utility functions
print(greet("Python Developer"))
```

### Interactive Examples

```python
from py101 import PythonFeatureDemo

# Run all Python feature demonstrations
demo = PythonFeatureDemo()
demo.run_all_demos()

# Or run individual demos
demo.demonstrate_loops()
demo.demonstrate_exception_handling()
```

## 🧪 Testing

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=py101 --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_math_ops.py -v
```

## 📚 API Documentation

### Math Operations (`py101.math_ops`)

- `factorial(n: int) -> int`: Calculate factorial of n
- `is_prime(num: int) -> bool`: Check if number is prime
- `fibonacci_sequence(length: int) -> List[int]`: Generate Fibonacci sequence

### Calculator (`py101.calculator`)

- `Calculator.add(a, b)`: Addition
- `Calculator.subtract(a, b)`: Subtraction  
- `Calculator.multiply(a, b)`: Multiplication
- `Calculator.divide(a, b)`: Division (with zero-division protection)
- `Calculator.power(base, exponent)`: Exponentiation

### Utilities (`py101.utils`)

- `greet(name: str) -> str`: Generate greeting message
- `string_operations(text: str) -> dict`: Various string manipulations
- `list_operations(numbers: List[int]) -> dict`: Statistical operations on lists
- `set_operations(set1, set2) -> dict`: Set theory operations

### Demos (`py101.demos`)

- `PythonFeatureDemo`: Interactive demonstrations of Python features
- Covers loops, conditionals, exception handling, data structures, and more

## 🎯 Learning Objectives

This package demonstrates:

1. **Project Structure**: Proper Python package organization
2. **Type Safety**: Complete type hints and mypy compatibility
3. **Error Handling**: Comprehensive exception handling patterns
4. **Testing**: Unit testing best practices with pytest
5. **Documentation**: Clear docstrings and README documentation
6. **CLI Design**: Command-line interface with argparse
7. **Logging**: Structured logging implementation
8. **Code Quality**: PEP 8 compliance and clean code practices

## 🔧 Development

### Code Quality Tools

Format code with Black:
```bash
black py101/ tests/
```

Type checking with mypy:
```bash
mypy py101/
```

Linting with flake8:
```bash
flake8 py101/ tests/
```

### Pre-commit Hooks

Install pre-commit hooks:
```bash
pre-commit install
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass (`pytest`)
6. Format your code (`black .`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## 📝 Changelog

### Version 1.0.0
- Initial release with complete refactoring
- Modular package structure
- Comprehensive test coverage
- CLI interface
- Full type hint support
- Documentation and examples

## 🙏 Acknowledgments

- Python community for excellent tooling and libraries
- Contributors and educators who make learning Python accessible
- Open source projects that inspired this educational resource

---

**Happy Learning! 🐍**
