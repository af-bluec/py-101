"""
Calculator module providing basic arithmetic operations.

This module contains a Calculator class that performs basic
mathematical operations like addition and subtraction.
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """
    A simple calculator class for basic arithmetic operations.
    
    This class provides methods for addition, subtraction, multiplication,
    and division operations.
    """
    
    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers.
        
        Args:
            a (Number): First number
            b (Number): Second number
            
        Returns:
            Number: Sum of a and b
        """
        return a + b
    
    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract second number from first number.
        
        Args:
            a (Number): First number (minuend)
            b (Number): Second number (subtrahend)
            
        Returns:
            Number: Difference of a and b
        """
        return a - b
    
    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers.
        
        Args:
            a (Number): First number
            b (Number): Second number
            
        Returns:
            Number: Product of a and b
        """
        return a * b
    
    def divide(self, a: Number, b: Number) -> Number:
        """
        Divide first number by second number.
        
        Args:
            a (Number): Dividend
            b (Number): Divisor
            
        Returns:
            Number: Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    def power(self, base: Number, exponent: Number) -> Number:
        """
        Raise base to the power of exponent.
        
        Args:
            base (Number): Base number
            exponent (Number): Exponent
            
        Returns:
            Number: base raised to the power of exponent
        """
        return base ** exponent
