# Frequently Asked Questions (FAQ)

## Python 101 - FAQ

Common questions and answers about the Python 101 project.

---

## General Questions

### Q: What is Python 101?

**A:** Python 101 is a comprehensive educational project designed to teach Python programming concepts through practical examples and utility functions. It covers core programming concepts, data structures, algorithms, and common programming tasks using only Python's standard library.

### Q: Who is this project for?

**A:** This project is designed for:
- **Python beginners** learning the language fundamentals
- **Students** studying computer science or programming
- **Educators** looking for teaching materials and examples
- **Developers** wanting to see clean, documented Python code examples
- **Anyone** interested in improving their Python skills

### Q: What Python version do I need?

**A:** Python 101 requires **Python 3.6 or higher**. We recommend Python 3.8+ for the best experience and performance. The project is tested on:
- Python 3.6, 3.7, 3.8, 3.9, 3.10, 3.11+
- Windows, macOS, and Linux operating systems

### Q: Does this project have any dependencies?

**A:** No! Python 101 uses **only the Python standard library**. This is intentional to:
- Keep the project simple and focused on core Python concepts
- Avoid dependency management complexity
- Ensure the project works out-of-the-box on any Python installation
- Demonstrate what's possible with just Python's built-in modules

---

## Installation and Setup

### Q: How do I install Python 101?

**A:** Simply clone the repository:

```bash
git clone https://github.com/yourusername/py-101.git
cd py-101
python main.py
```

No additional installation steps are required! See our [Installation Guide](INSTALLATION.md) for detailed instructions.

### Q: I'm getting "ModuleNotFoundError" when importing utils

**A:** This usually means you're not in the correct directory. Make sure you:

1. Navigate to the project root directory:
   ```bash
   cd py-101
   ```

2. Run Python from the project root:
   ```bash
   python main.py
   # or
   python -c "from utils import string_utils; print('Works!')"
   ```

3. Check that the `utils` directory exists and contains `__init__.py`

### Q: Can I use Python 101 in a virtual environment?

**A:** Absolutely! Virtual environments are recommended for any Python project:

```bash
# Create virtual environment
python -m venv py101_env

# Activate it
source py101_env/bin/activate  # macOS/Linux
# or
py101_env\Scripts\activate     # Windows

# Use the project
cd py-101
python main.py
```

### Q: Why doesn't `python` work but `python3` does?

**A:** This is common on macOS and Linux systems where `python` refers to Python 2.x and `python3` refers to Python 3.x. Always use `python3` on these systems:

```bash
python3 main.py
python3 -c "from utils import math_utils"
```

---

## Usage Questions

### Q: How do I use specific functions from the utils modules?

**A:** Import them directly:

```python
# Import specific functions
from utils.string_utils import clean_text, is_palindrome
from utils.math_utils import gcd, generate_primes

# Use them
cleaned = clean_text("  hello world  ")
is_palin = is_palindrome("racecar")
result = gcd(48, 18)
```

### Q: Can I use this project in my own code?

**A:** Yes! Python 101 is licensed under the MIT License, which allows:
- ✅ Commercial use
- ✅ Modification  
- ✅ Distribution
- ✅ Private use

Just include the license notice. See [LICENSE](../LICENSE) for details.

### Q: How do I run the examples?

**A:** Examples are in the `examples/` directory:

```bash
# Run specific example files
python examples/string_examples.py
python examples/math_examples.py
python examples/data_examples.py

# Or import and use in your own code
from examples.string_examples import demo_string_functions
demo_string_functions()
```

### Q: What's the difference between main.py and the utils modules?

