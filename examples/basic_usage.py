#!/usr/bin/env python3
"""
Basic usage example for py101 package.

This script demonstrates how to use the main features
of the py101 package in your own projects.
"""

from py101 import (
    Calculator, 
    factorial, 
    is_prime, 
    fibonacci_sequence,
    greet,
    string_operations
)


def main():
    """Main example function."""
    print("=== py101 Package Usage Examples ===\n")
    
    # Mathematical operations
    print("1. Mathematical Operations:")
    print(f"   Factorial of 6: {factorial(6)}")
    print(f"   Is 29 prime? {is_prime(29)}")
    print(f"   First 8 Fibonacci numbers: {fibonacci_sequence(8)}")
    print()
    
    # Calculator usage
    print("2. Calculator Operations:")
    calc = Calculator()
    print(f"   15 + 7 = {calc.add(15, 7)}")
    print(f"   15 - 7 = {calc.subtract(15, 7)}")
    print(f"   15 * 7 = {calc.multiply(15, 7)}")
    print(f"   15 / 7 = {calc.divide(15, 7):.2f}")
    print(f"   2 ** 8 = {calc.power(2, 8)}")
    print()
    
    # String operations
    print("3. String Operations:")
    text = "Python Programming"
    ops = string_operations(text)
    print(f"   Original: '{text}'")
    print(f"   Uppercase: '{ops['uppercase']}'")
    print(f"   Length: {ops['length']}")
    print(f"   Words: {ops['words']}")
    print()
    
    # Utility functions
    print("4. Utility Functions:")
    print(f"   {greet('Developer')}")
    
    print("\n=== Examples completed successfully! ===")


if __name__ == "__main__":
    main()
