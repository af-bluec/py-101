# Function Reference

## Python 101 - Complete Function Reference

This document provides a comprehensive reference of all functions available in Python 101, organized by module and functionality.

---

## Quick Reference

### Function Index by Category

| Category | Functions |
|----------|-----------|
| **Core** | `factorial`, `is_prime`, `fibonacci_sequence`, `greet` |
| **String** | `clean_text`, `is_palindrome`, `count_words`, `capitalize_words`, `reverse_words` |
| **Math** | `gcd`, `lcm`, `is_perfect_square`, `generate_primes`, `power` |
| **Data** | `merge_dicts`, `flatten_list`, `remove_duplicates`, `group_by_key`, `sort_dict_by_value` |
| **File** | `read_file`, `write_file`, `file_exists` |
| **Validation** | `validate_email`, `validate_phone`, `is_positive_integer` |

### Function Index by Complexity

| Beginner | Intermediate | Advanced |
|----------|--------------|----------|
| `greet` | `factorial` | `generate_primes` |
| `clean_text` | `is_prime` | `group_by_key` |
| `count_words` | `fibonacci_sequence` | `sieve_of_eratosthenes` |
| `file_exists` | `flatten_list` | `text_similarity` |
| `is_positive_integer` | `merge_dicts` | `advanced_validation` |

---

## Core Functions (main.py)

### factorial(n)
```python
def factorial(n: int) -> int
```

**Purpose:** Calculate the factorial of a non-negative integer.

**Parameters:**
- `n` (int): Non-negative integer to calculate factorial for

**Returns:**
- `int`: Factorial of n (n!)

**Raises:**
- `TypeError`: If n is not an integer
- `ValueError`: If n is negative

**Algorithm:** Iterative multiplication from 1 to n.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Examples:**
```python
factorial(0)  # Returns: 1
factorial(5)  # Returns: 120
factorial(10) # Returns: 3628800
```

**Educational Value:** Demonstrates basic loops, input validation, and mathematical computation.

---

### is_prime(num)
```python
def is_prime(num: int) -> bool
```

**Purpose:** Determine if a number is prime (only divisible by 1 and itself).

**Parameters:**
- `num` (int): Number to test for primality

**Returns:**
- `bool`: True if prime, False otherwise

**Algorithm:** Tests divisibility up to √num for efficiency.

**Time Complexity:** O(√n)  
**Space Complexity:** O(1)

**Examples:**
```python
is_prime(2)   # Returns: True
is_prime(17)  # Returns: True
is_prime(4)   # Returns: False
is_prime(100) # Returns: False
```

**Special Cases:**
- Numbers ≤ 1 return False
- 2 is the only even prime number
- Optimized to check only odd divisors

**Educational Value:** Shows algorithm optimization and mathematical reasoning.

---

### fibonacci_sequence(length)
```python
def fibonacci_sequence(length: int) -> List[int]
```

**Purpose:** Generate the Fibonacci sequence of specified length.

**Parameters:**
- `length` (int): Number of Fibonacci numbers to generate

**Returns:**
- `List[int]`: List containing first `length` Fibonacci numbers

**Raises:**
- `ValueError`: If length is negative

