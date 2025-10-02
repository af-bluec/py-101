"""
Utility functions module.

This module contains various utility functions for string manipulation,
data processing, and other common operations.
"""

import random
from typing import Any, Callable, List, Set, Tuple
from functools import reduce


def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name (str): Name to greet
        
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"


def generate_random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random number within specified range.
    
    Args:
        min_val (int): Minimum value (inclusive)
        max_val (int): Maximum value (inclusive)
        
    Returns:
        int: Random number between min_val and max_val
    """
    return random.randint(min_val, max_val)


def string_operations(text: str) -> dict:
    """
    Perform various string operations.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary containing various string operations results
    """
    return {
        'uppercase': text.upper(),
        'lowercase': text.lower(),
        'length': len(text),
        'reversed': text[::-1],
        'words': text.split(),
        'capitalized': text.capitalize()
    }


def set_operations(set1: Set[Any], set2: Set[Any]) -> dict:
    """
    Perform various set operations.
    
    Args:
        set1 (Set[Any]): First set
        set2 (Set[Any]): Second set
        
    Returns:
        dict: Dictionary containing set operation results
    """
    return {
        'union': set1 | set2,
        'intersection': set1 & set2,
        'difference': set1 - set2,
        'symmetric_difference': set1 ^ set2
    }


def list_operations(numbers: List[int]) -> dict:
    """
    Perform various list operations.
    
    Args:
        numbers (List[int]): List of numbers
        
    Returns:
        dict: Dictionary containing list operation results
    """
    if not numbers:
        return {'error': 'Empty list provided'}
    
    return {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers),
        'sorted': sorted(numbers),
        'reversed': list(reversed(numbers)),
        'squared': [x**2 for x in numbers],
        'evens': [x for x in numbers if x % 2 == 0],
        'odds': [x for x in numbers if x % 2 != 0]
    }


def apply_lambda_operations(numbers: List[int]) -> dict:
    """
    Apply lambda functions to a list of numbers.
    
    Args:
        numbers (List[int]): List of numbers
        
    Returns:
        dict: Dictionary containing lambda operation results
    """
    multiply = lambda x, y: x * y
    
    return {
        'doubled': list(map(lambda x: x * 2, numbers)),
        'evens': list(filter(lambda x: x % 2 == 0, numbers)),
        'product': reduce(multiply, numbers) if numbers else 0,
        'squares': list(map(lambda x: x**2, numbers))
    }


def tuple_operations(point: Tuple[int, int]) -> dict:
    """
    Perform operations on a tuple representing a point.
    
    Args:
        point (Tuple[int, int]): Tuple representing (x, y) coordinates
        
    Returns:
        dict: Dictionary containing tuple operation results
    """
    x, y = point
    return {
        'x': x,
        'y': y,
        'distance_from_origin': (x**2 + y**2)**0.5,
        'quadrant': get_quadrant(x, y)
    }


def get_quadrant(x: int, y: int) -> str:
    """
    Determine the quadrant of a point.
    
    Args:
        x (int): X coordinate
        y (int): Y coordinate
        
    Returns:
        str: Quadrant description
    """
    if x > 0 and y > 0:
        return "First quadrant"
    elif x < 0 and y > 0:
        return "Second quadrant"
    elif x < 0 and y < 0:
        return "Third quadrant"
    elif x > 0 and y < 0:
        return "Fourth quadrant"
    else:
        return "On axis"


def decorator_example(func: Callable) -> Callable:
    """
    Example decorator that logs function calls.
    
    Args:
        func (Callable): Function to decorate
        
    Returns:
        Callable: Decorated function
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper
