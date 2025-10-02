"""
Demonstration functions showcasing various Python concepts.
"""
import random
from datetime import date
from typing import Any, Dict, List


def demonstrate_control_flow() -> Dict[str, Any]:
    """
    Demonstrate various control flow constructs.
    
    Returns:
        Dictionary with control flow examples
    """
    results = {}
    
    # Conditional statements
    age = 25
    results['age_category'] = "Adult" if age >= 18 else "Minor"
    
    # For loop with range
    counting = []
    for i in range(1, 6):
        counting.append(f"Count: {i}")
    results['counting'] = counting
    
    # While loop
    countdown = []
    count = 5
    while count > 0:
        countdown.append(f"T-minus {count}")
        count -= 1
    countdown.append("Blast off!")
    results['countdown'] = countdown
    
    # List comprehension with conditional
    numbers = range(1, 11)
    results['even_squares'] = [x**2 for x in numbers if x % 2 == 0]
    
    return results


def demonstrate_error_handling() -> Dict[str, Any]:
    """
    Demonstrate error handling patterns.
    
    Returns:
        Dictionary with error handling examples
    """
    results = {}
    
    # Try-except-else-finally
    try:
        result = 10 / 2
    except ZeroDivisionError:
        results['division_error'] = "Cannot divide by zero!"
    else:
        results['division_result'] = result
    finally:
        results['cleanup'] = "Division operation completed"
    
    # Custom exception handling
    def safe_divide(a, b):
        try:
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        except ValueError as e:
            return f"Error: {e}"
    
    results['safe_division_valid'] = safe_divide(10, 2)
    results['safe_division_invalid'] = safe_divide(10, 0)
    
    # File handling simulation
    try:
        # Simulate file not found
        raise FileNotFoundError("File not found")
    except FileNotFoundError:
        results['file_operation'] = "File not found - using default content"
    
    return results


def demonstrate_functional_programming() -> Dict[str, Any]:
    """
    Demonstrate functional programming concepts.
    
    Returns:
        Dictionary with functional programming examples
    """
    numbers = [1, 2, 3, 4, 5]
    
    # Lambda functions
    multiply = lambda x, y: x * y
    square = lambda x: x ** 2
    is_even = lambda x: x % 2 == 0
    
    # Map, filter, and functional operations
    results = {
        'original_numbers': numbers,
        'squared': list(map(square, numbers)),
        'doubled': list(map(lambda x: x * 2, numbers)),
        'evens_only': list(filter(is_even, numbers)),
        'multiply_example': multiply(4, 7),
        'sum_all': sum(numbers),
        'max_value': max(numbers),
        'min_value': min(numbers)
    }
    
    # Reduce equivalent using sum
    from functools import reduce
    results['product'] = reduce(lambda x, y: x * y, numbers)
    
    return results


def demonstrate_advanced_features() -> Dict[str, Any]:
    """
    Demonstrate advanced Python features.
    
    Returns:
        Dictionary with advanced feature examples
    """
    results = {}
    
    # Enumerate and zip
    fruits = ['apple', 'banana', 'cherry']
    colors = ['red', 'yellow', 'red']
    
    results['enumerated_fruits'] = list(enumerate(fruits))
    results['fruit_colors'] = list(zip(fruits, colors))
    
    # Set operations (already covered in data_structures, but showing here too)
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    results['set_union'] = set_a | set_b
    results['set_intersection'] = set_a & set_b
    
    # Dictionary comprehension
    results['squared_dict'] = {x: x**2 for x in range(1, 6)}
    
    # Multiple assignment and tuple unpacking
    a, b, c = 1, 2, 3
    results['unpacked_values'] = {'a': a, 'b': b, 'c': c}
    
    # Ternary operator examples
    results['ternary_examples'] = [
        'positive' if x > 0 else 'negative or zero' for x in [-1, 0, 1]
    ]
    
    return results


def demonstrate_string_formatting() -> Dict[str, Any]:
    """
    Demonstrate various string formatting techniques.
    
    Returns:
        Dictionary with string formatting examples
    """
    name = "Alice"
    age = 30
    price = 123.456
    
    return {
        'f_string': f"{name} is {age} years old",
        'format_method': "{} is {} years old".format(name, age),
        'formatted_number': f"Price: ${price:.2f}",
        'padded_string': f"Name: '{name:>10}'",  # Right-aligned in 10 chars
        'percentage': f"Success rate: {0.85:.1%}",
        'scientific_notation': f"Large number: {123456789:.2e}"
    }


def demonstrate_context_management() -> Dict[str, Any]:
    """
    Demonstrate context management concepts.
    
    Returns:
        Dictionary with context management examples
    """
    results = {}
    
    # Simulated context manager
    class SimulatedFile:
        def __init__(self, name):
            self.name = name
            self.closed = False
        
        def __enter__(self):
            results['context_enter'] = f"Opening {self.name}"
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            results['context_exit'] = f"Closing {self.name}"
            self.closed = True
        
        def read(self):
            return "Sample file content"
    
    # Using context manager
    with SimulatedFile("sample.txt") as f:
        content = f.read()
        results['file_content'] = content
    
    results['file_closed'] = f.closed
    
    return results


def demonstrate_random_operations() -> Dict[str, Any]:
    """
    Demonstrate random number operations.
    
    Returns:
        Dictionary with random operation examples
    """
    # Set seed for reproducible results in demonstrations
    random.seed(42)
    
    return {
        'random_int': random.randint(1, 100),
        'random_float': random.random(),
        'random_choice': random.choice(['apple', 'banana', 'cherry']),
        'random_sample': random.sample(range(1, 11), 3),
        'shuffled_list': random.sample([1, 2, 3, 4, 5], 5)  # Like shuffle but returns new list
    }


def demonstrate_date_operations() -> Dict[str, Any]:
    """
    Demonstrate date and time operations.
    
    Returns:
        Dictionary with date operation examples
    """
    today = date.today()
    
    return {
        'today': str(today),
        'year': today.year,
        'month': today.month,
        'day': today.day,
        'weekday': today.strftime('%A'),
        'formatted_date': today.strftime('%B %d, %Y')
    }


def run_all_demonstrations() -> Dict[str, Any]:
    """
    Run all demonstration functions and return combined results.
    
    Returns:
        Dictionary with all demonstration results
    """
    return {
        'control_flow': demonstrate_control_flow(),
        'error_handling': demonstrate_error_handling(),
        'functional_programming': demonstrate_functional_programming(),
        'advanced_features': demonstrate_advanced_features(),
        'string_formatting': demonstrate_string_formatting(),
        'context_management': demonstrate_context_management(),
        'random_operations': demonstrate_random_operations(),
        'date_operations': demonstrate_date_operations()
    }
