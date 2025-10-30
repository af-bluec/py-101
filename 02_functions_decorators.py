"""
Demonstration of Python functions, decorators, and functional programming concepts.
"""

# Basic functions
def greet(name, greeting="Hello"):
    """Function with default parameter."""
    return f"{greeting}, {name}!"


def calculate_stats(*numbers):
    """Function with variable arguments (*args)."""
    if not numbers:
        return None
    return {
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }


def create_profile(**kwargs):
    """Function with keyword arguments (**kwargs)."""
    return kwargs


# Lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y


# Decorators
def timer_decorator(func):
    """Decorator that prints when a function is called."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper


def validate_positive(func):
    """Decorator that validates positive numbers."""
    def wrapper(x):
        if x < 0:
            raise ValueError("Number must be positive")
        return func(x)
    return wrapper


@timer_decorator
def slow_function():
    """Example function with decorator."""
    total = sum(range(1000000))
    return total


@validate_positive
def square_root(x):
    """Calculate square root (simplified)."""
    return x ** 0.5


# Higher-order functions
def apply_operation(numbers, operation):
    """Apply an operation to all numbers."""
    return [operation(n) for n in numbers]


def create_multiplier(factor):
    """Function that returns a function (closure)."""
    def multiply(x):
        return x * factor
    return multiply


# Generator function
def fibonacci_generator(n):
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def main():
    print("=== BASIC FUNCTIONS ===")
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    
    print("\n=== VARIABLE ARGUMENTS ===")
    stats = calculate_stats(10, 20, 30, 40, 50)
    print(f"Stats: {stats}")
    
    print("\n=== KEYWORD ARGUMENTS ===")
    profile = create_profile(name="Charlie", age=25, city="NYC")
    print(f"Profile: {profile}")
    
    print("\n=== LAMBDA FUNCTIONS ===")
    print(f"Square of 5: {square(5)}")
    print(f"Add 3 and 7: {add(3, 7)}")
    
    print("\n=== DECORATORS ===")
    slow_function()
    try:
        print(f"Square root of 16: {square_root(16)}")
        print(f"Square root of -4: {square_root(-4)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== HIGHER-ORDER FUNCTIONS ===")
    numbers = [1, 2, 3, 4, 5]
    doubled = apply_operation(numbers, lambda x: x * 2)
    print(f"Doubled: {doubled}")
    
    triple = create_multiplier(3)
    print(f"Triple of 7: {triple(7)}")
    
    print("\n=== GENERATORS ===")
    fib = list(fibonacci_generator(10))
    print(f"First 10 Fibonacci numbers: {fib}")
    
    print("\n=== MAP, FILTER, REDUCE ===")
    numbers = [1, 2, 3, 4, 5, 6]
    squared = list(map(lambda x: x**2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Squared: {squared}")
    print(f"Evens: {evens}")
    
    from functools import reduce
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product: {product}")


if __name__ == "__main__":
    main()
