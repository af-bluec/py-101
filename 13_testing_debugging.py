"""
Testing and Debugging in Python
Demonstrates unit testing, debugging techniques, and code profiling
"""

import unittest
import doctest
import time
import traceback
import logging
from typing import List


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# FUNCTIONS TO TEST
# ============================================================================

def add(a: int, b: int) -> int:
    """
    Add two numbers.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b


def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    >>> divide(10, 2)
    5.0
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("A man a plan a canal Panama")
    True
    """
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def factorial(n: int) -> int:
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def find_max(numbers: List[int]) -> int:
    """Find maximum number in a list"""
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)


# ============================================================================
# UNIT TESTS
# ============================================================================

class TestMathFunctions(unittest.TestCase):
    """Test cases for mathematical functions"""
    
    def setUp(self):
        """Set up test fixtures - runs before each test"""
        self.test_numbers = [1, 2, 3, 4, 5]
        logger.info("Setting up test")
    
    def tearDown(self):
        """Clean up after each test"""
        logger.info("Tearing down test")
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, 3), -2)
    
    def test_divide_normal(self):
        """Test normal division"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(10, 3), 3.333, places=3)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception"""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_factorial(self):
        """Test factorial calculation"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_negative(self):
        """Test factorial with negative number"""
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_find_max(self):
        """Test finding maximum"""
        self.assertEqual(find_max([1, 5, 3, 2]), 5)
        self.assertEqual(find_max([-1, -5, -3]), -1)
    
    def test_find_max_empty_list(self):
        """Test finding max in empty list"""
        with self.assertRaises(ValueError):
            find_max([])


class TestStringFunctions(unittest.TestCase):
    """Test cases for string functions"""
    
    def test_palindrome_simple(self):
        """Test simple palindromes"""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("noon"))
        self.assertFalse(is_palindrome("hello"))
    
    def test_palindrome_case_insensitive(self):
        """Test palindrome is case-insensitive"""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Noon"))
    
    def test_palindrome_with_spaces(self):
        """Test palindrome with spaces"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("race car"))


# ============================================================================
# ASSERTIONS AND DEBUGGING
# ============================================================================

def demonstrate_assertions():
    """Demonstrate assertion usage"""
    print("=" * 60)
    print("ASSERTIONS")
    print("=" * 60)
    
    # Basic assertions
    x = 10
    assert x > 0, "x must be positive"
    print(f"✓ Assertion passed: x={x} is positive")
    
    # Assertions in functions
    def calculate_average(numbers):
        assert len(numbers) > 0, "List cannot be empty"
        return sum(numbers) / len(numbers)
    
    avg = calculate_average([1, 2, 3, 4, 5])
    print(f"✓ Average: {avg}")
    
    # Assertions can be disabled with -O flag
    print("\nNote: Run with 'python -O' to disable assertions")
    
    print()


def demonstrate_logging():
    """Demonstrate logging for debugging"""
    print("=" * 60)
    print("LOGGING")
    print("=" * 60)
    
    # Different log levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Logging with variables
    user = "John"
    action = "login"
    logger.info(f"User {user} performed {action}")
    
    # Logging exceptions
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.exception("Division by zero occurred")
    
    print()


def demonstrate_debugging_techniques():
    """Demonstrate various debugging techniques"""
    print("=" * 60)
    print("DEBUGGING TECHNIQUES")
    print("=" * 60)
    
    # 1. Print debugging (simple but effective)
    def buggy_function(x):
        print(f"DEBUG: x = {x}")  # Debug print
        result = x * 2
        print(f"DEBUG: result = {result}")  # Debug print
        return result
    
    print("1. Print debugging:")
    buggy_function(5)
    
    # 2. Using repr() for detailed output
    data = "hello\nworld"
    print(f"\n2. Using repr(): {repr(data)}")
    
    # 3. Inspecting variables
    print("\n3. Variable inspection:")
    x = [1, 2, 3]
    print(f"Type: {type(x)}")
    print(f"Length: {len(x)}")
    print(f"ID: {id(x)}")
    
    # 4. Stack traces
    print("\n4. Stack trace example:")
    try:
        def func_a():
            func_b()
        
        def func_b():
            func_c()
        
        def func_c():
            raise ValueError("Something went wrong!")
        
        func_a()
    except ValueError as e:
        print(f"Error: {e}")
        print("\nStack trace:")
        traceback.print_exc()
    
    print()


