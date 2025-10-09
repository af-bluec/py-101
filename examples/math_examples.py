"""
Mathematical utilities examples.

This file demonstrates usage of various mathematical functions.
"""

from utils.math_utils import (
    gcd, lcm, is_perfect_square, generate_primes, factorial_iterative,
    fibonacci_nth, is_perfect_number, mean, median, mode, standard_deviation,
    distance_2d, circle_area, is_power_of_two, digit_sum, is_armstrong_number
)


def run_math_examples():
    """Run examples of mathematical utility functions."""
    
    print("=== MATHEMATICAL UTILITY EXAMPLES ===\n")
    
    # Number theory examples
    print("1. Number Theory:")
    a, b = 48, 18
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
    print(f"Is 16 a perfect square? {is_perfect_square(16)}")
    print(f"Is 15 a perfect square? {is_perfect_square(15)}")
    print()
    
    # Prime numbers
    print("2. Prime Numbers:")
    primes = generate_primes(30)
    print(f"Primes up to 30: {primes}")
    print(f"Is 17 prime? {17 in primes}")
    print(f"Is 18 prime? {18 in primes}\n")
    
    # Factorial and Fibonacci
    print("3. Sequences:")
    n = 8
    print(f"Factorial of {n}: {factorial_iterative(n)}")
    print(f"Fibonacci numbers (first 10):")
    for i in range(10):
        print(f"  F({i}) = {fibonacci_nth(i)}")
    print()
    
    # Perfect numbers
    print("4. Perfect Numbers:")
    test_numbers = [6, 28, 12, 496]
    for num in test_numbers:
        is_perfect = is_perfect_number(num)
        print(f"{num} is perfect: {is_perfect}")
    print()
    
    # Statistics
    print("5. Statistics:")
    data = [10, 15, 20, 25, 30, 25, 20, 15]
    print(f"Data: {data}")
    print(f"Mean: {mean(data):.2f}")
    print(f"Median: {median(data):.2f}")
    print(f"Mode: {mode(data)}")
    print(f"Standard Deviation: {standard_deviation(data):.2f}\n")
    
    # Geometry
    print("6. Geometry:")
    point1 = (0, 0)
    point2 = (3, 4)
    dist = distance_2d(point1, point2)
    print(f"Distance between {point1} and {point2}: {dist}")
    
    radius = 5
    area = circle_area(radius)
    print(f"Area of circle with radius {radius}: {area:.2f}\n")
    
    # Power of two checking
    print("7. Power of Two:")
    test_nums = [1, 2, 4, 8, 15, 16, 32, 33]
    for num in test_nums:
        is_power = is_power_of_two(num)
        print(f"{num} is power of 2: {is_power}")
    print()
    
    # Digit operations
    print("8. Digit Operations:")
    numbers = [12345, 987, 1001]
    for num in numbers:
        digit_sum_result = digit_sum(num)
        print(f"Digit sum of {num}: {digit_sum_result}")
    print()
    
    # Armstrong numbers
    print("9. Armstrong Numbers:")
    test_armstrong = [1, 9, 153, 371, 407, 1634, 123]
    for num in test_armstrong:
        is_armstrong = is_armstrong_number(num)
        print(f"{num} is Armstrong number: {is_armstrong}")
    print()
    
    # Complex calculations
    print("10. Complex Calculations:")
    
    # Calculate compound interest
    principal = 1000
    rate = 0.05
    time = 10
    compound_interest = principal * ((1 + rate) ** time)
    print(f"Compound Interest: ${principal} at {rate*100}% for {time} years = ${compound_interest:.2f}")
    
    # Calculate area of triangle using coordinates
    # Using Heron's formula with distance calculations
    p1, p2, p3 = (0, 0), (4, 0), (2, 3)
    side_a = distance_2d(p1, p2)
    side_b = distance_2d(p2, p3)
    side_c = distance_2d(p3, p1)
    
    # Semi-perimeter
    s = (side_a + side_b + side_c) / 2
    # Heron's formula
    import math
    triangle_area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    
    print(f"Triangle with vertices {p1}, {p2}, {p3}:")
    print(f"  Sides: {side_a:.2f}, {side_b:.2f}, {side_c:.2f}")
    print(f"  Area: {triangle_area:.2f}")


if __name__ == "__main__":
    run_math_examples()
