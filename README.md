# py-101 - Python Fundamentals Demo

A comprehensive Python demonstration script that showcases essential programming concepts and features for beginners and intermediate learners.

## 🚀 Overview

This project contains a single Python script (`main.py`) that demonstrates approximately 100 lines of Python code, covering fundamental programming concepts, data structures, functions, and best practices. It's designed as an educational resource for learning Python programming.

## ✨ Features

### Core Programming Concepts
- **Functions**: Recursive and iterative implementations
- **Control Flow**: Loops (`for`, `while`), conditionals (`if-else`)
- **Exception Handling**: `try-except-finally` blocks
- **Object-Oriented Programming**: Classes and methods

### Data Structures & Operations
- **Lists**: Comprehensions, methods, and manipulation
- **Dictionaries**: Creation, access, and operations
- **Sets**: Union and intersection operations
- **Tuples**: Unpacking and usage
- **Strings**: Manipulation and formatting

### Mathematical Operations
- **Factorial Calculation**: Recursive implementation
- **Prime Number Detection**: Efficient algorithm with square root optimization
- **Fibonacci Sequence**: Dynamic sequence generation

### Advanced Features
- **Decorators**: Function decoration example
- **Lambda Functions**: Anonymous function usage
- **Generators**: Memory-efficient iteration
- **Map/Filter/Reduce**: Functional programming concepts
- **Context Managers**: Resource management simulation

## 📋 Requirements

- **Python**: 3.6 or higher
- **Standard Library Modules Used**:
  - `sys`
  - `math`
  - `random`
  - `datetime`
  - `functools`

No external dependencies required!

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd py-101
   ```

2. **Verify Python installation**:
   ```bash
   python --version
   # or
   python3 --version
   ```

## 🏃‍♂️ Usage

### Running the Script

Execute the main script to see all demonstrations:

```bash
python main.py
```

### Expected Output

The script will demonstrate various Python features with output similar to:

```
Welcome to this Python demo script!
Factorial of 5: 120
Is 17 prime? True
First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Hello, World!
Counting: 1
Counting: 2
...
```

## 📚 Learning Objectives

After studying this code, you'll understand:

1. **Basic Syntax**: Variable assignment, function definitions, imports
2. **Control Structures**: Loops, conditionals, and flow control
3. **Data Types**: Working with numbers, strings, lists, dictionaries, sets, and tuples
4. **Functions**: Definition, parameters, return values, and recursion
5. **Error Handling**: Proper exception management
6. **Object-Oriented Basics**: Classes, methods, and instantiation
7. **Functional Programming**: Lambda functions, map, filter, reduce
8. **Advanced Concepts**: Decorators, generators, and context managers

## 🏗️ Code Structure

```
py-101/
├── README.md          # This file
├── main.py           # Main demonstration script
└── .git/             # Git repository files
```

### Key Functions in main.py

| Function | Purpose |
|----------|---------|
| `factorial(n)` | Calculates factorial recursively |
| `is_prime(num)` | Checks if a number is prime |
| `fibonacci_sequence(length)` | Generates Fibonacci sequence |
| `greet(name)` | Simple greeting function |
| `Calculator` class | Basic arithmetic operations |

## 🎯 Use Cases

- **Learning Python**: Perfect for beginners to see practical examples
- **Code Reference**: Quick reference for common Python patterns
- **Teaching Tool**: Educators can use this for Python instruction
- **Interview Preparation**: Review fundamental concepts

## 🧪 Testing the Code

You can modify the script to test different scenarios:

```python
# Test different factorial values
print("Factorial of 10:", factorial(10))

# Test prime checking with different numbers
test_numbers = [2, 3, 4, 17, 25, 29]
for num in test_numbers:
    print(f"Is {num} prime? {is_prime(num)}")

# Generate different Fibonacci sequence lengths
fib_20 = fibonacci_sequence(20)
print("First 20 Fibonacci numbers:", fib_20)
```

## 🤝 Contributing

Contributions are welcome! If you'd like to add more Python concepts or improve existing examples:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-concept`
3. Add your changes
4. Commit: `git commit -m "Add new Python concept demonstration"`
5. Push: `git push origin feature/new-concept`
6. Submit a Pull Request

### Ideas for Contributions
- Add more data structure examples
- Include file I/O operations
- Demonstrate web scraping basics
- Add unit tests
- Include performance benchmarking

## 📖 Additional Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python.org Beginner's Guide](https://www.python.org/about/gettingstarted/)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🏷️ Tags

`python` `education` `tutorial` `beginners` `programming-fundamentals` `demo` `learning-resource`

---

**Happy Learning! 🐍✨**

> This project is designed to be a comprehensive introduction to Python programming. Feel free to experiment with the code and make it your own!