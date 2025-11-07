"""
Advanced Python Features Showcase
Demonstrates decorators, context managers, generators, and more
"""

from functools import wraps
from contextlib import contextmanager
from typing import Generator, Callable
import time


# Decorator Example
def timing_decorator(func: Callable) -> Callable:
    """Decorator that measures execution time of a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def retry_decorator(max_attempts: int = 3):
    """Decorator factory that retries a function on failure"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"⚠️  Attempt {attempt + 1} failed: {e}. Retrying...")
            return None
        return wrapper
    return decorator


# Context Manager Example
@contextmanager
def custom_context_manager(name: str) -> Generator[str, None, None]:
    """Custom context manager using generator"""
    print(f"🔓 Entering context: {name}")
    try:
        yield f"Resource: {name}"
    finally:
        print(f"🔒 Exiting context: {name}")


class FileLogger:
    """Context manager class for logging"""
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        print(f"📝 Opening log file: {self.filename}")
        self.file = open(self.filename, 'a')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"✅ Closed log file: {self.filename}")
        return False


# Generator Examples
def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence up to n terms"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    """Infinite counter generator"""
    count = start
    while True:
        yield count
        count += 1


# List Comprehension and Generator Expression
@timing_decorator
def list_comprehension_demo():
    """Demonstrate list comprehensions"""
    squares = [x**2 for x in range(1000)]
    evens = [x for x in range(100) if x % 2 == 0]
    matrix = [[i*j for j in range(5)] for i in range(5)]
    return len(squares), len(evens), len(matrix)


@timing_decorator
def generator_expression_demo():
    """Demonstrate generator expressions (memory efficient)"""
    squares_gen = (x**2 for x in range(1000))
    return sum(squares_gen)


# Lambda and Higher-Order Functions
def apply_operations(numbers: list[int]) -> dict:
    """Apply various operations using lambda and map/filter/reduce"""
    from functools import reduce
    
    return {
        'doubled': list(map(lambda x: x * 2, numbers)),
        'evens': list(filter(lambda x: x % 2 == 0, numbers)),
        'sum': reduce(lambda x, y: x + y, numbers),
        'product': reduce(lambda x, y: x * y, numbers, 1)
    }


# Unpacking and Pattern Matching (Python 3.10+)
def unpacking_demo():
    """Demonstrate various unpacking techniques"""
    # Basic unpacking
    a, b, *rest = [1, 2, 3, 4, 5]
    print(f"a={a}, b={b}, rest={rest}")
    
    # Dictionary unpacking
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged = {**dict1, **dict2}
    print(f"Merged dict: {merged}")
    
    # Function argument unpacking
    def greet(name, age, city):
        return f"{name} is {age} years old and lives in {city}"
    
    person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
    print(greet(**person))


# Main demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("🐍 ADVANCED PYTHON FEATURES SHOWCASE")
    print("=" * 60)
    
    # Decorators
    print("\n1️⃣  DECORATORS")
    print("-" * 60)
    list_comprehension_demo()
    result = generator_expression_demo()
    print(f"Generator sum result: {result}")
    
    # Context Managers
    print("\n2️⃣  CONTEXT MANAGERS")
    print("-" * 60)
    with custom_context_manager("MyResource") as resource:
        print(f"Using {resource}")
    
    with FileLogger("/tmp/demo.log") as log:
        log.write(f"Log entry at {time.time()}\n")
    
    # Generators
    print("\n3️⃣  GENERATORS")
    print("-" * 60)
    print("Fibonacci sequence (first 10):", list(fibonacci_generator(10)))
    
    counter = infinite_counter(100)
    print("Infinite counter (first 5):", [next(counter) for _ in range(5)])
    
    # Lambda and Higher-Order Functions
    print("\n4️⃣  LAMBDA & HIGHER-ORDER FUNCTIONS")
    print("-" * 60)
    numbers = [1, 2, 3, 4, 5]
    operations = apply_operations(numbers)
    for key, value in operations.items():
        print(f"{key}: {value}")
    
    # Unpacking
    print("\n5️⃣  UNPACKING")
    print("-" * 60)
    unpacking_demo()
    
    print("\n" + "=" * 60)
    print("✨ Demo complete!")
    print("=" * 60)