**Algorithm:** Iterative generation using two variables.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**Examples:**
```python
fibonacci_sequence(0)  # Returns: []
fibonacci_sequence(1)  # Returns: [0]
fibonacci_sequence(5)  # Returns: [0, 1, 1, 2, 3]
fibonacci_sequence(10) # Returns: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Educational Value:** Demonstrates sequences, iteration, and list building.

---

### greet(name)
```python
def greet(name: str) -> str
```

**Purpose:** Generate a personalized greeting message.

**Parameters:**
- `name` (str): Name to include in greeting

**Returns:**
- `str`: Formatted greeting string

**Examples:**
```python
greet("Alice")  # Returns: "Hello, Alice!"
greet("Python") # Returns: "Hello, Python!"
```

**Educational Value:** Basic function structure and string formatting.

---

## String Utilities (utils/string_utils.py)

### clean_text(text)
```python
def clean_text(text: str) -> str
```

**Purpose:** Remove leading/trailing whitespace and normalize internal spacing.

**Parameters:**
- `text` (str): Text to clean

**Returns:**
- `str`: Cleaned text with normalized whitespace

**Algorithm:** Uses strip() and regex replacement for multiple spaces.

**Examples:**
```python
clean_text("  hello   world  ")  # Returns: "hello world"
clean_text("python\t\nis\n\nawesome")  # Returns: "python is awesome"
```

**Use Cases:**
- Data preprocessing
- User input sanitization
- Text normalization

---

### is_palindrome(text, ignore_case=True, ignore_spaces=True)
```python
def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool
```

**Purpose:** Check if text reads the same forwards and backwards.

**Parameters:**
- `text` (str): Text to check
- `ignore_case` (bool): Whether to ignore case differences
- `ignore_spaces` (bool): Whether to ignore spaces and punctuation

**Returns:**
- `bool`: True if palindrome, False otherwise

**Examples:**
```python
is_palindrome("racecar")           # Returns: True
is_palindrome("A man a plan a canal Panama")  # Returns: True
is_palindrome("hello")             # Returns: False
is_palindrome("Racecar", ignore_case=False)  # Returns: False
```

**Algorithm:** Normalizes text based on options, then compares with reverse.

---

### count_words(text)
```python
def count_words(text: str) -> int
```

**Purpose:** Count the number of words in text.

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- `int`: Number of words found

**Algorithm:** Splits on whitespace and counts non-empty parts.

**Examples:**
```python
count_words("hello world")     # Returns: 2
count_words("Python is awesome!")  # Returns: 3
count_words("")               # Returns: 0
count_words("   ")            # Returns: 0
```

---

### capitalize_words(text)
```python
def capitalize_words(text: str) -> str
```

**Purpose:** Capitalize the first letter of each word.

**Parameters:**
- `text` (str): Text to capitalize

**Returns:**
- `str`: Text with each word capitalized

**Examples:**
```python
capitalize_words("hello world")    # Returns: "Hello World"
capitalize_words("python programming")  # Returns: "Python Programming"
```

---

### reverse_words(text)
```python
def reverse_words(text: str) -> str
```

**Purpose:** Reverse the order of words in text.

**Parameters:**
- `text` (str): Text with words to reverse

**Returns:**
- `str`: Text with words in reverse order

**Examples:**
```python
reverse_words("hello world")       # Returns: "world hello"
reverse_words("Python is awesome") # Returns: "awesome is Python"
```

---

## Math Utilities (utils/math_utils.py)

### gcd(a, b)
```python
def gcd(a: int, b: int) -> int
```

**Purpose:** Calculate Greatest Common Divisor using Euclidean algorithm.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- `int`: Greatest common divisor of a and b

**Algorithm:** Euclidean algorithm with recursive approach.

**Time Complexity:** O(log(min(a, b)))

**Examples:**
```python
gcd(48, 18)  # Returns: 6
gcd(100, 75) # Returns: 25
gcd(17, 13)  # Returns: 1
```

---

### lcm(a, b)
```python
def lcm(a: int, b: int) -> int
```

**Purpose:** Calculate Least Common Multiple.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- `int`: Least common multiple of a and b

**Algorithm:** Uses relationship LCM(a,b) = (a*b)/GCD(a,b)

**Examples:**
```python
lcm(4, 6)    # Returns: 12
lcm(12, 15)  # Returns: 60
```

---

### is_perfect_square(n)
```python
def is_perfect_square(n: int) -> bool
```

**Purpose:** Check if a number is a perfect square.

**Parameters:**
- `n` (int): Number to test

**Returns:**
- `bool`: True if n is a perfect square

**Algorithm:** Uses integer square root and verification.

**Examples:**
```python
is_perfect_square(16)  # Returns: True
is_perfect_square(15)  # Returns: False
is_perfect_square(0)   # Returns: True
```

---

### generate_primes(limit)
```python
def generate_primes(limit: int) -> List[int]
```

**Purpose:** Generate all prime numbers up to limit using Sieve of Eratosthenes.

**Parameters:**
- `limit` (int): Upper bound for prime generation

**Returns:**
- `List[int]`: List of prime numbers ≤ limit

**Algorithm:** Sieve of Eratosthenes - most efficient for generating multiple primes.

**Time Complexity:** O(n log log n)  
**Space Complexity:** O(n)

**Examples:**
```python
generate_primes(10)  # Returns: [2, 3, 5, 7]
generate_primes(20)  # Returns: [2, 3, 5, 7, 11, 13, 17, 19]
```

**Educational Value:** Demonstrates advanced algorithms and optimization techniques.

---

### power(base, exponent)
```python
def power(base: Union[int, float], exponent: int) -> Union[int, float]
```

**Purpose:** Calculate base raised to the power of exponent.

**Parameters:**
- `base` (int/float): Base number
- `exponent` (int): Exponent (power)

**Returns:**
- `int/float`: Result of base^exponent

**Examples:**
```python
power(2, 3)   # Returns: 8
power(5, 0)   # Returns: 1
power(3, 4)   # Returns: 81
```

---

## Data Structure Utilities (utils/data_structures.py)

### merge_dicts(dict1, dict2)
```python
def merge_dicts(dict1: dict, dict2: dict) -> dict
```

**Purpose:** Merge two dictionaries, with dict2 values taking precedence.

**Parameters:**
- `dict1` (dict): First dictionary
- `dict2` (dict): Second dictionary (overrides conflicts)

**Returns:**
- `dict`: Merged dictionary

**Examples:**
```python
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
# Returns: {"a": 1, "b": 3, "c": 4}
```

---

### flatten_list(nested_list)
```python
def flatten_list(nested_list: List[List]) -> List
```

**Purpose:** Flatten a nested list structure into a single-level list.

**Parameters:**
- `nested_list` (List[List]): Nested list structure

**Returns:**
- `List`: Flattened single-level list

**Algorithm:** Recursive flattening with type checking.

**Examples:**
```python
flatten_list([[1, 2], [3, 4], [5]])
# Returns: [1, 2, 3, 4, 5]

