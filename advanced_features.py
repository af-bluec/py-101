"""
Advanced Python Features Showcase
Demonstrates decorators, context managers, generators, and more
"""

from functools import wraps
from typing import Generator, List, Dict, Any
from contextlib import contextmanager
import time


# Decorator Example
def timing_decorator(func):
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


# Generator Example
def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence up to n terms"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Context Manager Example
@contextmanager
def custom_context_manager(name: str):
    """Custom context manager for resource management"""
    print(f"Entering context: {name}")
    try:
        yield name
    finally:
        print(f"Exiting context: {name}")


# List Comprehension and Lambda Examples
def data_processing_examples():
    """Showcase list comprehensions, lambdas, and functional programming"""
    numbers = list(range(1, 11))
    
    # List comprehension
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")
    
    # List comprehension with condition
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Dictionary comprehension
    square_dict = {x: x**2 for x in numbers}
    print(f"Square dictionary: {square_dict}")
    
    # Lambda with map
    cubes = list(map(lambda x: x**3, numbers))
    print(f"Cubes: {cubes}")
    
    # Lambda with filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")


# Class with Magic Methods
class Vector:
    """Vector class demonstrating magic methods"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y
    
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2)**0.5


# Property Decorator Example
class Temperature:
    """Temperature class with property decorators"""
    
    def __init__(self, celsius: float = 0):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5/9


@timing_decorator
def demonstrate_features():
    """Main demonstration function"""
    print("=" * 50)
    print("Python Advanced Features Showcase")
    print("=" * 50)
    
    # Generator
    print("\n1. Fibonacci Generator:")
    fib_numbers = list(fibonacci_generator(10))
    print(f"First 10 Fibonacci numbers: {fib_numbers}")
    
    # Context Manager
    print("\n2. Context Manager:")
    with custom_context_manager("MyResource") as resource:
        print(f"Using resource: {resource}")
    
    # Data Processing
    print("\n3. Data Processing (Comprehensions & Lambdas):")
    data_processing_examples()
    
    # Magic Methods
    print("\n4. Vector Class with Magic Methods:")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"v1 = {v1}, magnitude = {v1.magnitude():.2f}")
    print(f"v2 = {v2}, magnitude = {v2.magnitude():.2f}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 * 2 = {v1 * 2}")
    
    # Properties
    print("\n5. Property Decorators:")
    temp = Temperature(25)
    print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
    temp.fahrenheit = 98.6
    print(f"Body temperature: {temp.celsius:.1f}°C = {temp.fahrenheit}°F")


if __name__ == "__main__":
    demonstrate_features()
