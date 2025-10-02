"""
Decorators module.

This module contains various decorator examples and utilities.
"""

import time
from functools import wraps


def simple_decorator(func):
    """
    A simple decorator that prints before and after function execution.
    
    Args:
        func: Function to decorate
        
    Returns:
        function: Wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper


def timing_decorator(func):
    """
    A decorator that measures function execution time.
    
    Args:
        func: Function to decorate
        
    Returns:
        function: Wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper


def retry_decorator(max_attempts=3):
    """
    A decorator that retries function execution on failure.
    
    Args:
        max_attempts (int): Maximum number of retry attempts
        
    Returns:
        function: Decorator function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            return None
        return wrapper
    return decorator


def log_calls(func):
    """
    A decorator that logs function calls with arguments.
    
    Args:
        func: Function to decorate
        
    Returns:
        function: Wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


# Example decorated functions
@simple_decorator
def say_hello():
    """Example function to demonstrate simple decorator."""
    print("Hello from decorated function!")


@timing_decorator
def slow_function():
    """Example function to demonstrate timing decorator."""
    time.sleep(0.1)
    return "Completed slow operation"


@log_calls
def add_numbers(a, b):
    """Example function to demonstrate logging decorator."""
    return a + b
