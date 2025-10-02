"""
Calculator class module.

This module contains a simple Calculator class with basic arithmetic operations.
"""


class Calculator:
    """
    A simple calculator class with basic arithmetic operations.
    """
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtract two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divide two numbers.
        
        Args:
            a (float): Dividend
            b (float): Divisor
            
        Returns:
            float: Quotient of a and b
            
        Raises:
            ValueError: If divisor is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """
        Calculate power of a number.
        
        Args:
            base (float): Base number
            exponent (float): Exponent
            
        Returns:
            float: base raised to the power of exponent
        """
        return base ** exponent


# Lambda functions for quick operations
multiply_lambda = lambda x, y: x * y
square_lambda = lambda x: x ** 2
is_even_lambda = lambda x: x % 2 == 0
