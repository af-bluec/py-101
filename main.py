#!/usr/bin/env python3
"""
Python 101 - Comprehensive Python Learning and Demonstration Toolkit

This is the main entry point for the refactored py-101 project.
It demonstrates various Python concepts through modular, well-organized code.

The original monolithic script has been refactored into:
- Mathematical utilities (src/math_utils.py)
- Calculator classes (src/calculator.py)
- Data manipulation utilities (src/data_utils.py)
- Decorators and patterns (src/decorators.py)
- Advanced Python features (src/advanced_features.py)
- Example scripts (examples/)
- Configuration (config.py)

Author: Refactored Code Base
Version: 2.0.0
"""

import sys
import random
from datetime import date
from functools import reduce

# Import our custom modules
from src.math_utils import factorial, is_prime, fibonacci_sequence, get_prime_numbers
from src.calculator import Calculator, ScientificCalculator
from src.data_utils import (
    process_text, analyze_list, create_squares_dict, 
    set_operations, chunk_list
)
from src.decorators import timer, logger
from src.advanced_features import countdown_generator, create_lambda_functions
from config import (
    APP_NAME, VERSION, DESCRIPTION, SAMPLE_DATA, 
    format_colored_text, is_feature_enabled
)

# Import example modules for demonstration
from examples.basic_examples import run_all_basic_examples
from examples.advanced_examples import run_all_advanced_examples
from examples.error_handling_examples import run_all_error_examples


def print_header():
    """Print application header with styling."""
    header = f"""
╔══════════════════════════════════════════════════════════════╗
║                        {APP_NAME:<30}                   ║
║                        Version {VERSION:<25}                ║
║                                                              ║
║  {DESCRIPTION:<58}  ║
╚══════════════════════════════════════════════════════════════╝
"""
    
    if is_feature_enabled('enable_colors'):
        print(format_colored_text(header, 'cyan'))
    else:
        print(header)


@timer
def demonstrate_mathematical_operations():
    """Demonstrate mathematical functions from math_utils module."""
    print(format_colored_text("\n🔢 MATHEMATICAL OPERATIONS", 'blue'))
    print("=" * 50)
    
    # Factorial demonstrations
    print("Factorial calculations:")
    for n in [5, 7, 10]:
        result = factorial(n)
        print(f"  {n}! = {result:,}")
    
    # Prime number demonstrations
    print("\nPrime number checks:")
    test_numbers = [17, 25, 29, 100, 101]
    for num in test_numbers:
        is_prime_result = is_prime(num)
        status = "✓ Prime" if is_prime_result else "✗ Not Prime"
        print(f"  {num}: {status}")
    
    # Prime numbers in range
    primes = get_prime_numbers(50)
    print(f"\nPrime numbers up to 50: {primes}")
    
    # Fibonacci sequence
    fib_seq = fibonacci_sequence(12)
    print(f"\nFirst 12 Fibonacci numbers: {fib_seq}")


@timer
def demonstrate_calculator_usage():
    """Demonstrate calculator classes."""
    print(format_colored_text("\n🧮 CALCULATOR DEMONSTRATIONS", 'green'))
    print("=" * 50)
    
    # Basic calculator
    print("Basic Calculator:")
    calc = Calculator()
    
    operations = [
        (calc.add, 15, 7),
        (calc.subtract, 20, 8),
        (calc.multiply, 6, 9),
        (calc.divide, 56, 8),
        (calc.power, 3, 4),
        (calc.square_root, 64),
        (calc.percentage, 200, 15)
    ]
    
    for op_data in operations:
        try:
            if len(op_data) == 3:
                func, a, b = op_data
                result = func(a, b)
            else:
                func, a = op_data
                result = func(a)
            print(f"  Result: {result}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print("\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry}")
    
    # Scientific calculator
    print("\nScientific Calculator:")
    sci_calc = ScientificCalculator()
    import math
    
    angle = math.pi / 4  # 45 degrees in radians
    print(f"  sin(π/4) = {sci_calc.sin(angle):.4f}")
    print(f"  cos(π/4) = {sci_calc.cos(angle):.4f}")
    print(f"  log₁₀(100) = {sci_calc.log(100):.2f}")


