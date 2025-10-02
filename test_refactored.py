"""
Test suite for the refactored Python demo application.

This module contains unit tests for all the utility modules to ensure
functionality is preserved after refactoring.
"""

import unittest
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils.math_operations import factorial, is_prime, fibonacci_sequence, divide
from utils.calculator import Calculator
from utils.string_operations import demonstrate_string_operations, format_person_info
from utils.data_structures import demonstrate_lists, demonstrate_dictionaries
from utils.constants import PI, E


class TestMathOperations(unittest.TestCase):
    """Test cases for mathematical operations."""
    
    def test_factorial(self):
        """Test factorial function."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_is_prime(self):
        """Test prime number checking."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
    
    def test_fibonacci_sequence(self):
        """Test Fibonacci sequence generation."""
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        
        with self.assertRaises(ValueError):
            fibonacci_sequence(0)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test calculator instance."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)


class TestStringOperations(unittest.TestCase):
    """Test cases for string operations."""
    
    def test_demonstrate_string_operations(self):
        """Test string operations demonstration."""
        result = demonstrate_string_operations("Test")
        
        self.assertEqual(result["original"], "Test")
        self.assertEqual(result["uppercase"], "TEST")
        self.assertEqual(result["lowercase"], "test")
        self.assertEqual(result["length"], 4)
    
    def test_format_person_info(self):
        """Test person info formatting."""
        result = format_person_info("Alice", 30)
        self.assertEqual(result, "Alice is 30 years old.")


class TestDataStructures(unittest.TestCase):
    """Test cases for data structure operations."""
    
    def test_demonstrate_lists(self):
        """Test list operations."""
        result = demonstrate_lists()
        
        self.assertEqual(result["squares"], [1, 4, 9, 16, 25])
        self.assertIn("apple", result["fruits"])
        self.assertEqual(result["product"], 24)
    
    def test_demonstrate_dictionaries(self):
        """Test dictionary operations."""
        result = demonstrate_dictionaries()
        
        self.assertEqual(result["person"]["name"], "Alice")
        self.assertEqual(result["average_score"], 91.5)


class TestConstants(unittest.TestCase):
    """Test cases for constants."""
    
    def test_constants_values(self):
        """Test that constants have expected values."""
        self.assertAlmostEqual(PI, 3.14159, places=4)
        self.assertAlmostEqual(E, 2.71828, places=4)


if __name__ == '__main__':
    unittest.main()