flatten_list([[[1, 2]], [[3, 4]]])
# Returns: [1, 2, 3, 4]
```

---

### remove_duplicates(lst)
```python
def remove_duplicates(lst: List) -> List
```

**Purpose:** Remove duplicate elements while preserving order.

**Parameters:**
- `lst` (List): List potentially containing duplicates

**Returns:**
- `List`: List with duplicates removed, order preserved

**Algorithm:** Uses set for tracking seen items, preserves first occurrence.

**Examples:**
```python
remove_duplicates([1, 2, 2, 3, 1, 4])
# Returns: [1, 2, 3, 4]

remove_duplicates(['a', 'b', 'a', 'c'])
# Returns: ['a', 'b', 'c']
```

---

### group_by_key(lst, key)
```python
def group_by_key(lst: List[dict], key: str) -> Dict[str, List[dict]]
```

**Purpose:** Group a list of dictionaries by a specified key.

**Parameters:**
- `lst` (List[dict]): List of dictionaries
- `key` (str): Key to group by

**Returns:**
- `Dict[str, List[dict]]`: Dictionary with grouped results

**Examples:**
```python
data = [
    {"type": "A", "value": 1},
    {"type": "B", "value": 2}, 
    {"type": "A", "value": 3}
]
group_by_key(data, "type")
# Returns: {
#     "A": [{"type": "A", "value": 1}, {"type": "A", "value": 3}],
#     "B": [{"type": "B", "value": 2}]
# }
```

---

### sort_dict_by_value(dictionary, reverse=False)
```python
def sort_dict_by_value(dictionary: dict, reverse: bool = False) -> dict
```

**Purpose:** Sort dictionary by its values.

**Parameters:**
- `dictionary` (dict): Dictionary to sort
- `reverse` (bool): Sort in descending order if True

**Returns:**
- `dict`: New dictionary sorted by values

**Examples:**
```python
sort_dict_by_value({"a": 3, "b": 1, "c": 2})
# Returns: {"b": 1, "c": 2, "a": 3}

sort_dict_by_value({"a": 3, "b": 1, "c": 2}, reverse=True)
# Returns: {"a": 3, "c": 2, "b": 1}
```

---

## File Utilities (utils/file_utils.py)

### read_file(filepath)
```python
def read_file(filepath: str) -> str
```

**Purpose:** Read and return the contents of a file.

**Parameters:**
- `filepath` (str): Path to the file to read

**Returns:**
- `str`: Contents of the file

**Raises:**
- `FileNotFoundError`: If file doesn't exist
- `IOError`: If file cannot be read

**Examples:**
```python
content = read_file("data.txt")
lines = read_file("config.ini").split('\n')
```

---

### write_file(filepath, content, mode='w')
```python
def write_file(filepath: str, content: str, mode: str = 'w') -> bool
```

**Purpose:** Write content to a file.

**Parameters:**
- `filepath` (str): Path to the file to write
- `content` (str): Content to write to file
- `mode` (str): Write mode ('w' for write, 'a' for append)

**Returns:**
- `bool`: True if successful, False otherwise

**Examples:**
```python
write_file("output.txt", "Hello, World!")
write_file("log.txt", "New entry\n", mode='a')
```

---

### file_exists(filepath)
```python
def file_exists(filepath: str) -> bool
```

**Purpose:** Check if a file exists.

**Parameters:**
- `filepath` (str): Path to check

**Returns:**
- `bool`: True if file exists, False otherwise

**Examples:**
```python
if file_exists("config.txt"):
    config = read_file("config.txt")
else:
    config = "default config"