@timer
def demonstrate_data_manipulation():
    """Demonstrate data utilities."""
    print(format_colored_text("\n📊 DATA MANIPULATION", 'yellow'))
    print("=" * 50)
    
    # Text processing
    sample_text = "Python Programming is Powerful and Versatile!"
    text_analysis = process_text(sample_text)
    
    print("Text Analysis:")
    for key, value in text_analysis.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    # List analysis
    numbers = SAMPLE_DATA['numbers'] + [23, 45, 12, 67, 34]
    stats = analyze_list(numbers)
    
    print(f"\nList Analysis for {numbers}:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key.title()}: {value:.2f}")
        else:
            print(f"  {key.title()}: {value}")
    
    # Dictionary creation
    squares = create_squares_dict(8)
    print(f"\nSquares dictionary (1-8): {squares}")
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set_results = set_operations(set1, set2)
    
    print(f"\nSet Operations:")
    print(f"  Set 1: {set1}")
    print(f"  Set 2: {set2}")
    for operation, result in set_results.items():
        if isinstance(result, bool):
            print(f"  {operation.replace('_', ' ').title()}: {result}")
        else:
            print(f"  {operation.replace('_', ' ').title()}: {result}")


def demonstrate_advanced_features():
    """Demonstrate advanced Python features."""
    print(format_colored_text("\n🚀 ADVANCED FEATURES", 'purple'))
    print("=" * 50)
    
    # Generator demonstration
    print("Generator - Countdown from 5:")
    for num in countdown_generator(5):
        print(f"  {num}")
    
    # Lambda functions
    lambda_funcs = create_lambda_functions()
    test_data = [1, 2, 3, 4, 5]
    
    print(f"\nLambda Functions with {test_data}:")
    squared = list(map(lambda_funcs['square'], test_data))
    print(f"  Squared: {squared}")
    
    evens = list(filter(lambda_funcs['is_even'], test_data))
    print(f"  Even numbers: {evens}")
    
    # List comprehensions
    print("\nList Comprehensions:")
    squares_comp = [x**2 for x in range(1, 6)]
    print(f"  Squares (1-5): {squares_comp}")
    
    # Dictionary comprehension
    word_lengths = {word: len(word) for word in SAMPLE_DATA['fruits']}
    print(f"  Fruit name lengths: {word_lengths}")


def demonstrate_error_handling():
    """Demonstrate error handling patterns."""
    print(format_colored_text("\n⚠️  ERROR HANDLING", 'red'))
    print("=" * 50)
    
    # Division by zero handling
    print("Safe division function:")
    
    def safe_divide(a, b):
        try:
            result = a / b
            return f"{a} / {b} = {result}"
        except ZeroDivisionError:
            return f"{a} / {b} = Error: Cannot divide by zero"
    
    test_divisions = [(10, 2), (15, 0), (20, 4)]
    for a, b in test_divisions:
        print(f"  {safe_divide(a, b)}")
    
    # Type error handling
    print("\nType validation:")
    
    def safe_factorial(n):
        try:
            if not isinstance(n, int):
                raise TypeError("Input must be an integer")
            if n < 0:
                raise ValueError("Input must be non-negative")
            return factorial(n)
        except (TypeError, ValueError) as e:
            return f"Error: {e}"
    
    test_values = [5, -3, "hello", 3.14]
    for value in test_values:
        result = safe_factorial(value)
        print(f"  factorial({value}) = {result}")


def demonstrate_data_structures_and_iteration():
    """Demonstrate various data structures and iteration patterns."""
    print(format_colored_text("\n🔄 DATA STRUCTURES & ITERATION", 'cyan'))
    print("=" * 50)
    
    # Working with different data structures
    fruits = SAMPLE_DATA['fruits'].copy()
    print(f"Original fruits: {fruits}")
    
    # List operations
    fruits.append("fig")
    fruits.sort()
    print(f"After adding and sorting: {fruits}")
    
    # Dictionary operations
    person_data = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"\nPerson data: {person_data}")
    
    # Adding new information
    person_data.update({"occupation": "Engineer", "salary": 75000})
    print(f"Updated person: {person_data}")
    
    # Tuple operations
    coordinates = [(0, 0), (1, 2), (3, 4), (5, 6)]
    print(f"\nCoordinates: {coordinates}")
    
    # Unpacking tuples
    print("Unpacked coordinates:")
    for x, y in coordinates:
        print(f"  Point: ({x}, {y}) - Distance from origin: {(x**2 + y**2)**0.5:.2f}")


