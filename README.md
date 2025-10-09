# Python 101 - Comprehensive Python Learning Project

A comprehensive Python project demonstrating core programming concepts, data structures, algorithms, and utility functions. This project serves as both a learning resource for Python beginners and a practical utility library.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Documentation](#documentation)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Features

- 🧮 **Mathematical Operations**: Factorial, prime checking, Fibonacci sequences, and advanced math utilities
- 📝 **String Manipulation**: Text processing, formatting, and validation functions  
- 📊 **Data Structures**: List, dictionary, set operations and custom data structure helpers
- 🔧 **Utility Functions**: File handling, validation, and common programming tasks
- 🎯 **Object-Oriented Programming**: Classes and decorators demonstration
- 🔄 **Functional Programming**: Lambda functions, map, filter, and reduce operations
- 🛡️ **Error Handling**: Comprehensive try-catch blocks and custom exceptions
- 🎲 **Random Operations**: Number generation and randomization utilities

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/py-101.git
   cd py-101
   ```

2. **Ensure Python 3.6+ is installed**:
   ```bash
   python --version
   ```

3. **No additional dependencies required** - uses only Python standard library!

## Usage

### Basic Usage

Run the main script to see all demonstrations:

```bash
python main.py
```

### Import specific modules

```python
from utils import string_utils, math_utils, data_structures

# Use string utilities
cleaned_text = string_utils.clean_text("  Hello World!  ")

# Use math utilities  
result = math_utils.gcd(48, 18)

# Use data structure helpers
sorted_dict = data_structures.sort_dict_by_value({"a": 3, "b": 1, "c": 2})
```

## Functions Overview

### Core Functions (main.py)

| Function | Description | Example |
|----------|-------------|---------|
| `factorial(n)` | Calculates factorial of n | `factorial(5)` → `120` |
| `is_prime(num)` | Checks if number is prime | `is_prime(17)` → `True` |
| `fibonacci_sequence(length)` | Generates Fibonacci sequence | `fibonacci_sequence(5)` → `[0,1,1,2,3]` |
| `greet(name)` | Prints personalized greeting | `greet("Alice")` → `"Hello, Alice!"` |

### String Utilities (utils/string_utils.py)

| Function | Description | Example |
|----------|-------------|---------|
| `clean_text(text)` | Removes extra whitespace | `"  hello  "` → `"hello"` |
| `is_palindrome(text)` | Checks if text is palindrome | `"racecar"` → `True` |
| `count_words(text)` | Counts words in text | `"hello world"` → `2` |
| `capitalize_words(text)` | Capitalizes each word | `"hello world"` → `"Hello World"` |

### Math Utilities (utils/math_utils.py)

| Function | Description | Example |
|----------|-------------|---------|
| `gcd(a, b)` | Greatest common divisor | `gcd(48, 18)` → `6` |
| `lcm(a, b)` | Least common multiple | `lcm(4, 6)` → `12` |
| `is_perfect_square(n)` | Checks if n is perfect square | `is_perfect_square(16)` → `True` |
| `generate_primes(limit)` | Generate primes up to limit | `generate_primes(10)` → `[2,3,5,7]` |

### Data Structure Helpers (utils/data_structures.py)

| Function | Description | Example |
|----------|-------------|---------|
| `merge_dicts(dict1, dict2)` | Merges two dictionaries | `merge_dicts({a:1}, {b:2})` → `{a:1, b:2}` |
| `flatten_list(nested_list)` | Flattens nested list | `[[1,2], [3,4]]` → `[1,2,3,4]` |
| `remove_duplicates(lst)` | Removes duplicates preserving order | `[1,2,2,3]` → `[1,2,3]` |
| `group_by_key(lst, key)` | Groups list of dicts by key | Groups objects by specified key |

## Project Structure

```
py-101/
├── main.py                 # Main demonstration script
├── utils/
│   ├── __init__.py        # Package initialization
│   ├── string_utils.py    # String manipulation functions
│   ├── math_utils.py      # Mathematical utility functions
│   ├── data_structures.py # Data structure helper functions
│   ├── file_utils.py      # File handling utilities
│   └── validators.py      # Input validation functions
├── examples/
│   ├── string_examples.py # String utility examples
│   ├── math_examples.py   # Math utility examples
│   └── data_examples.py   # Data structure examples
├── tests/
│   └── test_functions.py  # Basic function tests
├── docs/                   # Documentation
│   ├── API.md             # API documentation
│   ├── EXAMPLES.md        # Usage examples
│   ├── INSTALLATION.md    # Installation guide
│   ├── CONTRIBUTING.md    # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md # Community standards
│   ├── CHANGELOG.md       # Version history
│   ├── DEVELOPMENT.md     # Developer guide
│   ├── FAQ.md             # Frequently asked questions
│   └── FUNCTION_REFERENCE.md # Complete function reference
├── README.md              # This file
├── LICENSE                # MIT license
├── TODO_py101_enhancement.md # Development tasks
└── requirements.txt       # Dependencies (currently none)
```

## Examples

### Example 1: String Processing
```python
from utils.string_utils import clean_text, is_palindrome, count_words

text = "  A man a plan a canal Panama  "
cleaned = clean_text(text)  # "A man a plan a canal Panama"
is_palin = is_palindrome(cleaned.replace(" ", "").lower())  # True
word_count = count_words(cleaned)  # 7
```

### Example 2: Mathematical Operations
```python
from utils.math_utils import gcd, generate_primes, is_perfect_square

# Find GCD
result = gcd(48, 18)  # 6

# Generate prime numbers
primes = generate_primes(20)  # [2, 3, 5, 7, 11, 13, 17, 19]

# Check perfect square
is_square = is_perfect_square(25)  # True
```

### Example 3: Data Structure Manipulation
```python
from utils.data_structures import flatten_list, remove_duplicates, merge_dicts

# Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat = flatten_list(nested)  # [1, 2, 3, 4, 5]

# Remove duplicates
with_dupes = [1, 2, 2, 3, 1, 4]
unique = remove_duplicates(with_dupes)  # [1, 2, 3, 4]

# Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = merge_dicts(dict1, dict2)  # {"a": 1, "b": 2, "c": 3, "d": 4}
```

## Documentation

Python 101 includes comprehensive documentation:

### 📚 Core Documentation
- **[Installation Guide](docs/INSTALLATION.md)** - Complete setup instructions for all platforms
- **[API Reference](docs/API.md)** - Detailed documentation of all functions
- **[Usage Examples](docs/EXAMPLES.md)** - Real-world usage patterns and examples
- **[Function Reference](docs/FUNCTION_REFERENCE.md)** - Complete function catalog with complexity analysis

### 🛠️ Development Documentation  
- **[Contributing Guidelines](docs/CONTRIBUTING.md)** - How to contribute code and improvements
- **[Development Guide](docs/DEVELOPMENT.md)** - Advanced development topics and patterns
- **[Code of Conduct](docs/CODE_OF_CONDUCT.md)** - Community standards and guidelines

### 📋 Project Information
- **[Changelog](docs/CHANGELOG.md)** - Version history and release notes
- **[FAQ](docs/FAQ.md)** - Frequently asked questions and troubleshooting
- **[License](LICENSE)** - MIT license details

### Quick Start
```bash
# Get started immediately
git clone https://github.com/yourusername/py-101.git
cd py-101
python main.py

# Read the docs
ls docs/  # Browse available documentation
```

## Requirements

- **Python 3.6 or higher**
- **Standard Library Only** - No external dependencies required!

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Add docstrings to all functions
- Include type hints where appropriate
- Write simple tests for new functions
- Update the README with new functions
- Follow PEP 8 style guidelines

## Code Style

This project follows PEP 8 guidelines:
- Use 4 spaces for indentation
- Line length should not exceed 79 characters
- Use descriptive variable names
- Add docstrings to all functions

## Testing

Run the basic tests:
```bash
python tests/test_functions.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python Software Foundation for the amazing language
- The Python community for inspiration and best practices
- Contributors who help improve this learning resource

---

**Happy Coding! 🐍✨**

*This project is designed to be a comprehensive learning resource. Feel free to explore, modify, and extend it according to your needs.*