# Enhanced Python script demonstrating advanced concepts and functions
# This script includes mathematical functions, string manipulation, data structures, and utilities
# Extended with many more functions for comprehensive Python demonstration

import sys
import math
import random
import re
from datetime import date, datetime
from functools import reduce, wraps
import time

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate Fibonacci sequence
def fibonacci_sequence(length):
    fib = [0, 1]
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    return fib

# Function to print a greeting
def greet(name):
    print(f"Hello, {name}!")

# ===== NEW MATHEMATICAL FUNCTIONS =====

# Function to calculate Greatest Common Divisor
def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

# Function to calculate Least Common Multiple
def lcm(a, b):
    """Calculate LCM using the relationship: LCM(a,b) = |a*b| / GCD(a,b)"""
    return abs(a * b) // gcd(a, b)

# Function for modular exponentiation
def power_mod(base, exp, mod):
    """Calculate (base^exp) % mod efficiently"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Function to check if a number is a perfect square
def is_perfect_square(n):
    """Check if n is a perfect square"""
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

# Function to find the nth prime number
def nth_prime(n):
    """Find the nth prime number (1-indexed)"""
    if n <= 0:
        return None
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]

# Function to get prime factorization
def prime_factors(n):
    """Return list of prime factors of n"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Function for matrix multiplication (2x2 matrices)
def matrix_multiply(a, b):
    """Multiply two 2x2 matrices"""
    if len(a) != 2 or len(b) != 2 or len(a[0]) != 2 or len(b[0]) != 2:
        raise ValueError("Only 2x2 matrices supported")
    
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

# ===== STRING MANIPULATION FUNCTIONS =====

# Function to check if string is palindrome
def is_palindrome(text):
    """Check if text is a palindrome (ignoring spaces and case)"""
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return clean_text == clean_text[::-1]

# Function to count vowels
def count_vowels(text):
    """Count the number of vowels in text"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

# Function to reverse words in a sentence
def reverse_words(text):
    """Reverse the order of words in a sentence"""
    return ' '.join(text.split()[::-1])

# Function for Caesar cipher
def caesar_cipher(text, shift):
    """Apply Caesar cipher with given shift"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

# Function to remove duplicate characters
def remove_duplicates(text):
    """Remove duplicate characters while preserving order"""
    seen = set()
    result = ""
    for char in text:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Function to count word frequencies
def word_frequency(text):
    """Count frequency of each word in text"""
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# ===== DATA STRUCTURE FUNCTIONS =====

# Function to merge two sorted lists
def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list"""
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Function for binary search
def binary_search(arr, target):
    """Binary search implementation, returns index or -1"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Function for quicksort
def quick_sort(arr):
    """Quick sort implementation"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Function to find duplicates
def find_duplicates(arr):
    """Find all duplicate elements in a list"""
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# Function to rotate list
def rotate_list(arr, k):
    """Rotate list to the right by k positions"""
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Function to flatten nested list
def flatten_nested_list(nested):
    """Flatten a nested list structure"""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result

# ===== UTILITY FUNCTIONS =====

# Function to generate password
def generate_password(length=12):
    """Generate a random password with specified length"""
    import string
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Function to validate email
def validate_email(email):
    """Basic email validation using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Function for temperature conversion
