# Usage Examples

## Python 101 - Comprehensive Usage Examples

This document provides detailed examples of how to use all the functions and utilities in the Python 101 project.

---

## Getting Started

### Running the Main Demonstration

```bash
python main.py
```

This will show you a complete demonstration of all available functions.

### Importing Specific Modules

```python
# Import individual utility modules
from utils import string_utils, math_utils, data_structures, file_utils, validators

# Import specific functions
from utils.string_utils import clean_text, is_palindrome
from utils.math_utils import gcd, generate_primes
from utils.data_structures import flatten_list, merge_dicts
```

---

## Core Functions Examples

### Mathematical Operations

#### Factorial Calculation

```python
from main import factorial

# Basic usage
result = factorial(5)
print(f"5! = {result}")  # Output: 5! = 120

# Larger numbers
result = factorial(10)
print(f"10! = {result}")  # Output: 10! = 3628800

# Error handling
try:
    factorial(-1)
except ValueError as e:
    print(f"Error: {e}")  # Error: Factorial is not defined for negative numbers
```

#### Prime Number Checking

```python
from main import is_prime

# Check various numbers
numbers = [2, 3, 4, 17, 25, 29, 100]
for num in numbers:
    result = is_prime(num)
    print(f"{num} is {'prime' if result else 'not prime'}")

# Output:
# 2 is prime
# 3 is prime  
# 4 is not prime
# 17 is prime
# 25 is not prime
# 29 is prime
# 100 is not prime
```

#### Fibonacci Sequence Generation

```python
from main import fibonacci_sequence

# Generate different length sequences
sequences = [5, 10, 15]
for length in sequences:
    seq = fibonacci_sequence(length)
    print(f"Fibonacci({length}): {seq}")

# Output:
# Fibonacci(5): [0, 1, 1, 2, 3]
# Fibonacci(10): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Fibonacci(15): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

---

## String Utilities Examples

### Text Cleaning and Formatting

```python
from utils.string_utils import clean_text, capitalize_words, reverse_words

# Text cleaning
messy_text = "  hello    world   python  "
clean = clean_text(messy_text)
print(f"Original: '{messy_text}'")
print(f"Cleaned:  '{clean}'")
# Output:
# Original: '  hello    world   python  '
# Cleaned:  'hello world python'

# Word capitalization
text = "python is awesome"
capitalized = capitalize_words(text)
print(f"Original: {text}")
print(f"Capitalized: {capitalized}")
# Output:
# Original: python is awesome
# Capitalized: Python Is Awesome

# Word reversal
original = "Hello World Python"
reversed_words = reverse_words(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_words}")
# Output:
# Original: Hello World Python
# Reversed: Python World Hello
```

### Palindrome Detection

```python
from utils.string_utils import is_palindrome

# Test various palindromes
test_cases = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "hello",
    "Madam",
    "12321"
]

for text in test_cases:
    result = is_palindrome(text)
    print(f"'{text}' is {'a palindrome' if result else 'not a palindrome'}")

# Output:
# 'racecar' is a palindrome
# 'A man a plan a canal Panama' is a palindrome
# 'race a car' is not a palindrome
# 'hello' is not a palindrome
# 'Madam' is a palindrome
# '12321' is a palindrome
```

### Word Analysis

```python
from utils.string_utils import count_words

# Analyze different texts
texts = [
    "Hello world",
    "Python is a powerful programming language",
    "One",
    "",
    "  Multiple   spaces   between   words  "
]

for text in texts:
    count = count_words(text)
    print(f"'{text}' contains {count} words")

# Output:
# 'Hello world' contains 2 words
# 'Python is a powerful programming language' contains 6 words
# 'One' contains 1 words
# '' contains 0 words
# '  Multiple   spaces   between   words  ' contains 4 words
```

---

## Math Utilities Examples

### Greatest Common Divisor and Least Common Multiple

```python
from utils.math_utils import gcd, lcm

# Calculate GCD and LCM for various pairs
number_pairs = [(48, 18), (100, 75), (17, 13), (24, 36)]

for a, b in number_pairs:
    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)
    print(f"Numbers: {a}, {b}")
    print(f"GCD: {gcd_result}")
    print(f"LCM: {lcm_result}")
    print(f"Verification: {a * b} = {gcd_result * lcm_result}")
    print("-" * 30)

# Output:
# Numbers: 48, 18
# GCD: 6
# LCM: 144
# Verification: 864 = 864
# ------------------------------
# Numbers: 100, 75
# GCD: 25
# LCM: 300
# Verification: 7500 = 7500
# ------------------------------
```

### Perfect Square Detection

```python
from utils.math_utils import is_perfect_square

