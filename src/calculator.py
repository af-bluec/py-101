"""
Calculator class for basic arithmetic operations.

This module provides a Calculator class with methods for performing
common mathematical calculations.
"""

from typing import Union


class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract second number from first.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            Difference of a and b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divide first number by second.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If trying to divide by zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """
        Raise base to the power of exponent.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            base raised to the power of exponent
        """
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, n: Union[int, float]) -> float:
        """
        Calculate square root of a number.
        
        Args:
            n: Number to find square root of
            
        Returns:
            Square root of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = n ** 0.5
        self.history.append(f"√{n} = {result}")
        return result
    
    def percentage(self, value: Union[int, float], percent: Union[int, float]) -> Union[int, float]:
        """
        Calculate percentage of a value.
        
        Args:
            value: The base value
            percent: The percentage
            
        Returns:
            Percentage of the value
        """
        result = (value * percent) / 100
        self.history.append(f"{percent}% of {value} = {result}")
        return result
    
    def get_history(self) -> list:
        """
        Get calculation history.
        
        Returns:
            List of calculation strings
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()


class ScientificCalculator(Calculator):
    """Extended calculator with scientific functions."""
    
    def sin(self, x: Union[int, float]) -> float:
        """Calculate sine (requires math import in usage)."""
        import math
        result = math.sin(x)
        self.history.append(f"sin({x}) = {result}")
        return result
    
    def cos(self, x: Union[int, float]) -> float:
        """Calculate cosine (requires math import in usage)."""
        import math
        result = math.cos(x)
        self.history.append(f"cos({x}) = {result}")
        return result
    
    def tan(self, x: Union[int, float]) -> float:
        """Calculate tangent (requires math import in usage)."""
        import math
        result = math.tan(x)
        self.history.append(f"tan({x}) = {result}")
        return result
    
    def log(self, x: Union[int, float], base: Union[int, float] = 10) -> float:
        """Calculate logarithm."""
        import math
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        
        result = math.log(x, base)
        self.history.append(f"log_{base}({x}) = {result}")
        return result
