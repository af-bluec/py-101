"""
Unit tests for the utils module.
"""

import pytest
from py101.utils import (
    greet, 
    generate_random_number, 
    string_operations,
    set_operations, 
    list_operations, 
    apply_lambda_operations,
    tuple_operations, 
    get_quadrant
)


class TestUtilityFunctions:
    """Test cases for utility functions."""
    
    def test_greet(self):
        """Test greeting function."""
        assert greet("Alice") == "Hello, Alice!"
        assert greet("World") == "Hello, World!"
        assert greet("") == "Hello, !"
    
    def test_generate_random_number(self):
        """Test random number generation."""
        # Test default range
        num = generate_random_number()
        assert 1 <= num <= 100
        
        # Test custom range
        num = generate_random_number(5, 10)
        assert 5 <= num <= 10
        
        # Test single number range
        num = generate_random_number(7, 7)
        assert num == 7
    
    def test_string_operations(self):
        """Test string operations."""
        result = string_operations("Hello World")
        
        assert result['uppercase'] == "HELLO WORLD"
        assert result['lowercase'] == "hello world"
        assert result['length'] == 11
        assert result['reversed'] == "dlroW olleH"
        assert result['words'] == ["Hello", "World"]
        assert result['capitalized'] == "Hello world"
    
    def test_string_operations_empty(self):
        """Test string operations with empty string."""
        result = string_operations("")
        
        assert result['uppercase'] == ""
        assert result['lowercase'] == ""
        assert result['length'] == 0
        assert result['reversed'] == ""
        assert result['words'] == []
        assert result['capitalized'] == ""
    
    def test_set_operations(self):
        """Test set operations."""
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        
        result = set_operations(set1, set2)
        
        assert result['union'] == {1, 2, 3, 4, 5}
        assert result['intersection'] == {3}
        assert result['difference'] == {1, 2}
        assert result['symmetric_difference'] == {1, 2, 4, 5}
    
    def test_list_operations(self):
        """Test list operations."""
        numbers = [1, 2, 3, 4, 5]
        result = list_operations(numbers)
        
        assert result['sum'] == 15
        assert result['average'] == 3.0
        assert result['max'] == 5
        assert result['min'] == 1
        assert result['sorted'] == [1, 2, 3, 4, 5]
        assert result['reversed'] == [5, 4, 3, 2, 1]
        assert result['squared'] == [1, 4, 9, 16, 25]
        assert result['evens'] == [2, 4]
        assert result['odds'] == [1, 3, 5]
    
    def test_list_operations_empty(self):
        """Test list operations with empty list."""
        result = list_operations([])
        assert 'error' in result
        assert result['error'] == 'Empty list provided'
    
    def test_apply_lambda_operations(self):
        """Test lambda operations."""
        numbers = [1, 2, 3, 4]
        result = apply_lambda_operations(numbers)
        
        assert result['doubled'] == [2, 4, 6, 8]
        assert result['evens'] == [2, 4]
        assert result['product'] == 24
        assert result['squares'] == [1, 4, 9, 16]
    
    def test_apply_lambda_operations_empty(self):
        """Test lambda operations with empty list."""
        result = apply_lambda_operations([])
        
        assert result['doubled'] == []
        assert result['evens'] == []
        assert result['product'] == 0
        assert result['squares'] == []
    
    def test_tuple_operations(self):
        """Test tuple operations."""
        point = (3, 4)
        result = tuple_operations(point)
        
        assert result['x'] == 3
        assert result['y'] == 4
        assert result['distance_from_origin'] == 5.0
        assert result['quadrant'] == "First quadrant"
    
    def test_get_quadrant(self):
        """Test quadrant determination."""
        assert get_quadrant(1, 1) == "First quadrant"
        assert get_quadrant(-1, 1) == "Second quadrant"
        assert get_quadrant(-1, -1) == "Third quadrant"
        assert get_quadrant(1, -1) == "Fourth quadrant"
        assert get_quadrant(0, 1) == "On axis"
        assert get_quadrant(1, 0) == "On axis"
        assert get_quadrant(0, 0) == "On axis"
