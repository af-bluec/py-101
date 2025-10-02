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
    