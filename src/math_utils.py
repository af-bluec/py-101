"""
Mathematical utility functions for basic calculations.

This module provides commonly used mathematical functions including
factorial calculation, prime number checking, and Fibonacci sequence generation.
"""

import math
from typing import List


def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): Non-negative integer to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
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
    Generate a Fibonacci sequence of specified length.
    
    Args:
        length (int): The number of Fibonacci numbers to generate
        
    Returns:
        List[int]: List containing the Fibonacci sequence
        
    Raises:
        ValueError: If length is less than 1
    """
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    if length == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    return fib


def get_prime_numbers(limit: int) -> List[int]:
    """
    Get all prime numbers up to a specified limit.
    
    Args:
        limit (int): Upper limit for prime number search
        
    Returns:
        List[int]: List of all prime numbers up to the limit
    """
    return [num for num in range(2, limit + 1) if is_prime(num)]


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest Common Divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Least Common Multiple of a and b
    """
    return abs(a * b) // gcd(a, b) if a and b else 0
