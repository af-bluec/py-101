#!/usr/bin/env python3
"""
Main entry point for the py101 package.

This script demonstrates the functionality provided by the py101 package
and serves as an example of how to use the various modules.
"""

import argparse
import logging
import sys
from typing import Optional

from py101 import (
    Calculator, 
    PythonFeatureDemo, 
    factorial, 
    fibonacci_sequence, 
    generate_random_number,
    greet,
    is_prime,
    string_operations
)
from py101.utils import (
    apply_lambda_operations,
    list_operations,
    set_operations,
    tuple_operations
)


def setup_logging(level: str = "INFO") -> None:
    """
    Set up logging configuration.
    
    Args:
        level (str): Logging level
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('py101.log')
        ]
    )


def main_demo() -> None:
    """Run the main demonstration of py101 functionality."""
    logger = logging.getLogger(__name__)
    logger.info("Starting py101 demonstration...")
    
    # Math operations demo
    logger.info("=== Math Operations Demo ===")
    try:
        logger.info(f"Factorial of 5: {factorial(5)}")
        logger.info(f"Is 17 prime? {is_prime(17)}")
        logger.info(f"Is 15 prime? {is_prime(15)}")
        
        fib_seq = fibonacci_sequence(10)
        logger.info(f"First 10 Fibonacci numbers: {fib_seq}")
    except Exception as e:
        logger.error(f"Error in math operations: {e}")
    
    # Calculator demo
    logger.info("=== Calculator Demo ===")
    calc = Calculator()
    try:
        logger.info(f"5 + 3 = {calc.add(5, 3)}")
        logger.info(f"5 - 3 = {calc.subtract(5, 3)}")
        logger.info(f"5 * 3 = {calc.multiply(5, 3)}")
        logger.info(f"10 / 2 = {calc.divide(10, 2)}")
        logger.info(f"2 ^ 3 = {calc.power(2, 3)}")
    except Exception as e:
        logger.error(f"Error in calculator operations: {e}")
    
    # Utilities demo
    logger.info("=== Utilities Demo ===")
    logger.info(greet("Python Developer"))
    logger.info(f"Random number: {generate_random_number(1, 100)}")
    
    text_ops = string_operations("Python is Amazing!")
    logger.info(f"String operations: {text_ops}")
    
    # List operations demo
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_ops = list_operations(numbers)
    logger.info(f"List operations on {numbers}: {list_ops}")
    
    # Lambda operations demo
    lambda_ops = apply_lambda_operations(numbers[:5])
    logger.info(f"Lambda operations: {lambda_ops}")
    
    # Set operations demo
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set_ops = set_operations(set1, set2)
    logger.info(f"Set operations on {set1} and {set2}: {set_ops}")
    
    # Tuple operations demo
    point = (10, 20)
    tuple_ops = tuple_operations(point)
    logger.info(f"Tuple operations on {point}: {tuple_ops}")
    
    # Python features demo
    logger.info("=== Python Features Demo ===")
    demo = PythonFeatureDemo()
    demo.run_all_demos()
    
    logger.info("py101 demonstration completed successfully!")


def interactive_mode() -> None:
    """Run interactive mode for testing individual functions."""
    logger = logging.getLogger(__name__)
    calc = Calculator()
    
    logger.info("Welcome to py101 interactive mode!")
    logger.info("Available commands: factorial, prime, fibonacci, calc, quit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == "quit":
                break
            elif command == "factorial":
                n = int(input("Enter number: "))
                result = factorial(n)
                print(f"Factorial of {n} is {result}")
            elif command == "prime":
                n = int(input("Enter number: "))
                result = is_prime(n)
                print(f"{n} is {'prime' if result else 'not prime'}")
            elif command == "fibonacci":
                n = int(input("Enter length: "))
                result = fibonacci_sequence(n)
                print(f"Fibonacci sequence: {result}")
            elif command == "calc":
                a = float(input("Enter first number: "))
                op = input("Enter operation (+, -, *, /, **): ")
                b = float(input("Enter second number: "))
                
                if op == "+":
                    result = calc.add(a, b)
                elif op == "-":
                    result = calc.subtract(a, b)
                elif op == "*":
                    result = calc.multiply(a, b)
                elif op == "/":
                    result = calc.divide(a, b)
                elif op == "**":
                    result = calc.power(a, b)
                else:
                    print("Invalid operation")
                    continue
                
                print(f"Result: {result}")
            else:
                print("Unknown command")
                
        except (ValueError, TypeError) as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    logger.info("Goodbye!")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="py101 - Python educational package demonstration"
    )
    
    parser.add_argument(
        "--mode", 
        choices=["demo", "interactive"],
        default="demo",
        help="Run mode: demo (default) or interactive"
    )
    
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging level (default: INFO)"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="py101 1.0.0"
    )
    
    return parser.parse_args()


def main() -> None:
    """Main entry point for the application."""
    args = parse_arguments()
    setup_logging(args.log_level)
    
    logger = logging.getLogger(__name__)
    
    try:
        if args.mode == "demo":
            main_demo()
        elif args.mode == "interactive":
            interactive_mode()
    except KeyboardInterrupt:
        logger.info("Program interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
