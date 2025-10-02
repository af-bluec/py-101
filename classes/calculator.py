"""
Calculator class with basic arithmetic operations.
"""
from typing import Union

Number = Union[int, float]


class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract second number from first.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            Difference of a and b
        """
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        result = a * b
        self._record_operation(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Number, b: Number) -> Number:
        """
        Divide first number by second.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        
        result = a / b
        self._record_operation(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Number, exponent: Number) -> Number:
        """
        Raise base to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base raised to the power of exponent
        """
        result = base ** exponent
        self._record_operation(f"{base} ^ {exponent} = {result}")
        return result
    
    def sqrt(self, number: Number) -> float:
        """
        Calculate square root of a number.
        
        Args:
            number: Number to find square root of
            
        Returns:
            Square root of the number
            
        Raises:
            ValueError: If number is negative
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = number ** 0.5
        self._record_operation(f"√{number} = {result}")
        return result
    
    def get_history(self) -> list:
        """
        Get the calculation history.
        
        Returns:
            List of calculation strings
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()
    
    def _record_operation(self, operation: str) -> None:
        """
        Record an operation in history (private method).
        
        Args:
            operation: String representation of the operation
        """
        self.history.append(operation)


class ScientificCalculator(Calculator):
    """
    Extended calculator with scientific functions.
    """
    
    def __init__(self):
        """Initialize the scientific calculator."""
        super().__init__()
        import math
        self.math = math
    
    def sin(self, angle: Number, degrees: bool = False) -> float:
        """
        Calculate sine of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; if False, in radians
            
        Returns:
            Sine of the angle
        """
        if degrees:
            angle = self.math.radians(angle)
        result = self.math.sin(angle)
        unit = "°" if degrees else "rad"
        self._record_operation(f"sin({angle}{unit}) = {result}")
        return result
    
    def cos(self, angle: Number, degrees: bool = False) -> float:
        """
        Calculate cosine of an angle.
        
        Args:
            angle: Angle value
            degrees: If True, angle is in degrees; if False, in radians
            
        Returns:
            Cosine of the angle
        """
        if degrees:
            angle = self.math.radians(angle)
        result = self.math.cos(angle)
        unit = "°" if degrees else "rad"
        self._record_operation(f"cos({angle}{unit}) = {result}")
        return result
    
    def log(self, number: Number, base: Number = 10) -> float:
        """
        Calculate logarithm of a number.
        
        Args:
            number: Number to find logarithm of
            base: Base of logarithm (default: 10)
            
        Returns:
            Logarithm of the number
            
        Raises:
            ValueError: If number <= 0 or base <= 0 or base == 1
        """
        if number <= 0:
            raise ValueError("Number must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1")
        
        result = self.math.log(number) / self.math.log(base)
        self._record_operation(f"log_{base}({number}) = {result}")
        return result
