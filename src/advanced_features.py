"""
Advanced Python features and utilities.

This module demonstrates advanced Python concepts including generators,
context managers, lambda functions, and other advanced language features.
"""

import contextlib
from typing import Generator, Any, Iterator, List, Callable
import sys
import io


# Generator functions
def countdown_generator(n: int) -> Generator[int, None, None]:
    """
    Generator that counts down from n to 1.
    
    Args:
        n: Starting number
        
    Yields:
        Countdown numbers
    """
    while n > 0:
        yield n
        n -= 1


def fibonacci_generator() -> Generator[int, None, None]:
    """
    Infinite Fibonacci sequence generator.
    
    Yields:
        Fibonacci numbers
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def range_with_step(start: int, stop: int, step: int = 1) -> Generator[int, None, None]:
    """
    Custom range generator with step.
    
    Args:
        start: Starting value
        stop: Stopping value (exclusive)
        step: Step size
        
    Yields:
        Numbers in the range
    """
    current = start
    while current < stop:
        yield current
        current += step


def batch_generator(iterable: list, batch_size: int) -> Generator[List[Any], None, None]:
    """
    Generator that yields batches of items from an iterable.
    
    Args:
        iterable: Input iterable
        batch_size: Size of each batch
        
    Yields:
        Batches of items
    """
    iterator = iter(iterable)
    while True:
        batch = []
        try:
            for _ in range(batch_size):
                batch.append(next(iterator))
            yield batch
        except StopIteration:
            if batch:
                yield batch
            break


# Context managers
@contextlib.contextmanager
def timer_context():
    """
    Context manager to time code execution.
    
    Usage:
        with timer_context():
            # code to time
    """
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")


@contextlib.contextmanager
def suppress_output():
    """
    Context manager to suppress stdout output.
    
    Usage:
        with suppress_output():
            print("This won't be shown")
    """
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = old_stdout


@contextlib.contextmanager
def temporary_attribute(obj: Any, attr: str, value: Any):
    """
    Context manager to temporarily set an attribute.
    
    Args:
        obj: Object to modify
        attr: Attribute name
        value: Temporary value
    """
    old_value = getattr(obj, attr, None)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        if old_value is None:
            delattr(obj, attr)
        else:
            setattr(obj, attr, old_value)


class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()


# Lambda function utilities
def create_lambda_functions():
    """
    Create and return various lambda functions.
    
    Returns:
        Dictionary of lambda functions
    """
    return {
        'square': lambda x: x ** 2,
        'cube': lambda x: x ** 3,
        'add': lambda x, y: x + y,
        'multiply': lambda x, y: x * y,
        'is_even': lambda x: x % 2 == 0,
        'is_positive': lambda x: x > 0,
        'max_of_three': lambda a, b, c: max(a, b, c),
        'string_length': lambda s: len(s),
        'uppercase': lambda s: s.upper(),
        'reverse_string': lambda s: s[::-1]
    }


def apply_lambda_to_list(data: List[Any], func: Callable) -> List[Any]:
    """
    Apply a lambda function to each element in a list.
    
    Args:
        data: Input list
        func: Lambda function to apply
        
    Returns:
        List with function applied to each element
    """
    return list(map(func, data))


def filter_with_lambda(data: List[Any], predicate: Callable) -> List[Any]:
    """
    Filter a list using a lambda predicate.
    
    Args:
        data: Input list
        predicate: Lambda function that returns boolean
        
    Returns:
        Filtered list
    """
    return list(filter(predicate, data))


def reduce_with_lambda(data: List[Any], func: Callable, initial=None):
    """
    Reduce a list using a lambda function.
    
    Args:
        data: Input list
        func: Lambda function for reduction
        initial: Initial value
        
    Returns:
        Reduced value
    """
    from functools import reduce
    if initial is not None:
        return reduce(func, data, initial)
    return reduce(func, data)


# Iterator classes
class CountUp:
    """Iterator that counts up to a limit."""
    
    def __init__(self, limit: int):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.limit:
            current = self.current
            self.current += 1
            return current
        raise StopIteration


class ReverseIterator:
    """Iterator that reverses any sequence."""
    
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.sequence[self.index]
        raise StopIteration


# Coroutine example (simplified)
def simple_coroutine():
    """
    Simple coroutine example.
    
    Returns:
        Generator that can receive values
    """
    result = yield
    while True:
        print(f"Received: {result}")
        result = yield result * 2


# Advanced function features
def function_with_closure(multiplier: int):
    """
    Function that creates a closure.
    
    Args:
        multiplier: Value to multiply by
        
    Returns:
        Function that multiplies by the given value
    """
    def multiply(x: int) -> int:
        return x * multiplier
    return multiply


def partial_function_example():
    """
    Example of partial function application.
    
    Returns:
        Dictionary of partial functions
    """
    from functools import partial
    
    def power(base: int, exponent: int) -> int:
        return base ** exponent
    
    return {
        'square': partial(power, exponent=2),
        'cube': partial(power, exponent=3),
        'power_of_ten': partial(power, base=10)
    }


# Metaclass example (simplified)
class SingletonMeta(type):
    """Metaclass for singleton pattern."""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Example singleton class using metaclass."""
    
    def __init__(self):
        self.connected = False
    
    def connect(self):
        """Simulate database connection."""
        self.connected = True
        print("Database connected")
    
    def disconnect(self):
        """Simulate database disconnection."""
        self.connected = False
        print("Database disconnected")
