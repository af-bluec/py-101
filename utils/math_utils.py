"""
Mathematical utility functions.
"""
import math
from typing import List


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n: Non-negative integer to calculate factorial for
        
    Returns:
        The factorial of n
        
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
        num: Integer to check for primality
        
    Returns:
        True if the number is prime, False otherwise
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
        length: Number of Fibonacci numbers to generate
        
    Returns:
        List of Fibonacci numbers
        
    Raises:
        ValueError: If length is less than 1
    """
    if length < 1:
        raise ValueError("Length must be at least 1")
    if length == 1:
        return [0]
    if length == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    return fib


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor of two numbers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        The GCD of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple of two numbers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        The LCM of a and b
    """
    return abs(a * b) // gcd(a, b) if a and b else 0
