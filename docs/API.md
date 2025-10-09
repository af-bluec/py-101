# API Documentation

## Python 101 - Function Reference

This document provides detailed API documentation for all functions available in the Python 101 project.

---

## Core Functions (main.py)

### factorial(n)
Calculates the factorial of a given number.

**Parameters:**
- `n` (int): Non-negative integer

**Returns:**
- `int`: Factorial of n

**Raises:**
- `ValueError`: If n is negative
- `TypeError`: If n is not an integer

**Example:**
```python
result = factorial(5)  # Returns 120
```

**Time Complexity:** O(n)

---

### is_prime(num)
Checks if a given number is prime.

**Parameters:**
- `num` (int): Number to check

**Returns:**
- `bool`: True if number is prime, False otherwise

**Example:**
```python
result = is_prime(17)  # Returns True
result = is_prime(4)   # Returns False
```

**Time Complexity:** O(√n)

---

### fibonacci_sequence(length)
Generates a Fibonacci sequence of specified length.

**Parameters:**
- `length` (int): Length of sequence to generate

**Returns:**
- `list`: List containing Fibonacci sequence

**Raises:**
- `ValueError`: If length is negative

**Example:**
```python
seq = fibonacci_sequence(5)  # Returns [0, 1, 1, 2, 3]
```

**Time Complexity:** O(n)

---

### greet(name)
Returns a personalized greeting message.

**Parameters:**
- `name` (str): Name to include in greeting

**Returns:**
- `str`: Formatted greeting message

**Example:**
```python
message = greet("Alice")  # Returns "Hello, Alice!"
```

---

## String Utilities (utils/string_utils.py)

### clean_text(text)
Removes leading and trailing whitespace and normalizes internal spacing.

**Parameters:**
- `text` (str): Text to clean

**Returns:**
- `str`: Cleaned text with normalized spacing

**Example:**
```python
clean = clean_text("  hello   world  ")  # Returns "hello world"
```

---

### is_palindrome(text, ignore_case=True, ignore_spaces=True)
Checks if text reads the same forwards and backwards.

**Parameters:**
- `text` (str): Text to check
- `ignore_case` (bool, optional): Whether to ignore case. Default: True
- `ignore_spaces` (bool, optional): Whether to ignore spaces. Default: True

**Returns:**
- `bool`: True if text is a palindrome, False otherwise

**Example:**
```python
result = is_palindrome("A man a plan a canal Panama")  # Returns True
```

---

### count_words(text)
Counts the number of words in a text string.

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- `int`: Number of words in the text

**Example:**
```python
count = count_words("Hello world")  # Returns 2
```

---

### capitalize_words(text)
Capitalizes the first letter of each word.

**Parameters:**
- `text` (str): Text to capitalize

**Returns:**
- `str`: Text with each word capitalized

**Example:**
```python
result = capitalize_words("hello world")  # Returns "Hello World"
```

---

### reverse_words(text)
Reverses the order of words in a string.

**Parameters:**
- `text` (str): Text with words to reverse

**Returns:**
- `str`: Text with words in reverse order

**Example:**
```python
result = reverse_words("hello world")  # Returns "world hello"
```

---

## Math Utilities (utils/math_utils.py)

### gcd(a, b)
Calculates the Greatest Common Divisor of two numbers.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- `int`: Greatest common divisor of a and b

**Example:**
```python
result = gcd(48, 18)  # Returns 6
```

**Time Complexity:** O(log(min(a, b)))

---

### lcm(a, b)
Calculates the Least Common Multiple of two numbers.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:**
- `int`: Least common multiple of a and b

**Example:**
```python
result = lcm(4, 6)  # Returns 12
```

---

### is_perfect_square(n)
Checks if a number is a perfect square.

**Parameters:**
- `n` (int): Number to check

**Returns:**
- `bool`: True if n is a perfect square, False otherwise

**Example:**
```python
result = is_perfect_square(16)  # Returns True
result = is_perfect_square(15)  # Returns False
```

---

### generate_primes(limit)
Generates all prime numbers up to a given limit using the Sieve of Eratosthenes.

**Parameters:**
- `limit` (int): Upper limit for prime generation

**Returns:**
- `list`: List of prime numbers up to limit

**Example:**
```python
primes = generate_primes(20)  # Returns [2, 3, 5, 7, 11, 13, 17, 19]
```

**Time Complexity:** O(n log log n)

---

### power(base, exponent)
Calculates base raised to the power of exponent.

**Parameters:**
- `base` (int/float): Base number
- `exponent` (int): Exponent

**Returns:**
- `int/float`: Result of base^exponent

**Example:**
```python
result = power(2, 3)  # Returns 8
```

---

## Data Structure Utilities (utils/data_structures.py)

