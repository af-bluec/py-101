"""
Mathematical operations module.

This module contains various mathematical functions including
factorial calculation, prime number checking, and Fibonacci sequence generation.
"""

import math


def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): The number to calculate factorial for
        
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


def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_sequence(length):
    """
    Generate a Fibonacci sequence of specified length.
    
    Args:
        length (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: A list containing the Fibonacci sequence
        
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


def countdown(n):
    """
    Recursive countdown function.
    
    Args:
        n (int): Starting number for countdown
    """
    if n > 0:
        print(n)
        countdown(n - 1)
    else:
        print("Blast off!")


def divide(a, b):
    """
    Safely divide two numbers.
    
    Args:
        a (float): Dividend
        b (float): Divisor
        
    Returns:
        float: Result of division
        
    Raises:
        ValueError: If divisor is zero
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
