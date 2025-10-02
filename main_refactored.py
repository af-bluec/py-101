"""
Main application module.

This is the refactored main application that demonstrates various Python concepts
using modular, reusable code organized in separate modules.
"""

import sys
import os

# Add utils directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Import all our custom modules
from math_operations import factorial, is_prime, fibonacci_sequence, countdown, divide
from data_structures import (
    demonstrate_lists, demonstrate_dictionaries, 
    demonstrate_sets, demonstrate_tuples, generator_example
)
from string_operations import greet, demonstrate_string_operations, format_person_info, work_with_bytes
from file_operations import simulate_file_read, handle_file_operations, demonstrate_context_manager
from calculator import Calculator, multiply_lambda
from decorators import say_hello, slow_function, add_numbers
from constants import (
    PI, DEFAULT_FIBONACCI_LENGTH, SAMPLE_TEXT, 
    DEFAULT_GREETING_NAME, SCRIPT_COMPLETION_MESSAGE
)
from control_flow import (
    demonstrate_loops, demonstrate_conditionals, 
    demonstrate_exception_handling, generate_random_examples, demonstrate_date_operations
)


def main():
    """
    Main function that demonstrates all the refactored functionality.
    """
    print("=" * 60)
    print("Welcome to the Refactored Python Demo Application!")
    print("=" * 60)
    
    # Mathematical operations
    print("\n🔢 Mathematical Operations:")
    print("-" * 30)
    try:
        print(f"Factorial of 5: {factorial(5)}")
        print(f"Is 17 prime? {is_prime(17)}")
        fib_seq = fibonacci_sequence(DEFAULT_FIBONACCI_LENGTH)
        print(f"First {DEFAULT_FIBONACCI_LENGTH} Fibonacci numbers: {fib_seq}")
    except Exception as e:
        print(f"Error in mathematical operations: {e}")
    
    # String operations
    print("\n📝 String Operations:")
    print("-" * 30)
    greet(DEFAULT_GREETING_NAME)
    string_results = demonstrate_string_operations(SAMPLE_TEXT)
    for key, value in string_results.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print(f"Person info: {format_person_info('Bob', 28)}")
    
    # Data structures
    print("\n📊 Data Structures:")
    print("-" * 30)
    
    list_results = demonstrate_lists()
    print(f"Squares of 1-5: {list_results['squares']}")
    print(f"Fruits (sorted): {list_results['fruits']}")
    print(f"Doubled numbers: {list_results['doubled']}")
    print(f"Even numbers: {list_results['evens']}")
    print(f"Product: {list_results['product']}")
    
    dict_results = demonstrate_dictionaries()
    print(f"Person info: {dict_results['person']}")
    print(f"Average score: {dict_results['average_score']:.1f}")
    
    set_results = demonstrate_sets()
    print(f"Set union: {set_results['union']}")
    print(f"Set intersection: {set_results['intersection']}")
    
    tuple_results = demonstrate_tuples()
    print(f"Point coordinates: ({tuple_results['x_coordinate']}, {tuple_results['y_coordinate']})")
    
    # Calculator operations
    print("\n🧮 Calculator Operations:")
    print("-" * 30)
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"5 - 3 = {calc.subtract(5, 3)}")
    print(f"5 * 3 = {calc.multiply(5, 3)}")
    print(f"5 / 3 = {calc.divide(5, 3):.2f}")
    print(f"Lambda multiply 4 * 7 = {multiply_lambda(4, 7)}")
    
    # Control flow demonstrations
    print("\n🔄 Control Flow:")
    print("-" * 30)
    
    loop_results = demonstrate_loops()
    print(f"For loop iterations: {len(loop_results['for_loop'])}")
    print(f"While loop iterations: {len(loop_results['while_loop'])}")
    
    conditional_results = demonstrate_conditionals(25)
    print(f"Age 25 category: {conditional_results['age_category']}")
    print(f"Detailed category: {conditional_results['detailed_category']}")
    
    # Exception handling
    print("\n⚠️ Exception Handling:")
    print("-" * 30)
    exception_results = demonstrate_exception_handling()
    if "division_error" in exception_results:
        print(exception_results["division_error"])
    if "converted_number" in exception_results:
        print(f"Converted number: {exception_results['converted_number']}")
    print(exception_results.get("cleanup_status", "No cleanup info"))
    
    # File operations (simulated)
    print("\n📁 File Operations (Simulated):")
    print("-" * 30)
    print(simulate_file_read("example.txt"))
    file_results = handle_file_operations()
    if "error" in file_results:
        print(file_results["error"])
    print(file_results.get("cleanup", "No cleanup info"))
    
    # Context manager demonstration
    print("\n🔧 Context Manager:")
    print("-" * 30)
    demonstrate_context_manager()
    
    # Decorators
    print("\n🎭 Decorators:")
    print("-" * 30)
    say_hello()
    slow_function()
    add_numbers(10, 20)
    
    # Random examples
    print("\n🎲 Random Examples:")
    print("-" * 30)
    random_results = generate_random_examples()
    for key, value in random_results.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Date operations
    print("\n📅 Date Operations:")
    print("-" * 30)
    date_results = demonstrate_date_operations()
    print(f"Today's date: {date_results['formatted']}")
    print(f"Year: {date_results['year']}, Month: {date_results['month']}, Day: {date_results['day']}")
    
    # Constants demonstration
    print("\n📏 Constants:")
    print("-" * 30)
    print(f"Value of PI: {PI}")
    
    # Recursion example
    print("\n🔄 Recursion Example:")
    print("-" * 30)
    countdown(3)
    
    # Error handling with math operations
    print("\n🛡️ Error Handling:")
    print("-" * 30)
    try:
        result = divide(10, 2)
        print(f"10 ÷ 2 = {result}")
        result = divide(10, 0)  # This will raise an error
    except ValueError as e:
        print(f"Math error: {e}")
    
    # Bytes operations
    print("\n🔤 Bytes Operations:")
    print("-" * 30)
    byte_results = work_with_bytes("Hello World")
    print(f"Original: {byte_results['original']}")
    print(f"As bytes: {byte_results['as_bytes']}")
    print(f"Decoded: {byte_results['decoded']}")
    
    # Generator example
    print("\n⚡ Generator Example:")
    print("-" * 30)
    gen_values = generator_example()
    print(f"Generator values: {gen_values}")
    
    print("\n" + "=" * 60)
    print(SCRIPT_COMPLETION_MESSAGE)
    print("=" * 60)


if __name__ == "__main__":
    main()
