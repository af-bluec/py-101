"""
Control flow utilities module.

This module contains examples of various control flow constructs
and utility functions for loops, conditionals, and exception handling.
"""

import random
from datetime import date


def demonstrate_loops():
    """
    Demonstrate various loop constructs.
    
    Returns:
        dict: Results from different loop examples
    """
    results = {}
    
    # For loop example
    counting = []
    for i in range(1, 11):
        counting.append(f"Counting: {i}")
    results["for_loop"] = counting
    
    # While loop example
    while_results = []
    count = 0
    while count < 5:
        while_results.append(f"While loop iteration: {count}")
        count += 1
    results["while_loop"] = while_results
    
    return results


def demonstrate_conditionals(age=25):
    """
    Demonstrate conditional statements.
    
    Args:
        age (int): Age to check
        
    Returns:
        dict: Results of conditional checks
    """
    results = {}
    
    # Basic if-else
    if age >= 18:
        results["age_category"] = "Adult"
    else:
        results["age_category"] = "Minor"
    
    # Multiple conditions
    if age < 13:
        results["detailed_category"] = "Child"
    elif age < 20:
        results["detailed_category"] = "Teenager"
    elif age < 65:
        results["detailed_category"] = "Adult"
    else:
        results["detailed_category"] = "Senior"
    
    return results


def demonstrate_exception_handling():
    """
    Demonstrate various exception handling patterns.
    
    Returns:
        dict: Results of exception handling examples
    """
    results = {}
    
    # Basic try-except
    try:
        result = 10 / 0
        results["division_result"] = result
    except ZeroDivisionError:
        results["division_error"] = "Cannot divide by zero!"
    
    # Try-except with else
    try:
        num = int("123")
        results["conversion_error"] = None
    except ValueError:
        results["conversion_error"] = "Invalid number"
    else:
        results["converted_number"] = num
    
    # Try-except-finally
    try:
        # Simulate file operation
        data = "sample data"
        results["file_data"] = data
    except Exception as e:
        results["file_error"] = str(e)
    finally:
        results["cleanup_status"] = "Cleanup completed"
    
    return results


def generate_random_examples():
    """
    Generate various random examples.
    
    Returns:
        dict: Random number examples
    """
    return {
        "random_int": random.randint(1, 100),
        "random_float": random.random(),
        "random_choice": random.choice(["apple", "banana", "cherry"]),
        "random_sample": random.sample(range(1, 11), 3)
    }


def demonstrate_date_operations():
    """
    Demonstrate date operations.
    
    Returns:
        dict: Date operation results
    """
    today = date.today()
    return {
        "today": today,
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "weekday": today.weekday(),
        "formatted": today.strftime("%Y-%m-%d")
    }
