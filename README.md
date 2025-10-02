# Python Demo Application

A refactored Python demonstration script showcasing various programming concepts organized into modular, reusable components.

## 🚀 Features

This application demonstrates:

- **Mathematical Operations**: Factorial, prime checking, Fibonacci sequences
- **String Manipulation**: Formatting, analysis, transformations
- **Data Structures**: Lists, sets, dictionaries, tuples with various operations
- **Object-Oriented Programming**: Calculator classes with inheritance
- **Decorators**: Timing, logging, caching, validation decorators
- **Generators**: Number sequences, batching, cycling
- **Error Handling**: Try-catch patterns, custom exceptions
- **Functional Programming**: Lambda functions, map, filter, reduce operations
- **Advanced Features**: Context managers, comprehensions, unpacking

## 📁 Project Structure

```
├── main.py                          # Main entry point
├── config/                          # Configuration and constants
│   ├── __init__.py
│   └── constants.py
├── utils/                           # Utility functions
│   ├── __init__.py
│   ├── math_utils.py               # Mathematical functions
│   ├── string_utils.py             # String operations
│   └── data_structures.py          # Data structure utilities
├── classes/                         # Object-oriented components
│   ├── __init__.py
│   └── calculator.py               # Calculator classes
├── decorators/                      # Function decorators
│   ├── __init__.py
│   └── function_decorators.py      # Various decorators
├── generators/                      # Generator functions
│   ├── __init__.py
│   └── number_generators.py        # Number sequence generators
└── examples/                        # Demonstration functions
    ├── __init__.py
    └── demonstrations.py           # Comprehensive examples
```

## 🛠️ Installation

No additional dependencies required! This project uses only Python standard library.

**Requirements:**
- Python 3.6 or higher

## 🏃‍♂️ Usage

### Running the Complete Demo

```bash
python3 main.py
```

This will run all demonstrations in sequence, showing:
- Mathematical function examples
- String operations
- Data structure manipulations
- Object-oriented programming
- Decorator functionality
- Generator usage
- Error handling patterns
- Advanced Python features

### Using Individual Modules

You can also import and use individual components:

```python
# Mathematical utilities
from utils.math_utils import factorial, is_prime, fibonacci_sequence

print(factorial(5))  # 120
print(is_prime(17))  # True
print(fibonacci_sequence(8))  # [0, 1, 1, 2, 3, 5, 8, 13]

# Calculator class
from classes.calculator import Calculator, ScientificCalculator

calc = Calculator()
result = calc.add(10, 5)
print(result)  # 15

sci_calc = ScientificCalculator()
sine_value = sci_calc.sin(90, degrees=True)
print(sine_value)  # ~1.0

# String utilities
from utils.string_utils import greet, analyze_text

print(greet("World"))  # Hello, World!
analysis = analyze_text("Python Programming")
print(analysis['word_count'])  # 2

# Generators
from generators.number_generators import fibonacci_generator, prime_generator

# Get first 5 Fibonacci numbers
fib_gen = fibonacci_generator()
fib_numbers = [next(fib_gen) for _ in range(5)]
print(fib_numbers)  # [0, 1, 1, 2, 3]

# Decorators
from decorators.function_decorators import timer, cache

@timer
@cache
def expensive_function(n):
    return sum(range(n))

result = expensive_function(1000)  # Will show timing and caching info
```

## 📚 Module Documentation

### utils.math_utils
- `factorial(n)`: Calculate factorial using recursion
- `is_prime(num)`: Check if a number is prime
- `fibonacci_sequence(length)`: Generate Fibonacci sequence
- `gcd(a, b)`: Greatest Common Divisor
- `lcm(a, b)`: Least Common Multiple

### utils.string_utils
- `greet(name)`: Generate greeting message
- `analyze_text(text)`: Comprehensive text analysis
- `format_person_info(name, age)`: Format person information
- `reverse_words(text)`: Reverse word order
- `capitalize_words(text)`: Capitalize each word

### classes.calculator
- `Calculator`: Basic arithmetic operations with history
- `ScientificCalculator`: Extended with trigonometric and logarithmic functions

### decorators.function_decorators
- `@timer`: Measure execution time
- `@logger`: Log function calls and returns
- `@cache`: Memoization decorator
- `@retry`: Retry failed function calls
- `@validate_types`: Runtime type validation

### generators.number_generators
- `fibonacci_generator()`: Infinite Fibonacci sequence
- `prime_generator(limit)`: Prime numbers up to limit
- `even_numbers(start, limit)`: Even number sequence
- `square_generator(limit)`: Perfect squares
- `batch_generator(iterable, size)`: Group items into batches

## 🎯 Key Improvements Over Original

1. **Modularity**: Code split into logical, reusable modules
2. **Type Hints**: Added throughout for better IDE support and documentation
3. **Documentation**: Comprehensive docstrings for all functions
4. **Error Handling**: Improved with custom exceptions and validation
5. **Extensibility**: Easy to add new features to existing modules
6. **Reusability**: Functions can be imported and used in other projects
7. **Organization**: Clear separation of concerns and responsibilities
8. **Testing**: Structure supports easy unit testing
9. **Maintainability**: Easier to modify and update individual components

## 🔧 Configuration

The `config/constants.py` file contains configurable settings:

- Mathematical constants (PI, E, GOLDEN_RATIO)
- Application metadata (name, version, author)
- Default values for demonstrations
- Color codes for terminal output
- Error messages and templates

## 🚦 Examples Output

The application provides colorized terminal output showing:

```
==================================================
Welcome to this Python demo script!
==================================================

📊 Mathematical Functions:
Factorial of 5: 120
Is 17 prime? True
First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

📝 String Operations:
Greeting: Hello, Alice!
Person info: Alice is 30 years old.

🗂️  Data Structures:
Squares (1-5): [1, 4, 9, 16, 25]
Set union {1, 2, 3} ∪ {3, 4, 5}: {1, 2, 3, 4, 5}
Average score: 91.7

[... and more demonstrations ...]
```

## 🤝 Contributing

This is a demonstration project showing best practices for:
- Code organization and structure
- Documentation and type hints  
- Modular design patterns
- Python idioms and conventions

Feel free to extend the modules or add new demonstrations!

## 📄 License

This project is for educational purposes and demonstrates Python programming concepts.

---

**Version**: 2.0.0  
**Author**: Refactored Code Team  
**Python**: 3.6+
