# Simple Python script demonstrating basic concepts
# This script is generated to be approximately 100 lines long
# It includes comments, functions, and a main execution block

import sys
import math
import random

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

# Advanced mathematical functions
def gcd(a, b):
    """Calculate the Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

def power_of_two(n):
    """Check if a number is a power of two"""
    return n > 0 and (n & (n - 1)) == 0

def perfect_square(n):
    """Check if a number is a perfect square"""
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

# String manipulation utilities
def reverse_words(text):
    """Reverse the order of words in a sentence"""
    return ' '.join(text.split()[::-1])

def count_vowels(text):
    """Count the number of vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if a string is a palindrome (ignoring case and spaces)"""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def capitalize_words(text):
    """Capitalize the first letter of each word"""
    return ' '.join(word.capitalize() for word in text.split())

# Data processing functions
def find_max_min(numbers):
    """Find the maximum and minimum values in a list"""
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

def average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers"""
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        return sorted_nums[n//2]

def remove_duplicates(lst):
    """Remove duplicates from a list while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Utility functions for common tasks
def format_currency(amount, currency_symbol='$'):
    """Format a number as currency"""
    return f"{currency_symbol}{amount:,.2f}"

def generate_random_password(length=8):
    """Generate a random password with letters and numbers"""
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def days_between_dates(date1, date2):
    """Calculate the number of days between two dates (YYYY-MM-DD format)"""
    from datetime import datetime
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

# Algorithm implementations
def binary_search(arr, target):
    """Perform binary search on a sorted array"""
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

def bubble_sort(arr):
    """Sort an array using bubble sort algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def linear_search(arr, target):
    """Perform linear search on an array"""
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def count_occurrences(lst, element):
    """Count how many times an element appears in a list"""
    return lst.count(element)

def flatten_list(nested_list):
    """Flatten a nested list structure"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Text analysis functions
def word_frequency(text):
    """Count the frequency of each word in a text"""
    words = text.lower().split()
    frequency = {}
    for word in words:
        # Remove punctuation
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    return frequency

def longest_word(text):
    """Find the longest word in a text"""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

# Number theory functions
def prime_factors(n):
    """Find all prime factors of a number"""
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

def sum_of_digits(n):
    """Calculate the sum of digits in a number"""
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    """Reverse the digits of a number"""
    return int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)

# Validation functions
def is_email_valid(email):
    """Basic email validation"""
    return '@' in email and '.' in email.split('@')[-1]

def is_strong_password(password):
    """Check if a password meets basic strength criteria"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
    return has_upper and has_lower and has_digit and has_special

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
    
    # DEMONSTRATING NEW FUNCTIONS
    print("\n=== DEMONSTRATING NEW FUNCTIONS ===")
    
    # Advanced mathematical functions
    print("GCD of 48 and 18:", gcd(48, 18))
    print("LCM of 12 and 15:", lcm(12, 15))
    print("Is 16 a power of two?", power_of_two(16))
    print("Is 25 a perfect square?", perfect_square(25))
    
    # String manipulation utilities
    print("Reversed words:", reverse_words("Hello World Python"))
    print("Vowel count in 'programming':", count_vowels("programming"))
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
    print("Capitalized:", capitalize_words("hello world from python"))
    
    # Data processing functions
    sample_numbers = [5, 2, 8, 1, 9, 3]
    print("Max and Min of", sample_numbers, ":", find_max_min(sample_numbers))
    print("Average:", average(sample_numbers))
    print("Median:", median(sample_numbers))
    duplicated_list = [1, 2, 2, 3, 3, 3, 4]
    print("Remove duplicates from", duplicated_list, ":", remove_duplicates(duplicated_list))
    
    # Utility functions
    print("Currency format:", format_currency(1234.56))
    print("Random password:", generate_random_password(12))
    print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))
    print("77°F to Celsius:", fahrenheit_to_celsius(77))
    print("Days between 2024-01-01 and 2024-01-31:", days_between_dates("2024-01-01", "2024-01-31"))
    
    # Algorithm implementations
    sorted_array = [1, 3, 5, 7, 9, 11]
    print("Binary search for 7 in", sorted_array, ":", binary_search(sorted_array, 7))
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", unsorted_array)
    print("Bubble sorted:", bubble_sort(unsorted_array.copy()))
    print("Linear search for 25:", linear_search(unsorted_array, 25))
    print("Count of 3 in [1,2,3,3,4,3]:", count_occurrences([1,2,3,3,4,3], 3))
    nested = [1, [2, 3], [4, [5, 6]]]
    print("Flattened list:", flatten_list(nested))
    
    # Text analysis functions
    sample_text = "This is a simple text with repeated words. This text is for testing."
    print("Word frequency:", word_frequency(sample_text))
    print("Longest word in text:", longest_word(sample_text))
    
    # Number theory functions
    print("Prime factors of 60:", prime_factors(60))
    print("Sum of digits in 12345:", sum_of_digits(12345))
    print("Reverse of 12345:", reverse_number(12345))
    
    # Validation functions
    print("Is 'user@example.com' valid email?", is_email_valid("user@example.com"))
    print("Is 'Password123!' strong?", is_strong_password("Password123!"))
    print("Is 'weak' strong?", is_strong_password("weak"))
    
    # End of script
    print("Script execution completed.")
    