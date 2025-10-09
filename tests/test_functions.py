"""
Basic tests for utility functions.

This module provides simple tests to verify the functionality of various
utility functions. Not a comprehensive test suite, but basic validation.
"""

import sys
import os

# Add the parent directory to sys.path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import string_utils, math_utils, data_structures, validators


def test_string_utils():
    """Test string utility functions."""
    print("Testing String Utils...")
    
    # Test clean_text
    assert string_utils.clean_text("  hello   world  ") == "hello world"
    
    # Test is_palindrome
    assert string_utils.is_palindrome("racecar") == True
    assert string_utils.is_palindrome("hello") == False
    
    # Test count_words
    assert string_utils.count_words("hello world test") == 3
    
    # Test capitalize_words
    assert string_utils.capitalize_words("hello world") == "Hello World"
    
    # Test reverse_string
    assert string_utils.reverse_string("hello") == "olleh"
    
    print("✓ String Utils tests passed")


def test_math_utils():
    """Test mathematical utility functions."""
    print("Testing Math Utils...")
    
    # Test gcd
    assert math_utils.gcd(48, 18) == 6
    
    # Test lcm
    assert math_utils.lcm(4, 6) == 12
    
    # Test is_perfect_square
    assert math_utils.is_perfect_square(16) == True
    assert math_utils.is_perfect_square(15) == False
    
    # Test factorial
    assert math_utils.factorial_iterative(5) == 120
    
    # Test fibonacci
    assert math_utils.fibonacci_nth(6) == 8
    
    # Test mean
    assert math_utils.mean([1, 2, 3, 4, 5]) == 3.0
    
    # Test is_power_of_two
    assert math_utils.is_power_of_two(8) == True
    assert math_utils.is_power_of_two(9) == False
    
    print("✓ Math Utils tests passed")


def test_data_structures():
    """Test data structure utility functions."""
    print("Testing Data Structures...")
    
    # Test flatten_list
    nested = [[1, 2], [3, 4]]
    assert data_structures.flatten_list(nested) == [1, 2, 3, 4]
    
    # Test remove_duplicates
    assert data_structures.remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
    
    # Test merge_dicts
    dict1 = {"a": 1}
    dict2 = {"b": 2}
    merged = data_structures.merge_dicts(dict1, dict2)
    assert merged == {"a": 1, "b": 2}
    
    # Test chunk_list
    chunks = data_structures.chunk_list([1, 2, 3, 4, 5, 6], 2)
    assert chunks == [[1, 2], [3, 4], [5, 6]]
    
    # Test transpose_matrix
    matrix = [[1, 2], [3, 4]]
    transposed = data_structures.transpose_matrix(matrix)
    assert transposed == [[1, 3], [2, 4]]
    
    # Test rotate_list
    rotated = data_structures.rotate_list([1, 2, 3, 4, 5], 2)
    assert rotated == [4, 5, 1, 2, 3]
    
    print("✓ Data Structures tests passed")


def test_validators():
    """Test validation functions."""
    print("Testing Validators...")
    
    # Test email validation
    assert validators.is_valid_email("test@example.com") == True
    assert validators.is_valid_email("invalid-email") == False
    
    # Test URL validation
    assert validators.is_valid_url("https://www.example.com") == True
    assert validators.is_valid_url("not-a-url") == False
    
    # Test numeric validation
    assert validators.is_numeric("123") == True
    assert validators.is_numeric("123.45") == True
    assert validators.is_numeric("abc") == False
    
    # Test range validation
    assert validators.is_in_range(5, 1, 10) == True
    assert validators.is_in_range(15, 1, 10) == False
    
    # Test length validation
    assert validators.is_valid_length("hello", 3, 10) == True
    assert validators.is_valid_length("hi", 3, 10) == False
    
    # Test alphanumeric
    assert validators.contains_only_alphanumeric("hello123") == True
    assert validators.contains_only_alphanumeric("hello@123") == False
    
    print("✓ Validators tests passed")


def run_all_tests():
    """Run all test functions."""
    print("=== RUNNING BASIC TESTS ===\n")
    
    try:
        test_string_utils()
        test_math_utils()
        test_data_structures()
        test_validators()
        
        print("\n🎉 All tests passed successfully!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False
    
    return True


def demo_function_usage():
    """Demonstrate some function usage."""
    print("\n=== FUNCTION USAGE DEMO ===\n")
    
    # String processing demo
    text = "  The Quick BROWN fox jumps  "
    print(f"Original text: '{text}'")
    print(f"Cleaned: '{string_utils.clean_text(text)}'")
    print(f"Capitalized: '{string_utils.capitalize_words(text.lower())}'")
    print(f"Word count: {string_utils.count_words(text)}")
    
    # Math demo
    print(f"\nMath operations:")
    print(f"GCD(48, 18) = {math_utils.gcd(48, 18)}")
    print(f"LCM(4, 6) = {math_utils.lcm(4, 6)}")
    print(f"Fibonacci(10) = {math_utils.fibonacci_nth(10)}")
    
    # Data structures demo
    print(f"\nData structure operations:")
    data = [1, 2, 3, 2, 1, 4, 5]
    print(f"Original: {data}")
    print(f"Unique: {data_structures.remove_duplicates(data)}")
    print(f"Chunks of 3: {data_structures.chunk_list(data, 3)}")
    
    # Validation demo
    print(f"\nValidation examples:")
    test_email = "user@example.com"
    print(f"'{test_email}' is valid email: {validators.is_valid_email(test_email)}")
    print(f"'123.45' is numeric: {validators.is_numeric('123.45')}")
    print(f"5 is in range 1-10: {validators.is_in_range(5, 1, 10)}")


if __name__ == "__main__":
    # Run tests
    success = run_all_tests()
    
    if success:
        # Show demo if tests pass
        demo_function_usage()
    else:
        print("\nTests failed - skipping demo")
        sys.exit(1)