# Test numbers for perfect squares
test_numbers = [1, 4, 8, 9, 15, 16, 25, 30, 36, 50, 64, 100]

perfect_squares = []
non_perfect_squares = []

for num in test_numbers:
    if is_perfect_square(num):
        perfect_squares.append(num)
    else:
        non_perfect_squares.append(num)

print(f"Perfect squares: {perfect_squares}")
print(f"Non-perfect squares: {non_perfect_squares}")

# Output:
# Perfect squares: [1, 4, 9, 16, 25, 36, 64, 100]
# Non-perfect squares: [8, 15, 30, 50]
```

### Prime Number Generation

```python
from utils.math_utils import generate_primes

# Generate primes for different limits
limits = [10, 30, 50, 100]

for limit in limits:
    primes = generate_primes(limit)
    print(f"Primes up to {limit}: {primes}")
    print(f"Count: {len(primes)}")
    print("-" * 40)

# Output:
# Primes up to 10: [2, 3, 5, 7]
# Count: 4
# ----------------------------------------
# Primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Count: 10
# ----------------------------------------
```

### Power Calculations

```python
from utils.math_utils import power

# Calculate various powers
calculations = [
    (2, 3),    # 2^3
    (5, 2),    # 5^2
    (3, 4),    # 3^4
    (10, 0),   # 10^0
    (7, 1),    # 7^1
]

for base, exponent in calculations:
    result = power(base, exponent)
    print(f"{base}^{exponent} = {result}")

# Output:
# 2^3 = 8
# 5^2 = 25
# 3^4 = 81
# 10^0 = 1
# 7^1 = 7
```

---

## Data Structure Examples

### Dictionary Operations

```python
from utils.data_structures import merge_dicts, sort_dict_by_value

# Dictionary merging
dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "age": 31}  # age will be overridden
dict3 = {"country": "USA", "occupation": "Engineer"}

# Merge two dictionaries
merged = merge_dicts(dict1, dict2)
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Merged: {merged}")

# Chain merge multiple dictionaries
final = merge_dicts(merged, dict3)
print(f"Final: {final}")

# Output:
# Dict1: {'name': 'Alice', 'age': 30}
# Dict2: {'city': 'New York', 'age': 31}
# Merged: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# Final: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}

# Dictionary sorting by value
scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 98, "Eve": 89}
sorted_asc = sort_dict_by_value(scores)
sorted_desc = sort_dict_by_value(scores, reverse=True)

print(f"Original: {scores}")
print(f"Ascending: {sorted_asc}")
print(f"Descending: {sorted_desc}")

# Output:
# Original: {'Alice': 95, 'Bob': 87, 'Charlie': 92, 'Diana': 98, 'Eve': 89}
# Ascending: {'Bob': 87, 'Eve': 89, 'Charlie': 92, 'Alice': 95, 'Diana': 98}
# Descending: {'Diana': 98, 'Alice': 95, 'Charlie': 92, 'Eve': 89, 'Bob': 87}
```

### List Operations

```python
from utils.data_structures import flatten_list, remove_duplicates

# List flattening
nested_lists = [
    [[1, 2], [3, 4]],
    [[1, 2, 3], [4, 5], [6]],
    [[[1, 2]], [[3, 4]], [[5]]],
    []
]

for nested in nested_lists:
    flat = flatten_list(nested)
    print(f"Nested: {nested}")
    print(f"Flattened: {flat}")
    print("-" * 30)

# Output:
# Nested: [[1, 2], [3, 4]]
# Flattened: [1, 2, 3, 4]
# ------------------------------
# Nested: [[1, 2, 3], [4, 5], [6]]
# Flattened: [1, 2, 3, 4, 5, 6]
# ------------------------------

# Duplicate removal (preserving order)
lists_with_dupes = [
    [1, 2, 2, 3, 1, 4, 3],
    ["a", "b", "a", "c", "b", "d"],
    [1, 1, 1, 1],
    []
]

for lst in lists_with_dupes:
    unique = remove_duplicates(lst)
    print(f"Original: {lst}")
    print(f"Unique: {unique}")
    print("-" * 30)

# Output:
# Original: [1, 2, 2, 3, 1, 4, 3]
# Unique: [1, 2, 3, 4]
# ------------------------------
# Original: ['a', 'b', 'a', 'c', 'b', 'd']
# Unique: ['a', 'b', 'c', 'd']
# ------------------------------
```

### Data Grouping

```python
from utils.data_structures import group_by_key

