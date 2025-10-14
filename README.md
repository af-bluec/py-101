# py-101 🐍

A comprehensive Python learning script that demonstrates fundamental programming concepts and best practices. This educational project covers essential Python features through practical examples and well-documented code.

## 📋 Overview

This project is designed as a learning resource for Python beginners and intermediate developers. It showcases over 100 lines of Python code demonstrating various programming concepts including functions, classes, data structures, exception handling, and more.

## ✨ Features Demonstrated

### Core Python Concepts
- **Functions**: Factorial calculation, prime number checking, Fibonacci sequence generation
- **Classes & Objects**: Calculator class with basic arithmetic operations
- **Data Structures**: Lists, dictionaries, sets, tuples
- **Control Flow**: Loops, conditionals, exception handling
- **String Manipulation**: Formatting, methods, operations

### Advanced Topics
- **Recursion**: Factorial and countdown examples
- **Lambda Functions**: Anonymous function demonstrations
- **List Comprehensions**: Efficient list creation
- **Decorators**: Function wrapping and enhancement
- **Generators**: Memory-efficient iteration
- **Context Management**: Resource handling simulation

### Built-in Functions & Libraries
- **Math Operations**: Using the `math` module
- **Random Numbers**: Random number generation
- **Date/Time**: Working with dates
- **Functional Programming**: Map, filter, and reduce operations

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses only standard library)

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd py-101
   ```

2. Run the script:
   ```bash
   python main.py
   ```

## 💡 Usage Examples

The script demonstrates various Python concepts through interactive examples:

### Mathematical Operations
```python
# Factorial calculation
print("Factorial of 5:", factorial(5))  # Output: 120

# Prime number checking
print("Is 17 prime?", is_prime(17))     # Output: True
```

### Data Structures
```python
# List comprehension
squares = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]

# Dictionary operations
person = {"name": "Alice", "age": 30}
```

### Object-Oriented Programming
```python
# Using the Calculator class
calc = Calculator()
result = calc.add(5, 3)  # Returns: 8
```

## 📂 Project Structure

```
py-101/
│
├── README.md          # Project documentation
├── main.py           # Main Python demonstration script
└── .git/             # Git repository files
```

## 🎯 Learning Objectives

After studying this code, you should understand:

1. **Basic Python Syntax**: Variables, functions, and control structures
2. **Data Types**: Working with numbers, strings, lists, and dictionaries
3. **Error Handling**: Using try-except blocks effectively
4. **Object-Oriented Programming**: Classes and methods
5. **Functional Programming**: Lambda functions and higher-order functions
6. **Python Best Practices**: Code organization and documentation

## 🔧 Code Highlights

### Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Decorator Pattern
```python
@my_decorator
def say_hello():
    print("Hello from decorated function!")
```

### Generator Expression
```python
gen = (x for x in range(3))
for val in gen:
    print("Generator value:", val)
```

## 🤝 Contributing

This is an educational project. If you'd like to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-concept`)
3. Add your educational examples
4. Commit your changes (`git commit -am 'Add new Python concept'`)
5. Push to the branch (`git push origin feature/new-concept`)
6. Create a Pull Request

### Contribution Guidelines
- Keep examples simple and well-documented
- Add comments explaining complex concepts
- Ensure code follows PEP 8 style guidelines
- Test your code before submitting

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python PEP 8 Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Python.org Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and distribute for learning and teaching Python programming concepts.

## 🎓 About

Created as a comprehensive Python learning resource covering fundamental to intermediate programming concepts. Perfect for:
- Python beginners looking to understand core concepts
- Educators teaching Python programming
- Developers reviewing Python fundamentals
- Code review and best practices demonstration

---

**Happy Learning! 🐍✨**