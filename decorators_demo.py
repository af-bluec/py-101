"""
Python Decorators Demonstration

This module showcases various types of decorators in Python:
- Function decorators
- Class decorators 
- Property decorators
- Parameterized decorators
- Method decorators

Decorators are a powerful Python feature that allows you to modify or extend
the behavior of functions, methods, or classes without permanently modifying them.
"""

import time
import functools
from typing import Any, Callable


# Basic function decorator
def timer(func: Callable) -> Callable:
    """
    A decorator that measures the execution time of a function.
    
    Args:
        func: The function to be timed
        
    Returns:
        A wrapper function that times the original function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


# Parameterized decorator
def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    A decorator that retries a function call if it fails.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retry attempts in seconds
        
    Returns:
        A decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


# Class decorator
def add_repr(cls):
    """
    A class decorator that adds a __repr__ method to a class.
    
    Args:
        cls: The class to modify
        
    Returns:
        The modified class with __repr__ method
    """
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    
    cls.__repr__ = __repr__
    return cls


# Method decorator with access to instance
def validate_positive(func: Callable) -> Callable:
    """
    A decorator that validates all numeric arguments are positive.
    
    Args:
        func: The method to validate
        
    Returns:
        A wrapper method that validates arguments
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Check all numeric arguments
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Expected positive number, got {arg}")
        
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(f"Expected positive number for {key}, got {value}")
        
        return func(self, *args, **kwargs)
    return wrapper


# Demonstration classes and functions
@add_repr
class Person:
    """A person class enhanced with automatic repr generation."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class BankAccount:
    """A bank account class demonstrating method decorators."""
    
    def __init__(self, balance: float = 0.0):
        self._balance = balance
    
    @property
    def balance(self) -> float:
        """Get the current balance."""
        return self._balance
    
    @validate_positive
    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
    
    @validate_positive
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")


@timer
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number (with timing)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@retry(max_attempts=3, delay=0.5)
def unreliable_network_call(fail_probability: float = 0.7) -> str:
    """Simulate an unreliable network call that might fail."""
    import random
    
    if random.random() < fail_probability:
        raise ConnectionError("Network connection failed")
    
    return "Success! Data retrieved from network."


# Chaining decorators
@timer
@retry(max_attempts=2, delay=0.1)
def complex_calculation(x: int) -> int:
    """A function with multiple decorators applied."""
    if x < 0:
        raise ValueError("Negative input not allowed")
    return sum(i ** 2 for i in range(x))


if __name__ == "__main__":
    print("=== Python Decorators Demo ===\n")
    
    # Class decorator demo
    print("1. Class Decorator Demo:")
    person = Person("Alice", 30)
    print(f"Person object: {person}")
    print()
    
    # Property and method decorators
    print("2. Method Decorators Demo:")
    account = BankAccount(100.0)
    print(f"Initial balance: ${account.balance:.2f}")
    
    try:
        account.deposit(50.0)
        account.withdraw(25.0)
        # This will raise an exception
        account.deposit(-10.0)
    except ValueError as e:
        print(f"Validation error: {e}")
    print()
    
    # Function decorators
    print("3. Function Decorators Demo:")
    print("Calculating fibonacci(10):")
    result = fibonacci(10)
    print(f"Result: {result}")
    print()
    
    # Retry decorator
    print("4. Retry Decorator Demo:")
    try:
        result = unreliable_network_call(fail_probability=0.3)
        print(f"Network call result: {result}")
    except ConnectionError as e:
        print(f"All retry attempts failed: {e}")
    print()
    
    # Chained decorators
    print("5. Chained Decorators Demo:")
    try:
        result = complex_calculation(5)
        print(f"Complex calculation result: {result}")
    except ValueError as e:
        print(f"Calculation error: {e}")