# Sample data - list of dictionaries
employees = [
    {"name": "Alice", "department": "Engineering", "salary": 90000},
    {"name": "Bob", "department": "Marketing", "salary": 70000},
    {"name": "Charlie", "department": "Engineering", "salary": 85000},
    {"name": "Diana", "department": "HR", "salary": 65000},
    {"name": "Eve", "department": "Marketing", "salary": 72000},
    {"name": "Frank", "department": "Engineering", "salary": 95000}
]

# Group by department
by_department = group_by_key(employees, "department")

print("Employees grouped by department:")
for dept, emp_list in by_department.items():
    print(f"\n{dept}:")
    for emp in emp_list:
        print(f"  - {emp['name']}: ${emp['salary']:,}")

# Output:
# Employees grouped by department:
# 
# Engineering:
#   - Alice: $90,000
#   - Charlie: $85,000
#   - Frank: $95,000
# 
# Marketing:
#   - Bob: $70,000
#   - Eve: $72,000
# 
# HR:
#   - Diana: $65,000
```

---

## File Operations Examples

### Basic File Operations

```python
from utils.file_utils import write_file, read_file, file_exists

# Write content to files
content1 = "Hello, World!\nThis is a test file."
content2 = "Python is awesome!\nFile handling made easy."

# Write files
write_file("test1.txt", content1)
write_file("test2.txt", content2)

# Check if files exist
files = ["test1.txt", "test2.txt", "nonexistent.txt"]
for filename in files:
    exists = file_exists(filename)
    print(f"{filename}: {'exists' if exists else 'does not exist'}")

# Output:
# test1.txt: exists
# test2.txt: exists
# nonexistent.txt: does not exist

# Read file contents
if file_exists("test1.txt"):
    content = read_file("test1.txt")
    print(f"Content of test1.txt:\n{content}")

# Output:
# Content of test1.txt:
# Hello, World!
# This is a test file.

# Append to existing file
additional_content = "\nThis line was appended."
write_file("test1.txt", additional_content, mode='a')

updated_content = read_file("test1.txt")
print(f"Updated content:\n{updated_content}")

# Output:
# Updated content:
# Hello, World!
# This is a test file.
# This line was appended.
```

### File Processing Pipeline

```python
from utils.file_utils import write_file, read_file
from utils.string_utils import clean_text, count_words, capitalize_words

# Create a text processing pipeline
original_text = """
  this is a sample text file.
  it contains multiple lines with   extra spaces.
  we will process this text using our utilities.
"""

# Step 1: Write original text to file
write_file("original.txt", original_text)

# Step 2: Read and process the text
raw_content = read_file("original.txt")
print("Original content:")
print(repr(raw_content))

# Step 3: Clean the text
cleaned_lines = []
for line in raw_content.split('\n'):
    cleaned_line = clean_text(line)
    if cleaned_line:  # Skip empty lines
        cleaned_lines.append(cleaned_line)

cleaned_text = '\n'.join(cleaned_lines)
print("\nCleaned content:")
print(cleaned_text)

# Step 4: Capitalize words
capitalized_text = capitalize_words(cleaned_text)
print("\nCapitalized content:")
print(capitalized_text)

# Step 5: Analyze text
word_count = count_words(cleaned_text)
print(f"\nText analysis:")
print(f"Total words: {word_count}")
print(f"Total lines: {len(cleaned_lines)}")

# Step 6: Save processed text
write_file("processed.txt", capitalized_text)
print("\nProcessed text saved to 'processed.txt'")
```

---

## Validation Examples

### Email and Phone Validation

```python
from utils.validators import validate_email, validate_phone, is_positive_integer

# Test email addresses
emails = [
    "user@example.com",
    "valid.email@domain.org",
    "invalid-email",
    "user@",
    "@domain.com",
    "user.name+tag@example.co.uk"
]

print("Email validation results:")
for email in emails:
    is_valid = validate_email(email)
    print(f"{email}: {'✓ Valid' if is_valid else '✗ Invalid'}")

# Output:
# user@example.com: ✓ Valid
# valid.email@domain.org: ✓ Valid
# invalid-email: ✗ Invalid
# user@: ✗ Invalid
# @domain.com: ✗ Invalid
# user.name+tag@example.co.uk: ✓ Valid

# Test phone numbers
phones = [
    "123-456-7890",
    "(123) 456-7890",
    "1234567890",
    "123.456.7890",
    "invalid-phone",
    "123-45-6789"  # Too short
]

print("\nPhone validation results:")
for phone in phones:
    is_valid = validate_phone(phone)
    print(f"{phone}: {'✓ Valid' if is_valid else '✗ Invalid'}")

