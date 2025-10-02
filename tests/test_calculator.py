"""
Unit tests for the calculator module.
"""

import pytest
from py101.calculator import Calculator


class TestCalculator:
    """Test cases for the Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operations."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 1.5) == 4.0
    
    def test_subtraction(self):
        """Test subtraction operations."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(-2, -3) == 1
        assert self.calc.subtract(4.5, 1.5) == 3.0
    
    def test_multiplication(self):
        """Test multiplication operations."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 5) == -10
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(2.5, 4) == 10.0
    
    def test_division(self):
        """Test division operations."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-6, 3) == -2
        assert self.calc.divide(0, 5) == 0
    
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            self.calc.divide(10, 0)
        
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            self.calc.divide(0, 0)
    
    def test_power(self):
        """Test power operations."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(3, 2) == 9
        assert self.calc.power(4, 0.5) == 2.0
        assert self.calc.power(-2, 3) == -8
    
    def test_power_with_negative_exponent(self):
        """Test power with negative exponent."""
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(4, -2) == 0.0625
