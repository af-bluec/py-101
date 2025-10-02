#!/usr/bin/env python3
"""
Refactored Python Demo Script - Main Entry Point

This script demonstrates various Python concepts organized into modular components.
The code has been refactored from a single file into reusable modules and functions.

Author: Refactored Code Team
Version: 2.0.0
"""

import sys
import random
from typing import Dict, Any

# Import our modular components
from config import (
    WELCOME_MESSAGE, COMPLETION_MESSAGE, SEPARATOR, Colors,
    DEFAULT_FIBONACCI_LENGTH, SAMPLE_NAMES
)
from utils import (
    factorial, is_prime, fibonacci_sequence, greet, format_person_info,
    demonstrate_lists, demonstrate_sets, demonstrate_dictionaries,
    demonstrate_advanced_operations
)
from classes import Calculator
from decorators import timer, example_function, expensive_calculation
from generators import fibonacci_generator, demonstrate_generators
from examples import run_all_demonstrations


def print_header():
    """Print a colorful header for the application."""
    if sys.stdout.isatty():  # Only use colors if output is a terminal
        print(f"{Colors.BRIGHT_BLUE}{SEPARATOR}")
        print(f"{Colors.BRIGHT_GREEN}{WELCOME_MESSAGE}")
        print(f"{Colors.BRIGHT_BLUE}{SEPARATOR}{Colors.RESET}")
    else:
        print(SEPARATOR)
        print(WELCOME_MESSAGE)
        print(SEPARATOR)


def demonstrate_math_functions():
    """Demonstrate mathematical functions from utils.math_utils."""
    print(f"\n{Colors.YELLOW}📊 Mathematical Functions:{Colors.RESET}")
    
    # Factorial demonstration
    factorial_num = 5
    print(f"Factorial of {factorial_num}: {factorial(factorial_num)}")
    
    # Prime checking
    prime_candidate = 17
    print(f"Is {prime_candidate} prime? {is_prime(prime_candidate)}")
    
    # Fibonacci sequence
    fib_seq = fibonacci_sequence(DEFAULT_FIBONACCI_LENGTH)
    print(f"First {DEFAULT_FIBONACCI_LENGTH} Fibonacci numbers: {fib_seq}")


def demonstrate_string_operations():
    """Demonstrate string utilities."""
    print(f"\n{Colors.YELLOW}📝 String Operations:{Colors.RESET}")
    
    # Greeting
    name = random.choice(SAMPLE_NAMES)
    greeting = greet(name)
    print(f"Greeting: {greeting}")
    
    # Person info formatting
    age = random.randint(20, 60)
    person_info = format_person_info(name, age)
    print(f"Person info: {person_info}")


def demonstrate_data_structures():
    """Demonstrate data structure utilities."""
    print(f"\n{Colors.YELLOW}🗂️  Data Structures:{Colors.RESET}")
    
    # Lists
    lists_demo = demonstrate_lists()
    print(f"Squares (1-5): {lists_demo['squares']}")
    print(f"Sorted fruits: {lists_demo['fruits']}")
    
    # Sets
    sets_demo = demonstrate_sets()
    print(f"Set union {sets_demo['set1']} ∪ {sets_demo['set2']}: {sets_demo['union']}")
    print(f"Set intersection: {sets_demo['intersection']}")
    
    # Dictionaries  
    dict_demo = demonstrate_dictionaries()
    print(f"Average score: {dict_demo['average_score']:.1f}")


def demonstrate_object_oriented():
    """Demonstrate object-oriented programming with Calculator class."""
    print(f"\n{Colors.YELLOW}🧮 Object-Oriented Programming:{Colors.RESET}")
    
    calc = Calculator()
    
    # Basic operations
    result_add = calc.add(5, 3)
    result_subtract = calc.subtract(10, 4)
    result_multiply = calc.multiply(6, 7)
    result_divide = calc.divide(15, 3)
    
    print(f"5 + 3 = {result_add}")
    print(f"10 - 4 = {result_subtract}")
    print(f"6 × 7 = {result_multiply}")
    print(f"15 ÷ 3 = {result_divide}")
    
    # Show calculation history
    history = calc.get_history()
    print(f"Calculator history: {len(history)} operations performed")