# Output:
# 123-456-7890: ✓ Valid
# (123) 456-7890: ✓ Valid
# 1234567890: ✓ Valid
# 123.456.7890: ✓ Valid
# invalid-phone: ✗ Invalid
# 123-45-6789: ✗ Invalid
```

### Number Validation

```python
from utils.validators import is_positive_integer

# Test various values
test_values = [5, -1, 0, 3.14, "5", "hello", None, True, False]

print("Positive integer validation:")
for value in test_values:
    is_valid = is_positive_integer(value)
    print(f"{repr(value)} ({type(value).__name__}): {'✓ Valid' if is_valid else '✗ Invalid'}")

# Output:
# 5 (int): ✓ Valid
# -1 (int): ✗ Invalid
# 0 (int): ✗ Invalid
# 3.14 (float): ✗ Invalid
# '5' (str): ✗ Invalid
# 'hello' (str): ✗ Invalid
# None (NoneType): ✗ Invalid
# True (bool): ✗ Invalid
# False (bool): ✗ Invalid
```

---

## Complex Examples

### Data Analysis Pipeline

```python
from utils.string_utils import clean_text, count_words
from utils.math_utils import generate_primes
from utils.data_structures import group_by_key, sort_dict_by_value
from utils.file_utils import write_file

# Sample data - article analysis
articles = [
    {
        "title": "Python Programming Basics",
        "content": "  Python is a powerful programming language. It's easy to learn and versatile.  ",
        "category": "Programming",
        "author": "Alice"
    },
    {
        "title": "Data Science with Python",
        "content": "  Data science involves analyzing data to extract insights. Python is perfect for this.  ",
        "category": "Data Science", 
        "author": "Bob"
    },
    {
        "title": "Web Development",
        "content": "  Building web applications is fun. Python frameworks make it easier.  ",
        "category": "Programming",
        "author": "Alice"
    }
]

# Process articles
processed_articles = []
for article in articles:
    # Clean content
    cleaned_content = clean_text(article["content"])
    
    # Count words
    word_count = count_words(cleaned_content)
    
    # Create processed article
    processed = {
        **article,
        "cleaned_content": cleaned_content,
        "word_count": word_count
    }
    processed_articles.append(processed)

# Group by category
by_category = group_by_key(processed_articles, "category")

# Group by author
by_author = group_by_key(processed_articles, "author")

# Calculate statistics
category_stats = {}
for category, articles_list in by_category.items():
    total_words = sum(article["word_count"] for article in articles_list)
    category_stats[category] = {
        "article_count": len(articles_list),
        "total_words": total_words,
        "average_words": total_words / len(articles_list)
    }

# Sort categories by total words
sorted_categories = sort_dict_by_value(
    {cat: stats["total_words"] for cat, stats in category_stats.items()},
    reverse=True
)

# Generate report
report = "Article Analysis Report\n"
report += "=" * 25 + "\n\n"

report += "Category Statistics:\n"
for category in sorted_categories.keys():
    stats = category_stats[category]
    report += f"  {category}:\n"
    report += f"    Articles: {stats['article_count']}\n"
    report += f"    Total Words: {stats['total_words']}\n"
    report += f"    Average Words: {stats['average_words']:.1f}\n\n"

report += "Author Summary:\n"
for author, articles_list in by_author.items():
    article_count = len(articles_list)
    total_words = sum(article["word_count"] for article in articles_list)
    report += f"  {author}: {article_count} articles, {total_words} words\n"

# Save report
write_file("analysis_report.txt", report)
print("Analysis Report Generated:")
print(report)
```

### Mathematical Sequence Analysis

```python
from utils.math_utils import is_prime, generate_primes, is_perfect_square
from utils.data_structures import group_by_key

# Analyze numbers 1-100
numbers = list(range(1, 101))

# Classify numbers
number_analysis = []
for num in numbers:
    analysis = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect_square": is_perfect_square(num),
        "is_even": num % 2 == 0,
        "digit_sum": sum(int(digit) for digit in str(num))
    }
    number_analysis.append(analysis)

# Group by different properties
prime_numbers = [n["number"] for n in number_analysis if n["is_prime"]]
perfect_squares = [n["number"] for n in number_analysis if n["is_perfect_square"]]
even_numbers = [n["number"] for n in number_analysis if n["is_even"]]

print(f"Prime numbers (1-100): {prime_numbers[:10]}...  (showing first 10)")
print(f"Perfect squares (1-100): {perfect_squares}")
print(f"Even numbers count: {len(even_numbers)}")