### merge_dicts(dict1, dict2)
Merges two dictionaries, with dict2 values taking precedence.

**Parameters:**
- `dict1` (dict): First dictionary
- `dict2` (dict): Second dictionary

**Returns:**
- `dict`: Merged dictionary

**Example:**
```python
merged = merge_dicts({"a": 1}, {"b": 2})  # Returns {"a": 1, "b": 2}
```

---

### flatten_list(nested_list)
Flattens a nested list structure into a single-level list.

**Parameters:**
- `nested_list` (list): List containing nested lists

**Returns:**
- `list`: Flattened list

**Example:**
```python
flat = flatten_list([[1, 2], [3, 4]])  # Returns [1, 2, 3, 4]
```

---

### remove_duplicates(lst)
Removes duplicate elements from a list while preserving order.

**Parameters:**
- `lst` (list): List with potential duplicates

**Returns:**
- `list`: List with duplicates removed

**Example:**
```python
unique = remove_duplicates([1, 2, 2, 3, 1])  # Returns [1, 2, 3]
```

---

### group_by_key(lst, key)
Groups a list of dictionaries by a specified key.

**Parameters:**
- `lst` (list): List of dictionaries
- `key` (str): Key to group by

**Returns:**
- `dict`: Dictionary with grouped results

**Example:**
```python
data = [{"type": "A", "val": 1}, {"type": "B", "val": 2}, {"type": "A", "val": 3}]
grouped = group_by_key(data, "type")
# Returns {"A": [{"type": "A", "val": 1}, {"type": "A", "val": 3}], "B": [{"type": "B", "val": 2}]}
```

---

### sort_dict_by_value(dictionary, reverse=False)
Sorts a dictionary by its values.

**Parameters:**
- `dictionary` (dict): Dictionary to sort
- `reverse` (bool, optional): Sort in descending order. Default: False

**Returns:**
- `dict`: Dictionary sorted by values

**Example:**
```python
sorted_dict = sort_dict_by_value({"a": 3, "b": 1, "c": 2})
# Returns {"b": 1, "c": 2, "a": 3}
```

---

## File Utilities (utils/file_utils.py)

### read_file(filepath)
Reads content from a file.

**Parameters:**
- `filepath` (str): Path to the file

**Returns:**
- `str`: File content

**Raises:**
- `FileNotFoundError`: If file doesn't exist
- `IOError`: If file cannot be read

**Example:**
```python
content = read_file("data.txt")
```

---

### write_file(filepath, content, mode='w')
Writes content to a file.

**Parameters:**
- `filepath` (str): Path to the file
- `content` (str): Content to write
- `mode` (str, optional): Write mode ('w' or 'a'). Default: 'w'

**Returns:**
- `bool`: True if successful

**Example:**
```python
success = write_file("output.txt", "Hello World!")
```

---

### file_exists(filepath)
Checks if a file exists.

**Parameters:**
- `filepath` (str): Path to check

**Returns:**
- `bool`: True if file exists, False otherwise

**Example:**
```python
exists = file_exists("data.txt")
```

---

## Validators (utils/validators.py)

### validate_email(email)
Validates email address format.

**Parameters:**
- `email` (str): Email address to validate

**Returns:**
- `bool`: True if valid email format, False otherwise

**Example:**
```python
is_valid = validate_email("user@example.com")  # Returns True
```

---

### validate_phone(phone)
Validates phone number format.

**Parameters:**
- `phone` (str): Phone number to validate

**Returns:**
- `bool`: True if valid phone format, False otherwise

**Example:**
```python
is_valid = validate_phone("123-456-7890")  # Returns True
```

---

### is_positive_integer(value)
Checks if a value is a positive integer.

**Parameters:**
- `value` (any): Value to check

**Returns:**
- `bool`: True if positive integer, False otherwise

**Example:**
```python
is_pos = is_positive_integer(5)    # Returns True
is_pos = is_positive_integer(-1)   # Returns False
is_pos = is_positive_integer("5")  # Returns False
```

---

## Error Handling

Most functions include proper error handling and will raise appropriate exceptions:

- **ValueError**: For invalid input values
- **TypeError**: For incorrect data types
- **FileNotFoundError**: For missing files
- **IOError**: For file operation errors

Always handle exceptions appropriately in your code:

```python
try:
    result = factorial(-1)
except ValueError as e:
    print(f"Error: {e}")
```

---

## Performance Notes

- **Prime Generation**: Uses Sieve of Eratosthenes for optimal performance
- **String Operations**: Most are O(n) complexity
- **List Operations**: Flattening and deduplication preserve order efficiently
- **Math Operations**: GCD uses Euclidean algorithm for optimal performance

---

## Version Compatibility

All functions are compatible with Python 3.6+ and use only standard library modules.