def demonstrate_profiling():
    """Demonstrate code profiling"""
    print("=" * 60)
    print("PROFILING")
    print("=" * 60)
    
    # Simple timing
    def slow_function():
        total = 0
        for i in range(1000000):
            total += i
        return total
    
    start = time.time()
    result = slow_function()
    end = time.time()
    print(f"Execution time: {end - start:.4f} seconds")
    
    # Timing decorator
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper
    
    @timer
    def another_function():
        return sum(range(1000000))
    
    print("\nUsing timer decorator:")
    another_function()
    
    # Memory profiling concept
    print("\nMemory profiling:")
    import sys
    data = [i for i in range(10000)]
    print(f"List size: {sys.getsizeof(data)} bytes")
    
    print()


def demonstrate_test_driven_development():
    """Demonstrate TDD concept"""
    print("=" * 60)
    print("TEST-DRIVEN DEVELOPMENT (TDD)")
    print("=" * 60)
    
    tdd_process = """
TDD Process:
1. Write a failing test
2. Write minimal code to pass the test
3. Refactor the code
4. Repeat

Example:
# Step 1: Write test first
def test_reverse_string():
    assert reverse_string("hello") == "olleh"

# Step 2: Implement function
def reverse_string(s):
    return s[::-1]

# Step 3: Run test - it passes!
# Step 4: Refactor if needed
"""
    print(tdd_process)
    print()


def demonstrate_mocking():
    """Demonstrate mocking concept"""
    print("=" * 60)
    print("MOCKING")
    print("=" * 60)
    
    print("""
Mocking is used to replace parts of your system with mock objects
and make assertions about how they were used.

Example with unittest.mock:

from unittest.mock import Mock, patch

# Mock an object
mock_api = Mock()
mock_api.get_data.return_value = {"status": "success"}

# Use the mock
result = mock_api.get_data()
assert result["status"] == "success"

# Verify it was called
mock_api.get_data.assert_called_once()

# Patch a function
@patch('module.external_api_call')
def test_function(mock_api):
    mock_api.return_value = "mocked response"
    # Test your code that uses external_api_call
""")
    print()


def demonstrate_best_practices():
    """Testing best practices"""
    print("=" * 60)
    print("TESTING BEST PRACTICES")
    print("=" * 60)
    
    best_practices = """
1. Test Organization:
   ✓ One test class per class/module
   ✓ One test method per behavior
   ✓ Use descriptive test names

2. Test Independence:
   ✓ Tests should not depend on each other
   ✓ Use setUp/tearDown for test fixtures
   ✓ Clean up resources after tests

3. Test Coverage:
   ✓ Test normal cases
   ✓ Test edge cases
   ✓ Test error conditions
   ✓ Aim for high coverage (80%+)

4. Assertions:
   ✓ One logical assertion per test
   ✓ Use specific assertion methods
   ✓ Include helpful error messages

5. Test Data:
   ✓ Use realistic test data
   ✓ Avoid hardcoded values when possible
   ✓ Use fixtures for complex data

6. Debugging:
   ✓ Use logging instead of print
   ✓ Write tests to reproduce bugs
   ✓ Use debugger (pdb) for complex issues
   ✓ Profile performance bottlenecks

7. Continuous Testing:
   ✓ Run tests frequently
   ✓ Automate testing in CI/CD
   ✓ Fix failing tests immediately
"""
    print(best_practices)
    print()


def demonstrate_doctest():
    """Demonstrate doctest usage"""
    print("=" * 60)
    print("DOCTEST")
    print("=" * 60)
    
    print("Running doctests for module functions...")
    print()
    
    # Run doctests
    results = doctest.testmod(verbose=False)
    
    if results.failed == 0:
        print(f"✓ All {results.attempted} doctests passed!")
    else:
        print(f"✗ {results.failed} of {results.attempted} doctests failed")
    
    print()


def run_unit_tests():
    """Run all unit tests"""
    print("=" * 60)
    print("RUNNING UNIT TESTS")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestMathFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestStringFunctions))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.wasSuccessful()}")
    print("=" * 60)
    
    return result.wasSuccessful()


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 60)
    print("PYTHON TESTING AND DEBUGGING SHOWCASE")
    print("=" * 60 + "\n")
    
    demonstrate_assertions()
    demonstrate_logging()
    demonstrate_debugging_techniques()
    demonstrate_profiling()
    demonstrate_doctest()
    demonstrate_test_driven_development()
    demonstrate_mocking()
    demonstrate_best_practices()
    
    print("\n" + "=" * 60)
    print("Now running unit tests...")
    print("=" * 60 + "\n")
    
    success = run_unit_tests()
    
    print("\n" + "=" * 60)
    print("Testing and debugging demonstration complete!")
    print("=" * 60)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
