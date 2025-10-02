"""
Mathematical operations module.

This module provides basic mathematical functions including
factorial calculation, prime number checking, and Fibonacci sequence generation.
"""

import math
from typing import List


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): Non-negative integer to calculate factorial for
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        num (int): Number to check for primality
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def fibonacci_sequence(length: int) -> List[int]:
    """
    Generate Fibonacci sequence of specified length.
    
    Args:
        length (int): Length of Fibonacci sequence to generate
        
    Returns:
        List[int]: Fibonacci sequence
        
    Raises:
        ValueError: If length is less than 1
        TypeError: If length is not an integer
    """
    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    if length == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    return fib