# Find interesting patterns
prime_squares = [n for n in perfect_squares if is_prime(n)]
print(f"Numbers that are both prime and perfect square: {prime_squares}")

# Digit sum analysis
digit_sum_groups = group_by_key(number_analysis, "digit_sum")
max_digit_sum = max(digit_sum_groups.keys())
numbers_with_max_digit_sum = [n["number"] for n in digit_sum_groups[max_digit_sum]]

print(f"Maximum digit sum: {max_digit_sum}")
print(f"Numbers with max digit sum: {numbers_with_max_digit_sum}")
```

---

## Integration Examples

### Complete Text Processing System

```python
# This example shows how to combine multiple utilities
from utils import *
import os

def process_text_file(input_file, output_file):
    """Complete text processing pipeline"""
    
    # Step 1: Check if input file exists
    if not file_utils.file_exists(input_file):
        print(f"Error: {input_file} does not exist")
        return False
    
    # Step 2: Read content
    raw_content = file_utils.read_file(input_file)
    
    # Step 3: Process each line
    processed_lines = []
    total_words = 0
    
    for line_num, line in enumerate(raw_content.split('\n'), 1):
        # Clean the line
        cleaned = string_utils.clean_text(line)
        
        if cleaned:  # Skip empty lines
            # Capitalize words
            capitalized = string_utils.capitalize_words(cleaned)
            
            # Count words
            word_count = string_utils.count_words(cleaned)
            total_words += word_count
            
            # Add line number and process
            processed_line = f"[Line {line_num:2d}] {capitalized} ({word_count} words)"
            processed_lines.append(processed_line)
    
    # Step 4: Add summary
    summary = f"\n--- Summary ---\n"
    summary += f"Total lines processed: {len(processed_lines)}\n"
    summary += f"Total words: {total_words}\n"
    summary += f"Average words per line: {total_words/len(processed_lines):.1f}\n"
    
    # Step 5: Combine content
    final_content = '\n'.join(processed_lines) + summary
    
    # Step 6: Write to output file
    file_utils.write_file(output_file, final_content)
    
    print(f"Successfully processed {input_file} -> {output_file}")
    return True

# Example usage
sample_text = """
hello world
this is a test file
python programming is fun
data processing with utilities
"""

# Create sample file
file_utils.write_file("sample_input.txt", sample_text)

# Process the file
process_text_file("sample_input.txt", "processed_output.txt")

# Read and display the result
if file_utils.file_exists("processed_output.txt"):
    result = file_utils.read_file("processed_output.txt")
    print("\nProcessed content:")
    print(result)
```

---

## Error Handling Examples

### Robust Function Usage

```python
from utils import math_utils, string_utils, validators

def safe_factorial(n):
    """Safely calculate factorial with error handling"""
    try:
        # Validate input
        if not validators.is_positive_integer(n):
            return None, "Input must be a positive integer"
        
        # Calculate factorial (assuming we have this in main.py)
        result = 1
        for i in range(1, n + 1):
            result *= i
        
        return result, "Success"
    
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"

def safe_text_analysis(text):
    """Safely analyze text with comprehensive error handling"""
    try:
        # Validate input
        if not isinstance(text, str):
            return None, "Input must be a string"
        
        if not text.strip():
            return {"word_count": 0, "is_palindrome": False, "cleaned": ""}, "Empty string processed"
        
        # Process text
        cleaned = string_utils.clean_text(text)
        word_count = string_utils.count_words(cleaned)
        is_palindrome = string_utils.is_palindrome(cleaned)
        
        result = {
            "original": text,
            "cleaned": cleaned,
            "word_count": word_count,
            "is_palindrome": is_palindrome
        }
        
        return result, "Success"
    
    except Exception as e:
        return None, f"Error processing text: {str(e)}"

# Test error handling
test_cases = [
    (5, "Valid integer"),
    (-1, "Negative integer"), 
    (3.14, "Float"),
    ("5", "String"),
    (None, "None value")
]

print("Factorial Error Handling:")
for value, description in test_cases:
    result, message = safe_factorial(value)
    print(f"{description}: {result} - {message}")

print("\nText Analysis Error Handling:")
text_tests = [
    ("hello world", "Normal text"),
    ("", "Empty string"),
    ("   ", "Whitespace only"),
    (123, "Non-string input"),
    (None, "None input")
]

for text, description in text_tests:
    result, message = safe_text_analysis(text)
    print(f"{description}: {message}")
    if result:
        print(f"  Result: {result}")
```

---

This comprehensive examples guide demonstrates the versatility and power of the Python 101 utility functions. Each example can be run independently or combined to create more complex applications.

**Happy coding! 🐍**
