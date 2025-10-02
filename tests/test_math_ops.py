"""
Unit tests for the math_ops module.
"""

import pytest
from py101.math_ops import factorial, is_prime, fibonacci_sequence


class TestFactorial:
    """Test cases for the factorial function."""
    
    def test_factorial_zero(self):
        """Test factorial of 0."""
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        """Test factorial of 1."""
        assert factorial(1) == 1
    
    def test_factorial_positive(self):
        """Test factorial of positive numbers."""
        assert factorial(5) == 120
        assert factorial(3) == 6
        assert factorial(4) == 24
    
    def test_factorial_negative(self):
        """Test factorial raises error for negative numbers."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
    
    def test_factorial_non_integer(self):
        """Test factorial raises error for non-integers."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            factorial(3.5)
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            factorial("5")


class TestIsPrime:
    """Test cases for the is_prime function."""
    
    def test_prime_numbers(self):
        """Test recognition of prime numbers."""
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(17) == True
        assert is_prime(29) == True
    
    def test_non_prime_numbers(self):
        """Test recognition of non-prime numbers."""
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(15) == False
        assert is_prime(25) == False
    
    def test_negative_and_zero(self):
        """Test that negative numbers and zero are not prime."""
        assert is_prime(0) == False
        assert is_prime(-1) == False
        assert is_prime(-5) == False
    
    def test_non_integer(self):
        """Test that non-integers raise TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer"):
            is_prime(3.5)
        
        with pytest.raises(TypeError, match="Input must be an integer"):
            is_prime("5")


class TestFibonacciSequence:
    """Test cases for the fibonacci_sequence function."""
    
    def test_fibonacci_length_one(self):
        """Test Fibonacci sequence of length 1."""
        assert fibonacci_sequence(1) == [0]
    
    def test_fibonacci_length_two(self):
        """Test Fibonacci sequence of length 2."""
        assert fibonacci_sequence(2) == [0, 1]
    
    def test_fibonacci_longer_sequences(self):
        """Test longer Fibonacci sequences."""
        assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
        assert fibonacci_sequence(8) == [0, 1, 1, 2, 3, 5, 8, 13]
        assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_fibonacci_invalid_length(self):
        """Test that invalid lengths raise appropriate errors."""
        with pytest.raises(ValueError, match="Length must be at least 1"):
            fibonacci_sequence(0)
        
        with pytest.raises(ValueError, match="Length must be at least 1"):
            fibonacci_sequence(-1)
    
    def test_fibonacci_non_integer_length(self):
        """Test that non-integer lengths raise TypeError."""
        with pytest.raises(TypeError, match="Length must be an integer"):
            fibonacci_sequence(3.5)
        
        with pytest.raises(TypeError, match="Length must be an integer"):
            fibonacci_sequence("5")
