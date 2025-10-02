#!/usr/bin/env python3
"""
Advanced usage example for py101 package.

This script demonstrates advanced features and error handling
patterns using the py101 package.
"""

import logging
from py101 import Calculator, PythonFeatureDemo
from py101.utils import list_operations, apply_lambda_operations, set_operations

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def demonstrate_error_handling():
    """Demonstrate proper error handling."""
    print("=== Error Handling Examples ===")
    
    calc = Calculator()
    
    # Handle division by zero
    try:
        result = calc.divide(10, 0)
        print(f"10 / 0 = {result}")
    except ValueError as e:
        print(f"Caught error: {e}")
    
    # Handle invalid factorial input
    try:
        from py101 import factorial
        result = factorial(-5)
        print(f"Factorial of -5: {result}")
    except ValueError as e:
        print(f"Caught error: {e}")
    
    print()


def demonstrate_data_processing():
    """Demonstrate data processing capabilities."""
    print("=== Data Processing Examples ===")
    
    # Process a list of numbers
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original data: {data}")
    
    # Statistical operations
    stats = list_operations(data)
    print(f"Sum: {stats['sum']}, Average: {stats['average']:.2f}")
    print(f"Min: {stats['min']}, Max: {stats['max']}")
    print(f"Even numbers: {stats['evens']}")
    print(f"Odd numbers: {stats['odds']}")
    
    # Lambda operations
    lambda_results = apply_lambda_operations(data[:5])
    print(f"Doubled first 5: {lambda_results['doubled']}")
    print(f"Product of first 5: {lambda_results['product']}")
    
    # Set operations
    set1 = set(data[:6])  # {1, 2, 3, 4, 5, 6}
    set2 = set(data[4:])  # {5, 6, 7, 8, 9, 10}
    set_ops = set_operations(set1, set2)
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set_ops['union']}")
    print(f"Intersection: {set_ops['intersection']}")
    
    print()


def demonstrate_interactive_features():
    """Demonstrate interactive features."""
    print("=== Interactive Features Demo ===")
    
    # Create demo instance
    demo = PythonFeatureDemo()
    
    # Run specific demonstrations
    print("Running loop demonstrations...")
    demo.demonstrate_loops()
    
    print("\nRunning conditional demonstrations...")
    category = demo.demonstrate_conditionals(16)
    print(f"Age category result: {category}")
    
    print("\nRunning data structure demonstrations...")
    structures = demo.demonstrate_data_structures()
    print("Data structures created:")
    for key, value in structures.items():
        print(f"  {key}: {value}")
    
    print()


def performance_example():
    """Demonstrate performance considerations."""
    print("=== Performance Example ===")
    
    import time
    from py101 import fibonacci_sequence
    
    # Measure execution time
    start_time = time.time()
    
    # Generate larger Fibonacci sequence
    fib_result = fibonacci_sequence(30)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Generated {len(fib_result)} Fibonacci numbers")
    print(f"Execution time: {execution_time:.4f} seconds")
    print(f"Last 5 numbers: {fib_result[-5:]}")
    
    print()


def main():
    """Main function to run all advanced examples."""
    print("=== py101 Advanced Usage Examples ===\n")
    
    try:
        demonstrate_error_handling()
        demonstrate_data_processing()
        demonstrate_interactive_features()
        performance_example()
        
        print("=== All advanced examples completed successfully! ===")
        
    except Exception as e:
        logger.error(f"An error occurred during execution: {e}")
        raise


if __name__ == "__main__":
    main()
