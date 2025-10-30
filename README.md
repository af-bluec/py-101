# Python Features Showcase

A comprehensive collection of Python files demonstrating various features, concepts, and best practices.

## 📚 Overview

This project contains 11 Python files (including `main.py`) that showcase different aspects of Python programming, from basic data structures to advanced features like async programming and metaclasses.

## 📁 File Structure

```
.
├── main.py                      # Original demo script with basic concepts
├── 01_data_structures.py        # Lists, tuples, sets, and dictionaries
├── 02_functions_decorators.py   # Functions, decorators, and functional programming
├── 03_classes_oop.py            # Object-oriented programming concepts
├── 04_file_handling.py          # File I/O operations (text, JSON, CSV)
├── 05_error_handling.py         # Exception handling and custom exceptions
├── 06_comprehensions.py         # List, dict, set comprehensions and generators
├── 07_iterators_generators.py   # Custom iterators and generator functions
├── 08_async_programming.py      # Async/await and asyncio patterns
├── 09_context_managers.py       # Context managers and resource management
├── 10_advanced_features.py      # Type hints, dataclasses, metaclasses, etc.
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher (Python 3.8+ recommended for full async support)
- No external dependencies required (uses only standard library)

### Running the Examples

Each file can be run independently:

```bash
# Run individual files
python 01_data_structures.py
python 02_functions_decorators.py
python 03_classes_oop.py
# ... and so on

# Or run all files sequentially
for file in *.py; do
    echo "Running $file..."
    python "$file"
    echo "---"
done
```

## 📖 What You'll Learn

### 1. Data Structures (`01_data_structures.py`)
- **Lists**: Mutable sequences with append, insert, remove, slicing
- **Tuples**: Immutable sequences and unpacking
- **Sets**: Unique elements and set operations (union, intersection, difference)
- **Dictionaries**: Key-value mappings and dictionary methods
- **Comprehensions**: Concise syntax for creating collections

### 2. Functions & Decorators (`02_functions_decorators.py`)
- Basic functions with default parameters
- `*args` and `**kwargs` for variable arguments
- Lambda functions for inline operations
- Decorators for function modification
- Higher-order functions and closures
- Generator functions with `yield`
- `map()`, `filter()`, and `reduce()`

### 3. Object-Oriented Programming (`03_classes_oop.py`)
- Class definition with `__init__` constructor
- Instance and class variables
- Class methods (`@classmethod`) and static methods (`@staticmethod`)
- Inheritance and method overriding
- Polymorphism
- Special methods (`__str__`, `__add__`, `__eq__`, etc.)
- Property decorators for getters and setters

### 4. File Handling (`04_file_handling.py`)
- Reading and writing text files
- JSON serialization and deserialization
- CSV file operations
- `pathlib` for modern file operations
- Context managers for safe file handling
- File cleanup and resource management

### 5. Error Handling (`05_error_handling.py`)
- `try-except` blocks for exception handling
- Multiple exception types
- `else` and `finally` clauses
- Custom exception classes
- Exception chaining
- Context managers for error handling
- Assertions for debugging

### 6. Comprehensions (`06_comprehensions.py`)
- List comprehensions with conditions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions for memory efficiency
- Nested comprehensions
- Practical examples and performance comparison

### 7. Iterators & Generators (`07_iterators_generators.py`)
- Custom iterator classes with `__iter__` and `__next__`
- Generator functions with `yield`
- Infinite sequences
- `itertools` module utilities
- `yield from` for delegation
- Pipeline processing patterns

### 8. Async Programming (`08_async_programming.py`)
- `async`/`await` syntax
- `asyncio.gather()` for concurrent execution
- Async context managers
- Async iterators and generators
- Timeout handling with `asyncio.wait_for()`
- Task cancellation
- Semaphores for limiting concurrency
- Async queues for producer-consumer patterns

### 9. Context Managers (`09_context_managers.py`)
- `with` statement for resource management
- Custom context managers with `__enter__` and `__exit__`
- `@contextmanager` decorator
- `contextlib.suppress` for ignoring exceptions
- `contextlib.redirect_stdout` for output capture
- `ExitStack` for dynamic context management
- Practical examples (timers, locks, resource pools)

### 10. Advanced Features (`10_advanced_features.py`)
- Type hints and annotations
- Generic types with `TypeVar`
- Dataclasses for reducing boilerplate
- Enums for named constants
- Named tuples
- Descriptors for attribute validation
- Metaclasses (Singleton pattern)
- Advanced decorators (`@lru_cache`, custom decorators)
- Collections (`defaultdict`, `Counter`, `deque`)
- `__slots__` for memory optimization

## 💡 Key Concepts

### Python Philosophy (The Zen of Python)
```python
import this
```

- **Beautiful is better than ugly**
- **Explicit is better than implicit**
- **Simple is better than complex**
- **Readability counts**

### Best Practices Demonstrated

1. **Use context managers** for resource management
2. **Type hints** for better code documentation
3. **List comprehensions** for concise, readable code
4. **Generators** for memory-efficient iteration
5. **Dataclasses** to reduce boilerplate
6. **Exception handling** for robust code
7. **Async programming** for I/O-bound operations
8. **Decorators** for code reuse and separation of concerns

## 🎯 Learning Path

**Beginner** → Start here:
1. `01_data_structures.py`
2. `02_functions_decorators.py`
3. `03_classes_oop.py`
4. `04_file_handling.py`

**Intermediate** → Continue with:
5. `05_error_handling.py`
6. `06_comprehensions.py`
7. `07_iterators_generators.py`

**Advanced** → Master these:
8. `08_async_programming.py`
9. `09_context_managers.py`
10. `10_advanced_features.py`

## 🔧 Customization

Feel free to modify any file to experiment with the concepts. Each file is self-contained and can be run independently.

### Example Modifications

```python
# In 01_data_structures.py, try adding your own data:
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "Your Name", "age": 25}

# In 02_functions_decorators.py, create your own decorator:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

# In 08_async_programming.py, add your own async function:
async def my_async_task():
    await asyncio.sleep(1)
    return "Done!"
```

## 📚 Additional Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Package Index (PyPI)](https://pypi.org/)

## 🤝 Contributing

This is a learning project. Feel free to:
- Add more examples
- Improve existing code
- Add comments for clarity
- Create new files for additional topics

## 📝 Topics Covered

- ✅ Data Structures
- ✅ Functions & Decorators
- ✅ Object-Oriented Programming
- ✅ File I/O
- ✅ Error Handling
- ✅ Comprehensions
- ✅ Iterators & Generators
- ✅ Async Programming
- ✅ Context Managers
- ✅ Type Hints
- ✅ Dataclasses
- ✅ Metaclasses
- ✅ And much more!

## 🎓 Next Steps

After mastering these concepts, consider exploring:
- **Web frameworks**: Django, Flask, FastAPI
- **Data science**: NumPy, Pandas, Matplotlib
- **Machine learning**: scikit-learn, TensorFlow, PyTorch
- **Testing**: pytest, unittest
- **Packaging**: setuptools, poetry
- **Async frameworks**: aiohttp, Trio

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

Built to demonstrate Python's versatility and power. Happy coding! 🐍

---

**Note**: All files use only Python's standard library, so no additional installations are required!