```

---

## Validation Utilities (utils/validators.py)

### validate_email(email)
```python
def validate_email(email: str) -> bool
```

**Purpose:** Validate email address format using regex.

**Parameters:**
- `email` (str): Email address to validate

**Returns:**
- `bool`: True if valid email format

**Algorithm:** Uses regex pattern for basic email validation.

**Examples:**
```python
validate_email("user@example.com")     # Returns: True
validate_email("invalid-email")        # Returns: False
validate_email("user.name@domain.org") # Returns: True
```

**Note:** This is basic format validation, not deliverability checking.

---

### validate_phone(phone)
```python
def validate_phone(phone: str) -> bool
```

**Purpose:** Validate phone number format.

**Parameters:**
- `phone` (str): Phone number to validate

**Returns:**
- `bool`: True if valid phone format

**Supported Formats:**
- `123-456-7890`
- `(123) 456-7890`
- `1234567890`
- `123.456.7890`

**Examples:**
```python
validate_phone("123-456-7890")   # Returns: True
validate_phone("(555) 123-4567") # Returns: True
validate_phone("invalid")        # Returns: False
```

---

### is_positive_integer(value)
```python
def is_positive_integer(value) -> bool
```

**Purpose:** Check if value is a positive integer.

**Parameters:**
- `value` (Any): Value to check

**Returns:**
- `bool`: True if positive integer

**Examples:**
```python
is_positive_integer(5)      # Returns: True
is_positive_integer(0)      # Returns: False
is_positive_integer(-1)     # Returns: False
is_positive_integer("5")    # Returns: False
is_positive_integer(3.14)   # Returns: False
```

---

## Usage Patterns

### Function Chaining
```python
# Combine multiple string operations
from utils.string_utils import clean_text, capitalize_words, count_words

def process_text(raw_text):
    cleaned = clean_text(raw_text)
    capitalized = capitalize_words(cleaned)
    word_count = count_words(capitalized)
    return capitalized, word_count

result, count = process_text("  hello python world  ")
# result: "Hello Python World", count: 3
```

### Data Processing Pipeline
```python
# Process and analyze data
from utils.data_structures import flatten_list, remove_duplicates, group_by_key

def analyze_data(nested_data):
    # Flatten the structure
    flat_data = flatten_list(nested_data)
    
    # Remove duplicates
    unique_data = remove_duplicates(flat_data)
    
    # Group by some criteria
    if isinstance(unique_data[0], dict):
        grouped = group_by_key(unique_data, 'category')
        return grouped
    
    return unique_data
```

### Mathematical Operations
```python
# Mathematical analysis
from utils.math_utils import gcd, lcm, generate_primes, is_perfect_square

def number_analysis(numbers):
    results = {}
    
    # Find GCD and LCM of first two numbers
    if len(numbers) >= 2:
        results['gcd'] = gcd(numbers[0], numbers[1])
        results['lcm'] = lcm(numbers[0], numbers[1])
    
    # Find perfect squares
    results['perfect_squares'] = [n for n in numbers if is_perfect_square(n)]
    
    # Generate primes up to max number
    if numbers:
        max_num = max(numbers)
        results['primes_in_range'] = generate_primes(max_num)
    
    return results
```

---

## Performance Guidelines

### Function Complexity Reference

| Function | Time Complexity | Space Complexity | Best Use Case |
|----------|----------------|------------------|---------------|
| `factorial` | O(n) | O(1) | Small to medium n |
| `is_prime` | O(√n) | O(1) | Individual prime checks |
| `generate_primes` | O(n log log n) | O(n) | Multiple primes needed |
| `fibonacci_sequence` | O(n) | O(n) | Sequence generation |
| `gcd` | O(log min(a,b)) | O(1) | Any size numbers |
| `flatten_list` | O(n) | O(n) | Nested list processing |
| `group_by_key` | O(n) | O(n) | Data organization |

### Memory Usage Tips

**For Large Data:**
```python
# Use generators when possible
def fibonacci_generator(max_count):
    """Memory-efficient Fibonacci generation."""
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1

# Process files line by line
def process_large_file(filename):
    """Memory-efficient file processing."""
    with open(filename) as f:
        for line in f:  # Don't load entire file
            yield process_line(line)
```

---

## Error Handling Patterns

### Input Validation
```python
def safe_function_call():
    """Demonstrate safe function usage."""
    try:
        # Validate before calling
        if not isinstance(input_val, int):
            raise TypeError("Expected integer")
        
        result = factorial(input_val)
        return result
        
    except (TypeError, ValueError) as e:
        print(f"Input error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### Robust Processing
```python
def robust_text_processing(texts):
    """Process multiple texts with error handling."""
    results = []
    errors = []
    
    for i, text in enumerate(texts):
        try:
            # Multiple operations with error handling
            cleaned = clean_text(text) if isinstance(text, str) else str(text)
            word_count = count_words(cleaned)
            is_palin = is_palindrome(cleaned)
            
            results.append({
                'index': i,
                'cleaned_text': cleaned,
                'word_count': word_count,
                'is_palindrome': is_palin
            })
            
        except Exception as e:
            errors.append({'index': i, 'error': str(e), 'input': text})
    
    return results, errors
```

---

This comprehensive function reference provides all the details needed to effectively use Python 101's functions in your projects and learning endeavors.

**Happy coding! 🐍📚**

---

*Last updated: October 2024*