def demonstrate_decorators():
    """Demonstrate decorator functionality."""
    print(f"\n{Colors.YELLOW}🎭 Decorators:{Colors.RESET}")
    
    # Example decorated function
    example_function("Decorator Demo")
    
    # Cached function demonstration
    print("\nCaching demonstration:")
    expensive_calculation(5)  # Cache miss
    expensive_calculation(5)  # Cache hit


def demonstrate_generators_section():
    """Demonstrate generator functionality."""
    print(f"\n{Colors.YELLOW}🔄 Generators:{Colors.RESET}")
    
    # Fibonacci generator
    print("First 8 Fibonacci numbers (using generator):")
    fib_gen = fibonacci_generator()
    fib_numbers = [next(fib_gen) for _ in range(8)]
    print(f"Fibonacci: {fib_numbers}")
    
    # Run comprehensive generator demonstrations
    print("\nRunning generator demonstrations...")
    demonstrate_generators()


def demonstrate_error_handling():
    """Demonstrate error handling patterns."""
    print(f"\n{Colors.YELLOW}⚠️  Error Handling:{Colors.RESET}")
    
    # Safe division
    try:
        result = 10 / 2
        print(f"10 ÷ 2 = {result}")
    except ZeroDivisionError:
        print("Division by zero error!")
    else:
        print("Division completed successfully")
    
    # Exception with Calculator
    calc = Calculator()
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Calculator error: {e}")


def demonstrate_advanced_features():
    """Demonstrate advanced Python features."""
    print(f"\n{Colors.YELLOW}🚀 Advanced Features:{Colors.RESET}")
    
    # List comprehensions
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares (1-5) via comprehension: {squares}")
    
    # Lambda functions
    multiply = lambda x, y: x * y
    print(f"Lambda multiplication (4 × 7): {multiply(4, 7)}")
    
    # Map and filter
    numbers = [1, 2, 3, 4, 5, 6]
    doubled = list(map(lambda x: x * 2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    
    print(f"Original numbers: {numbers}")
    print(f"Doubled: {doubled}")
    print(f"Evens only: {evens}")


@timer
def run_comprehensive_demonstrations():
    """Run all comprehensive demonstrations."""
    print(f"\n{Colors.YELLOW}🎯 Comprehensive Demonstrations:{Colors.RESET}")
    results = run_all_demonstrations()
    
    # Show a sample of results
    print(f"Control flow example - age category: {results['control_flow']['age_category']}")
    print(f"Functional programming - product: {results['functional_programming']['product']}")
    print(f"Today's date: {results['date_operations']['today']}")


def print_footer():
    """Print completion message."""
    print(f"\n{Colors.BRIGHT_BLUE}{SEPARATOR}")
    print(f"{Colors.BRIGHT_GREEN}{COMPLETION_MESSAGE}")
    print(f"{Colors.BRIGHT_BLUE}{SEPARATOR}{Colors.RESET}")


def main():
    """
    Main execution function that orchestrates all demonstrations.
    """
    # Print header
    print_header()
    
    try:
        # Run all demonstration sections
        demonstrate_math_functions()
        demonstrate_string_operations()
        demonstrate_data_structures()
        demonstrate_object_oriented()
        demonstrate_decorators()
        demonstrate_generators_section()
        demonstrate_error_handling()
        demonstrate_advanced_features()
        run_comprehensive_demonstrations()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Program interrupted by user.{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {e}{Colors.RESET}")
        sys.exit(1)
    
    # Print completion message
    print_footer()


if __name__ == "__main__":
    main()
