"""
Basic Python examples and demonstrations.

This module provides simple examples of fundamental Python concepts
for learning and reference purposes.
"""

import random
from src.math_utils import factorial, is_prime, fibonacci_sequence
from src.calculator import Calculator
from src.data_utils import process_text, analyze_list, create_squares_dict


def demonstrate_variables_and_types():
    """Demonstrate basic variable types and operations."""
    print("=== Variables and Types Demo ===")
    
    # Different data types
    name = "Alice"
    age = 30
    height = 5.6
    is_student = False
    
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
    
    # Type conversion
    age_str = str(age)
    print(f"Age as string: '{age_str}' (type: {type(age_str).__name__})")


def demonstrate_control_flow():
    """Demonstrate if statements, loops, and control structures."""
    print("\n=== Control Flow Demo ===")
    
    # Conditional statements
    age = 25
    if age >= 18:
        status = "Adult"
    else:
        status = "Minor"
    print(f"Age {age} -> Status: {status}")
    
    # For loop
    print("Counting 1 to 5:")
    for i in range(1, 6):
        print(f"  {i}")
    
    # While loop
    print("Countdown from 3:")
    count = 3
    while count > 0:
        print(f"  {count}")
        count -= 1
    print("  Blast off!")


def demonstrate_data_structures():
    """Demonstrate lists, dictionaries, sets, and tuples."""
    print("\n=== Data Structures Demo ===")
    
    # Lists
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Fruits: {fruits}")
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    fruits.append("elderberry")
    print(f"After adding elderberry: {fruits}")
    
    # Dictionaries
    person = {"name": "Bob", "age": 28, "city": "New York"}
    print(f"Person: {person}")
    print(f"Person's name: {person['name']}")
    
    # Sets
    numbers = {1, 2, 3, 4, 5}
    more_numbers = {4, 5, 6, 7, 8}
    print(f"Set 1: {numbers}")
    print(f"Set 2: {more_numbers}")
    print(f"Union: {numbers | more_numbers}")
    print(f"Intersection: {numbers & more_numbers}")
    
    # Tuples
    coordinates = (10, 20)
    x, y = coordinates  # Tuple unpacking
    print(f"Point: ({x}, {y})")


def demonstrate_functions():
    """Demonstrate function usage and examples."""
    print("\n=== Functions Demo ===")
    
    # Using math utilities
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 15 prime? {is_prime(15)}")
    
    fib_sequence = fibonacci_sequence(8)
    print(f"First 8 Fibonacci numbers: {fib_sequence}")
    
    # Using calculator
    calc = Calculator()
    result1 = calc.add(10, 5)
    result2 = calc.multiply(4, 7)
    print(f"10 + 5 = {result1}")
    print(f"4 * 7 = {result2}")


def demonstrate_string_operations():
    """Demonstrate string manipulation."""
    print("\n=== String Operations Demo ===")
    
    text = "Python Programming"
    text_info = process_text(text)
    
    for key, value in text_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def demonstrate_list_operations():
    """Demonstrate list comprehensions and operations."""
    print("\n=== List Operations Demo ===")
    
    # List comprehensions
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")
    
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers 0-9: {evens}")
    
    # List analysis
    numbers = [10, 23, 5, 78, 12, 45, 33]
    stats = analyze_list(numbers)
    print(f"Numbers: {numbers}")
    print(f"Statistics: {stats}")


def demonstrate_error_handling():
    """Demonstrate basic error handling."""
    print("\n=== Error Handling Demo ===")
    
    # Try-except block
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    
    # Multiple exception types
    try:
        number = int("not_a_number")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Try-except-else-finally
    try:
        num = int("123")
    except ValueError:
        print("Invalid number")
    else:
        print(f"Successfully converted: {num}")
    finally:
        print("Cleanup completed")


def demonstrate_random_numbers():
    """Demonstrate random number generation."""
    print("\n=== Random Numbers Demo ===")
    
    # Random integers
    random_int = random.randint(1, 100)
    print(f"Random integer (1-100): {random_int}")
    
    # Random choice from list
    colors = ["red", "green", "blue", "yellow", "purple"]
    random_color = random.choice(colors)
    print(f"Random color: {random_color}")
    
    # Random sample
    random_numbers = random.sample(range(1, 21), 5)
    print(f"Random sample of 5 numbers (1-20): {random_numbers}")


def demonstrate_file_simulation():
    """Simulate file operations (without actual files)."""
    print("\n=== File Operations Simulation ===")
    
    # Simulate reading a file
    simulated_content = [
        "Line 1: Hello World",
        "Line 2: Python is awesome",
        "Line 3: Learning is fun"
    ]
    
    print("Simulated file content:")
    for line_num, line in enumerate(simulated_content, 1):
        print(f"  {line_num}: {line}")
    
    # Simulate file statistics
    total_lines = len(simulated_content)
    total_chars = sum(len(line) for line in simulated_content)
    print(f"File statistics: {total_lines} lines, {total_chars} characters")


def run_all_basic_examples():
    """Run all basic examples."""
    print("🐍 PYTHON BASICS DEMONSTRATION 🐍")
    print("=" * 50)
    
    demonstrate_variables_and_types()
    demonstrate_control_flow()
    demonstrate_data_structures()
    demonstrate_functions()
    demonstrate_string_operations()
    demonstrate_list_operations()
    demonstrate_error_handling()
    demonstrate_random_numbers()
    demonstrate_file_simulation()
    
    print("\n" + "=" * 50)
    print("✅ All basic examples completed!")


if __name__ == "__main__":
    run_all_basic_examples()