def convert_temperature(temp, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # Convert to Celsius first
    if from_unit == 'f' or from_unit == 'fahrenheit':
        celsius = (temp - 32) * 5/9
    elif from_unit == 'k' or from_unit == 'kelvin':
        celsius = temp - 273.15
    else:  # Celsius
        celsius = temp
    
    # Convert from Celsius to target
    if to_unit == 'f' or to_unit == 'fahrenheit':
        return celsius * 9/5 + 32
    elif to_unit == 'k' or to_unit == 'kelvin':
        return celsius + 273.15
    else:  # Celsius
        return celsius

# Function to calculate age
def calculate_age(birth_date):
    """Calculate age from birth date (YYYY-MM-DD format)"""
    if isinstance(birth_date, str):
        birth = datetime.strptime(birth_date, '%Y-%m-%d').date()
    else:
        birth = birth_date
    
    today = date.today()
    age = today.year - birth.year
    
    if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
        age -= 1
    
    return age

# Function to format file size
def format_file_size(bytes):
    """Format bytes to human readable format"""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(bytes)
    
    for unit in units:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    
    return f"{size:.1f} PB"

# Function to parse CSV line
def parse_csv_line(line):
    """Simple CSV parser for a single line"""
    result = []
    current_field = ""
    in_quotes = False
    
    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            result.append(current_field.strip())
            current_field = ""
        else:
            current_field += char
    
    result.append(current_field.strip())
    return result

# ===== ADVANCED CONCEPTS =====

# Memoization decorator
def memoize(func):
    """Decorator to memoize function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper

# Timer context manager
class Timer:
    """Context manager to time code execution"""
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")

# Retry decorator
def retry(max_attempts=3, delay=1):
    """Decorator to retry failed operations"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Custom iterator class
class NumberSequence:
    """Custom iterator for number sequences"""
    def __init__(self, start=0, end=10, step=1):
        self.current = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += self.step
            return current

# Generator function for Fibonacci
def fibonacci_generator():
    """Generator that yields Fibonacci numbers indefinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Function with memoization example
@memoize
def expensive_fibonacci(n):
    """Fibonacci with memoization for better performance"""
    if n <= 1:
        return n
    return expensive_fibonacci(n-1) + expensive_fibonacci(n-2)

# Main execution starts here
if __name__ == "__main__":
    # Print a header
    print("Welcome to this Python demo script!")
    
    # Example of factorial calculation
    print("Factorial of 5:", factorial(5))
    
    # Example of prime check
    print("Is 17 prime?", is_prime(17))
    
    # Generate and print Fibonacci sequence
    fib_seq = fibonacci_sequence(10)
    print("First 10 Fibonacci numbers:", fib_seq)
    
    # Greeting example
    greet("World")
    
    # Loop to demonstrate iteration
    for i in range(1, 11):
        print(f"Counting: {i}")
    
    # List comprehension example
    squares = [x**2 for x in range(1, 6)]
    print("Squares of 1 to 5:", squares)
    
    # Dictionary example
    person = {"name": "Alice", "age": 30}
    print("Person info:", person)
    
    # Try-except block
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    
    # Random number generation
    random_num = random.randint(1, 100)
    print("Random number between 1 and 100:", random_num)
    
    # String manipulation
    text = "Python is fun!"
    print("Uppercase:", text.upper())
    print("Length:", len(text))
    
    # File handling simulation (without actual file)
    print("Simulating file read: This is sample content.")
    
    # Class definition
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def subtract(self, a, b):
            return a - b
    
    # Instantiate and use class
    calc = Calculator()
    print("5 + 3 =", calc.add(5, 3))
    print("5 - 3 =", calc.subtract(5, 3))
    
    # Lambda function
    multiply = lambda x, y: x * y
    print("4 * 7 =", multiply(4, 7))
    
    # Set operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    
    # Tuple unpacking
    point = (10, 20)
    x, y = point
    print(f"Point: ({x}, {y})")
    
    # Enum simulation with constants
    PI = 3.14159
    print("Value of PI:", PI)
    
    # Conditional statements
    age = 25
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
    
    # While loop
    count = 0
    while count < 5:
        print("While loop iteration:", count)
        count += 1
    
    # Generator expression
    gen = (x for x in range(3))
    for val in gen:
        print("Generator value:", val)
    
    # Decorators (simple example)
    def my_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello from decorated function!")
    
    say_hello()
    
    # List methods
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    print("Fruits list:", fruits)
    fruits.sort()
    print("Sorted fruits:", fruits)
    
    # Dictionary methods
    scores = {"math": 95, "science": 88}
    print("Average score:", sum(scores.values()) / len(scores))
    
    # String formatting
    name = "Bob"
    age = 28
    print(f"{name} is {age} years old.")
    
    # Import from module
    from datetime import date
    today = date.today()
    print("Today's date:", today)
    
    # Exception handling with else
    try:
        num = int("123")
    except ValueError:
        print("Invalid number")
    else:
        print("Number is:", num)
    
    # Finally block
    try:
        file = open("nonexistent.txt", "r")
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Cleanup done")
    
    # Recursion example (simple)
    def countdown(n):
        if n > 0:
            print(n)
            countdown(n - 1)
        else:
            print("Blast off!")
    
    countdown(3)
    
    # Map function
    numbers = [1, 2, 3, 4]
    doubled = list(map(lambda x: x * 2, numbers))
    print("Doubled numbers:", doubled)
    
    # Filter function
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", evens)
    
    # Reduce simulation (using functools)
    from functools import reduce
    product = reduce(lambda x, y: x * y, numbers)
    print("Product:", product)
    
    # Context manager simulation
    print("Simulating context manager: Resource acquired and released.")
    
    # Async simulation (commented, as it's advanced)
    # import asyncio
    # async def async_task():
    #     print("Async task")
    # asyncio.run(async_task())
    
    # Error handling in functions
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    
    try:
        print(divide(10, 2))
    except ValueError as e:
        print(e)
    
    # Working with bytes
    byte_data = b"Hello"
    print("Bytes:", byte_data)
    
    # JSON simulation (without import)
    print("Simulating JSON: {'key': 'value'}")
    
    # Performance note
    print("This script demonstrates various Python features.")
    
    # End of script
    print("Script execution completed.")
    
    # ===== TESTING NEW FUNCTIONS =====
    print("\n" + "="*50)
    print("TESTING NEW FUNCTIONS")
    print("="*50)
    
    # Test mathematical functions
    print("\n--- Mathematical Functions ---")
    print(f"GCD(48, 18): {gcd(48, 18)}")
    print(f"LCM(12, 15): {lcm(12, 15)}")
    print(f"Power mod (3^13 mod 7): {power_mod(3, 13, 7)}")
    print(f"Is 16 a perfect square? {is_perfect_square(16)}")
    print(f"5th prime number: {nth_prime(5)}")
    print(f"Prime factors of 60: {prime_factors(60)}")
    
    # Test matrix multiplication
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    print(f"Matrix multiplication: {matrix_multiply(matrix_a, matrix_b)}")
    
    # Test string functions
    print("\n--- String Manipulation Functions ---")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Is 'A man a plan a canal Panama' a palindrome? {is_palindrome('A man a plan a canal Panama')}")
    print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
    print(f"Reverse words 'Hello World Python': {reverse_words('Hello World Python')}")
    print(f"Caesar cipher 'HELLO' shift 3: {caesar_cipher('HELLO', 3)}")
    print(f"Remove duplicates 'programming': {remove_duplicates('programming')}")
    print(f"Word frequency 'the quick brown fox jumps over the lazy dog': {word_frequency('the quick brown fox jumps over the lazy dog')}")
    
    # Test data structure functions
    print("\n--- Data Structure Functions ---")
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print(f"Merge sorted lists {list1} and {list2}: {merge_sorted_lists(list1, list2)}")
    
    sorted_arr = [1, 3, 5, 7, 9, 11, 13]
    print(f"Binary search for 7 in {sorted_arr}: {binary_search(sorted_arr, 7)}")
    
    unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Quick sort {unsorted_arr}: {quick_sort(unsorted_arr)}")
    
    dup_arr = [1, 2, 3, 2, 4, 5, 1]
    print(f"Find duplicates in {dup_arr}: {find_duplicates(dup_arr)}")
    
    rotate_arr = [1, 2, 3, 4, 5]
    print(f"Rotate {rotate_arr} by 2 positions: {rotate_list(rotate_arr, 2)}")
    
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"Flatten {nested}: {flatten_nested_list(nested)}")
    
    # Test utility functions
    print("\n--- Utility Functions ---")
    print(f"Generated password (8 chars): {generate_password(8)}")
    print(f"Is 'test@example.com' valid email? {validate_email('test@example.com')}")
    print(f"Is 'invalid-email' valid email? {validate_email('invalid-email')}")
    print(f"Convert 32°F to Celsius: {convert_temperature(32, 'F', 'C'):.1f}°C")
    print(f"Convert 0°C to Kelvin: {convert_temperature(0, 'C', 'K'):.1f}K")
    print(f"Age if born on 1990-05-15: {calculate_age('1990-05-15')} years")
    print(f"Format 1536 bytes: {format_file_size(1536)}")
    print(f"Format 5242880 bytes: {format_file_size(5242880)}")
    
    csv_line = 'John Doe,"Software Engineer","New York, NY",50000'
    print(f"Parse CSV: {parse_csv_line(csv_line)}")
    
    # Test advanced concepts
    print("\n--- Advanced Concepts ---")
    
    # Test memoized fibonacci
    with Timer():
        print(f"Memoized Fibonacci(30): {expensive_fibonacci(30)}")
    
    # Test custom iterator
    print("Custom iterator (0 to 5, step 2):", end=" ")
    for num in NumberSequence(0, 5, 2):
        print(num, end=" ")
    print()
    
    # Test fibonacci generator
    print("First 10 Fibonacci numbers from generator:", end=" ")
    fib_gen = fibonacci_generator()
    for _ in range(10):
        print(next(fib_gen), end=" ")
    print()
    
    # Test retry decorator
    @retry(max_attempts=2, delay=0.1)
    def flaky_function():
        if random.random() < 0.7:  # 70% chance to fail
            raise Exception("Random failure")
        return "Success!"
    
    try:
        result = flaky_function()
        print(f"Retry decorator test: {result}")
    except Exception as e:
        print(f"Retry decorator test failed: {e}")
    
    print("\n" + "="*50)
    print("ALL FUNCTION TESTS COMPLETED!")
    print("="*50)
    