"""
Mathematical utility functions.

This module provides various mathematical operations including number theory,
statistics, geometry, and computational math functions.
"""

import math
from typing import List, Tuple, Union, Optional
from functools import reduce


def gcd(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Greatest common divisor
        
    Example:
        >>> gcd(48, 18)
        6
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate Least Common Multiple.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Least common multiple
        
    Example:
        >>> lcm(4, 6)
        12
    """
    return abs(a * b) // gcd(a, b)


def is_perfect_square(n: int) -> bool:
    """
    Check if a number is a perfect square.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a perfect square
        
    Example:
        >>> is_perfect_square(16)
        True
    """
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n


def generate_primes(limit: int) -> List[int]:
    """
    Generate all prime numbers up to limit using Sieve of Eratosthenes.
    
    Args:
        limit (int): Upper limit (exclusive)
        
    Returns:
        List[int]: List of prime numbers
        
    Example:
        >>> generate_primes(10)
        [2, 3, 5, 7]
    """
    if limit < 2:
        return []
    
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial iteratively.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial_iterative(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_nth(n: int) -> int:
    """
    Calculate the nth Fibonacci number efficiently.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: nth Fibonacci number
        
    Example:
        >>> fibonacci_nth(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_perfect_number(n: int) -> bool:
    """
    Check if a number is perfect (equals sum of its proper divisors).
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is perfect
        
    Example:
        >>> is_perfect_number(28)
        True
    """
    if n < 2:
        return False
    
    divisor_sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting the same divisor twice for perfect squares
                divisor_sum += n // i
    
    return divisor_sum == n


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate arithmetic mean of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: Arithmetic mean
        
    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculate median of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: Median value
        
    Example:
        >>> median([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return float(sorted_numbers[n // 2])


def mode(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Find the mode (most frequent value) in a list.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        Union[int, float]: Most frequent number
        
    Example:
        >>> mode([1, 2, 2, 3, 3, 3])
        3
    """
    if not numbers:
        raise ValueError("Cannot find mode of empty list")
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    return max(frequency, key=frequency.get)


def standard_deviation(numbers: List[Union[int, float]], population: bool = True) -> float:
    """
    Calculate standard deviation.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        population (bool): If True, calculate population std dev; if False, sample std dev
        
    Returns:
        float: Standard deviation
    """
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers)
    
    divisor = len(numbers) if population else len(numbers) - 1
    if divisor <= 0:
        raise ValueError("Need at least 2 values for sample standard deviation")
    
    return math.sqrt(variance / divisor)


def distance_2d(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """
    Calculate Euclidean distance between two 2D points.
    
    Args:
        point1 (Tuple[float, float]): First point (x, y)
        point2 (Tuple[float, float]): Second point (x, y)
        
    Returns:
        float: Distance between points
        
    Example:
        >>> distance_2d((0, 0), (3, 4))
        5.0
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def circle_area(radius: float) -> float:
    """
    Calculate area of a circle.
    
    Args:
        radius (float): Circle radius
        
    Returns:
        float: Circle area
        
    Example:
        >>> circle_area(5)
        78.53981633974483
    """
    return math.pi * radius ** 2


def circle_circumference(radius: float) -> float:
    """
    Calculate circumference of a circle.
    
    Args:
        radius (float): Circle radius
        
    Returns:
        float: Circle circumference
    """
    return 2 * math.pi * radius


def triangle_area(base: float, height: float) -> float:
    """
    Calculate area of a triangle.
    
    Args:
        base (float): Triangle base
        height (float): Triangle height
        
    Returns:
        float: Triangle area
    """
    return 0.5 * base * height


def rectangle_area(width: float, height: float) -> float:
    """
    Calculate area of a rectangle.
    
    Args:
        width (float): Rectangle width
        height (float): Rectangle height
        
    Returns:
        float: Rectangle area
    """
    return width * height


def is_power_of_two(n: int) -> bool:
    """
    Check if a number is a power of two.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a power of two
        
    Example:
        >>> is_power_of_two(16)
        True
    """
    return n > 0 and (n & (n - 1)) == 0


def digit_sum(n: int) -> int:
    """
    Calculate sum of digits in a number.
    
    Args:
        n (int): Input number
        
    Returns:
        int: Sum of digits
        
    Example:
        >>> digit_sum(12345)
        15
    """
    return sum(int(digit) for digit in str(abs(n)))


def reverse_number(n: int) -> int:
    """
    Reverse the digits of a number.
    
    Args:
        n (int): Input number
        
    Returns:
        int: Number with reversed digits
        
    Example:
        >>> reverse_number(12345)
        54321
    """
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def is_armstrong_number(n: int) -> bool:
    """
    Check if a number is an Armstrong number (narcissistic number).
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is Armstrong number
        
    Example:
        >>> is_armstrong_number(153)
        True
    """
    digits = str(abs(n))
    num_digits = len(digits)
    digit_sum_pow = sum(int(digit) ** num_digits for digit in digits)
    return digit_sum_pow == abs(n)


def greatest_common_divisor_list(numbers: List[int]) -> int:
    """
    Find GCD of a list of numbers.
    
    Args:
        numbers (List[int]): List of integers
        
    Returns:
        int: Greatest common divisor
    """
    if not numbers:
        raise ValueError("Cannot find GCD of empty list")
    return reduce(gcd, numbers)


def least_common_multiple_list(numbers: List[int]) -> int:
    """
    Find LCM of a list of numbers.
    
    Args:
        numbers (List[int]): List of integers
        
    Returns:
        int: Least common multiple
    """
    if not numbers:
        raise ValueError("Cannot find LCM of empty list")
    return reduce(lcm, numbers)


def clamp(value: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
    """
    Clamp a value between minimum and maximum bounds.
    
    Args:
        value: Value to clamp
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        
    Returns:
        Clamped value
        
    Example:
        >>> clamp(15, 10, 20)
        15
        >>> clamp(5, 10, 20)
        10
    """
    return max(min_val, min(max_val, value))