**A:** 
- **main.py**: Contains core demonstration functions and runs a complete demo
- **utils/**: Contains organized utility modules for specific purposes
  - `string_utils.py` - String manipulation
  - `math_utils.py` - Mathematical operations
  - `data_structures.py` - Data structure helpers
  - `file_utils.py` - File operations
  - `validators.py` - Input validation

---

## Functionality Questions

### Q: What functions are available?

**A:** Python 101 includes 25+ functions across different categories:

**Core Functions (main.py):**
- `factorial()`, `is_prime()`, `fibonacci_sequence()`, `greet()`

**String Utils:**
- `clean_text()`, `is_palindrome()`, `count_words()`, `capitalize_words()`, `reverse_words()`

**Math Utils:**
- `gcd()`, `lcm()`, `is_perfect_square()`, `generate_primes()`, `power()`

**Data Structure Utils:**
- `merge_dicts()`, `flatten_list()`, `remove_duplicates()`, `group_by_key()`, `sort_dict_by_value()`

**File Utils:**
- `read_file()`, `write_file()`, `file_exists()`

**Validators:**
- `validate_email()`, `validate_phone()`, `is_positive_integer()`

See [API.md](API.md) for complete function documentation.

### Q: How do I find prime numbers up to 1000?

**A:**
```python
from utils.math_utils import generate_primes

primes = generate_primes(1000)
print(f"Found {len(primes)} primes up to 1000")
print(f"First 10 primes: {primes[:10]}")
```

### Q: How do I check if text is a palindrome?

**A:**
```python
from utils.string_utils import is_palindrome

# Simple check
result = is_palindrome("racecar")  # True

# Case-insensitive (default)
result = is_palindrome("A man a plan a canal Panama")  # True

# Case-sensitive
result = is_palindrome("Racecar", ignore_case=False)  # False
```

### Q: How do I process a text file?

**A:**
```python
from utils.file_utils import read_file, write_file
from utils.string_utils import clean_text, count_words

# Read file
content = read_file("input.txt")

# Process content
lines = content.split('\n')
processed_lines = []
total_words = 0

for line in lines:
    cleaned = clean_text(line)
    if cleaned:
        word_count = count_words(cleaned)
        total_words += word_count
        processed_lines.append(f"{cleaned} ({word_count} words)")

# Write results
result = '\n'.join(processed_lines) + f"\n\nTotal words: {total_words}"
write_file("output.txt", result)
```

---

## Development Questions

### Q: How do I contribute to the project?

**A:** We welcome contributions! Please:

1. Read our [Contributing Guidelines](CONTRIBUTING.md)
2. Check existing [issues](https://github.com/yourusername/py-101/issues)
3. Fork the repository
4. Create a feature branch
5. Make your changes with tests and documentation
6. Submit a pull request

### Q: How do I add a new function?

**A:** Follow these steps:

1. **Choose appropriate module** (or create new one)
2. **Implement function** with docstring and type hints
3. **Add tests** in `tests/test_functions.py`
4. **Add examples** in relevant example file
5. **Update documentation** (API.md, README.md)
6. **Test thoroughly** before submitting

Example:
```python
# utils/string_utils.py
def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: String to reverse
        
    Returns:
        Reversed string
        
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text[::-1]
```

### Q: How do I run tests?

**A:**
```bash
# Run all tests
python tests/test_functions.py

# Run with more verbose output
python -m unittest tests.test_functions -v

# Test specific function
python -c "from utils.string_utils import clean_text; print(clean_text('  test  '))"
```

### Q: What coding style should I follow?

**A:** We follow **PEP 8** with these guidelines:
- 4 spaces for indentation (no tabs)
- Maximum line length of 79 characters
- Descriptive variable names in snake_case
- Functions in snake_case, classes in PascalCase
- Comprehensive docstrings for all functions
- Type hints where appropriate

See our [Development Guide](DEVELOPMENT.md) for details.

---

## Performance Questions

### Q: Is Python 101 suitable for large datasets?

**A:** Python 101 is designed for **educational purposes** and moderate-sized data. For large datasets:

- **File processing**: Functions process line-by-line when possible
- **Memory usage**: Most functions are memory-efficient
- **Prime generation**: Uses Sieve of Eratosthenes (efficient algorithm)
- **String operations**: Optimized for typical use cases

For production use with very large datasets, consider:
- Using NumPy for numerical computations
- Using pandas for data processing
- Implementing specialized algorithms for your use case

### Q: How fast are the mathematical functions?

**A:** Performance characteristics:

- **Factorial**: O(n) - efficient iterative implementation
- **Prime checking**: O(√n) - optimized algorithm
- **GCD**: O(log(min(a,b))) - uses Euclidean algorithm
- **Prime generation**: O(n log log n) - Sieve of Eratosthenes
- **Fibonacci**: O(n) - iterative implementation

For very large numbers, consider specialized libraries like `math` module or `sympy`.

### Q: Can I optimize the functions for my specific use case?

**A:** Absolutely! The code is designed to be:
- **Readable and educational** first
- **Correct and reliable** second  
- **Reasonably efficient** third

Feel free to modify functions for your needs, or use them as starting points for more specialized implementations.

---

## Educational Questions

### Q: How can I use this project for learning?

**A:** Great question! Here are learning approaches:

**For Beginners:**
1. **Start with main.py** - understand basic function structure
2. **Read function docstrings** - learn what each function does
3. **Run examples** - see functions in action
4. **Modify parameters** - experiment with different inputs
5. **Read the code** - understand implementation details

**For Intermediate Learners:**
1. **Study algorithms** - understand how Sieve of Eratosthenes works
2. **Analyze complexity** - learn about O(n), O(log n), etc.
3. **Compare approaches** - see different ways to solve problems
4. **Extend functions** - add new features or optimizations
5. **Write tests** - practice test-driven development

**For Advanced Learners:**
1. **Optimize algorithms** - improve performance
2. **Add type systems** - use mypy for static type checking
3. **Create new modules** - extend the project architecture
4. **Contribute features** - help improve the project

### Q: What Python concepts does this project demonstrate?

**A:** Python 101 covers many core concepts:

**Basic Concepts:**
- Functions and parameters
- Variables and data types
- Control flow (if/else, loops)
- Error handling (try/except)

**Intermediate Concepts:**
- Modules and imports
- List comprehensions
- Dictionary operations
- File I/O operations
- String manipulation

**Advanced Concepts:**
- Type hints and annotations
- Docstrings and documentation
- Algorithm complexity
- Code organization and structure
- Testing and validation

### Q: Can I use this project for teaching?

**A:** Yes! Python 101 is specifically designed for educational use:

**For Teachers:**
- Well-documented code examples
- Progressive complexity levels
- Real-world applications
- Complete project structure
- Ready-to-use examples

**Suggested Teaching Approach:**
1. **Demo main.py** - show what the project does
2. **Explain one module** - deep dive into string_utils.py
3. **Have students experiment** - modify functions, try different inputs
4. **Assign exercises** - implement new functions using existing patterns
5. **Code review** - discuss different approaches and improvements

### Q: What's the best way to study the code?

**A:** Here's a suggested study approach:

**Phase 1: Understanding**
```bash
# Run the main demo
python main.py

# Study one module at a time
python -c "from utils import string_utils; help(string_utils)"
```

**Phase 2: Experimentation**
```python
# Try functions with different inputs
from utils.string_utils import is_palindrome

# Experiment with edge cases
print(is_palindrome(""))        # Empty string
print(is_palindrome("a"))       # Single character
print(is_palindrome("Aa"))      # Case sensitivity
```

**Phase 3: Implementation**
```python
# Try implementing your own version
def my_palindrome_check(text):
    # Your implementation here
    pass

# Compare with existing implementation
```

---

## Troubleshooting

### Q: The project seems to be running slowly. What can I do?

**A:** Try these solutions:

1. **Check Python version**: Use Python 3.8+ for better performance
2. **Use appropriate test sizes**: Don't generate primes up to 1,000,000 for learning
3. **Profile your code**: Use timing functions to identify bottlenecks
4. **Check system resources**: Ensure adequate memory and CPU

### Q: I'm getting unexpected results from a function. How do I debug?

**A:** Debugging approach:

1. **Check input types and values**:
   ```python
   def debug_function(input_val):
       print(f"Input type: {type(input_val)}")
       print(f"Input value: {repr(input_val)}")
       # Your function call here
   ```

2. **Read the docstring** for expected input/output format
3. **Try simple test cases** first
4. **Check error messages** carefully
5. **Look at examples** in the documentation

### Q: How do I report bugs or request features?

**A:** Use GitHub issues:

1. **Search existing issues** first
2. **For bugs**: Include error messages, input values, expected vs actual output
3. **For features**: Explain the use case and provide examples
4. **Be specific**: Include Python version, operating system, relevant code

**Bug Report Template:**
```markdown
**Bug Description:** Clear description of the problem

**Steps to Reproduce:**
1. Import function X
2. Call with parameters Y
3. See error Z

**Expected:** What should happen
**Actual:** What actually happens
**Environment:** Python 3.x, OS, etc.
```

---

## Community and Support

### Q: Where can I get help?

**A:** Several resources available:

1. **Documentation**: Check docs/ folder first
2. **Examples**: Look in examples/ directory
3. **GitHub Issues**: Search for similar questions
4. **Create an Issue**: Ask specific questions
5. **Code Comments**: Many functions have detailed comments

### Q: How can I help improve Python 101?

**A:** Many ways to contribute:

- **Report bugs** you find
- **Suggest new functions** or features
- **Improve documentation** - fix typos, add clarity
- **Add examples** - show creative uses
- **Write tests** - help ensure reliability
- **Share your use cases** - help others learn

### Q: Can I use Python 101 in my classroom/workshop?

**A:** Absolutely! Python 101 is perfect for:

- **Computer Science courses**
- **Python workshops**
- **Coding bootcamps**  
- **Self-study groups**
- **Programming tutorials**

The MIT license allows free use in educational settings. We'd love to hear about your experiences!

### Q: How often is the project updated?

**A:** Python 101 is actively maintained:

- **Bug fixes**: As needed
- **New functions**: Based on community requests
- **Documentation**: Ongoing improvements
- **Compatibility**: Kept current with Python versions

Check the [CHANGELOG.md](CHANGELOG.md) for recent updates.

---

## Advanced Usage

### Q: Can I extend Python 101 with my own modules?

**A:** Yes! The architecture supports extensions:

```python
# Create utils/my_custom_utils.py
def my_function():
    """My custom function."""
    pass

# Import in your code
from utils.my_custom_utils import my_function
```

### Q: How do I use Python 101 functions in my own projects?

**A:** Several approaches:

**Option 1: Copy needed functions**
```python
# Copy specific functions to your project
from py101.utils.string_utils import clean_text

def my_project_function():
    text = clean_text(user_input)
    return text
```

**Option 2: Import the entire module**
```python
# Add py101 to your Python path
import sys
sys.path.append('/path/to/py-101')

from utils import string_utils, math_utils
```

**Option 3: Install as development package**
```bash
cd py-101
pip install -e .
```

---

Still have questions? **Create an issue** on GitHub and we'll help you out! 🐍✨

---

*Last updated: October 2024*