def demonstrate_functional_programming():
    """Demonstrate functional programming concepts."""
    print(format_colored_text("\n🔧 FUNCTIONAL PROGRAMMING", 'green'))
    print("=" * 50)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Map, Filter, Reduce
    print(f"Original numbers: {numbers}")
    
    # Map - square all numbers
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared: {squared}")
    
    # Filter - get even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Reduce - calculate product
    product = reduce(lambda x, y: x * y, numbers[:4])  # First 4 numbers
    print(f"Product of first 4 numbers: {product}")
    
    # Chunk list demonstration
    chunked = chunk_list(numbers, 3)
    print(f"Numbers in chunks of 3: {chunked}")


def demonstrate_random_and_date_operations():
    """Demonstrate random number generation and date operations."""
    print(format_colored_text("\n🎲 RANDOM & DATE OPERATIONS", 'blue'))
    print("=" * 50)
    
    # Random number generation
    print("Random number demonstrations:")
    print(f"  Random integer (1-100): {random.randint(1, 100)}")
    print(f"  Random float (0-1): {random.random():.4f}")
    
    # Random choice from list
    random_fruit = random.choice(SAMPLE_DATA['fruits'])
    print(f"  Random fruit: {random_fruit}")
    
    # Random sample
    random_numbers = random.sample(range(1, 21), 5)
    print(f"  Random sample (5 from 1-20): {random_numbers}")
    
    # Date operations
    today = date.today()
    print(f"\nToday's date: {today}")
    print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")


def run_interactive_menu():
    """Run an interactive menu for different demonstrations."""
    menu_options = {
        '1': ('Basic Examples', run_all_basic_examples),
        '2': ('Advanced Examples', run_all_advanced_examples),
        '3': ('Error Handling Examples', run_all_error_examples),
        '4': ('Mathematical Operations', demonstrate_mathematical_operations),
        '5': ('Calculator Usage', demonstrate_calculator_usage),
        '6': ('Data Manipulation', demonstrate_data_manipulation),
        '7': ('Advanced Features', demonstrate_advanced_features),
        '8': ('Error Handling', demonstrate_error_handling),
        '9': ('Data Structures', demonstrate_data_structures_and_iteration),
        '10': ('Functional Programming', demonstrate_functional_programming),
        '11': ('Random & Dates', demonstrate_random_and_date_operations),
        '0': ('Run All Demonstrations', None)
    }
    
    while True:
        print(format_colored_text("\n📋 MENU - Choose a demonstration:", 'bold'))
        print("-" * 40)
        
        for key, (description, _) in menu_options.items():
            print(f"  {key}: {description}")
        
        print("  q: Quit")
        
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice == 'q':
            print(format_colored_text("👋 Goodbye! Thanks for exploring Python!", 'green'))
            break
        elif choice == '0':
            run_all_demonstrations()
        elif choice in menu_options and choice != '0':
            _, func = menu_options[choice]
            if func:
                func()
        else:
            print(format_colored_text("❌ Invalid choice. Please try again.", 'red'))


def run_all_demonstrations():
    """Run all demonstrations in sequence."""
    print_header()
    
    demonstrate_mathematical_operations()
    demonstrate_calculator_usage()
    demonstrate_data_manipulation()
    demonstrate_advanced_features()
    demonstrate_error_handling()
    demonstrate_data_structures_and_iteration()
    demonstrate_functional_programming()
    demonstrate_random_and_date_operations()
    
    print(format_colored_text("\n🎉 ALL DEMONSTRATIONS COMPLETED!", 'green'))
    print("=" * 50)


def main():
    """Main entry point of the application."""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command in ['help', '-h', '--help']:
            print(f"""
{APP_NAME} v{VERSION}

Usage: python main.py [command]

Commands:
  help        Show this help message
  basic       Run basic examples
  advanced    Run advanced examples
  errors      Run error handling examples
  all         Run all demonstrations
  interactive Run interactive menu (default)

Examples:
  python main.py basic
  python main.py all
  python main.py
            """)
        elif command == 'basic':
            print_header()
            run_all_basic_examples()
        elif command == 'advanced':
            print_header()
            run_all_advanced_examples()
        elif command == 'errors':
            print_header()
            run_all_error_examples()
        elif command == 'all':
            run_all_demonstrations()
        else:
            print(f"Unknown command: {command}")
            print("Use 'python main.py help' for usage information")
    else:
        # Default: run interactive menu
        print_header()
        run_interactive_menu()


if __name__ == "__main__":
    main()
