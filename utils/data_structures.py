"""
Data structures operations module.

This module contains examples and operations for various Python data structures
including lists, dictionaries, sets, and tuples.
"""

from functools import reduce


def demonstrate_lists():
    """
    Demonstrate various list operations.
    
    Returns:
        dict: Results of list operations
    """
    # List comprehension example
    squares = [x**2 for x in range(1, 6)]
    
    # List methods
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    fruits.sort()
    
    numbers = [1, 2, 3, 4]
    doubled = list(map(lambda x: x * 2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    product = reduce(lambda x, y: x * y, numbers)
    
    return {
        "squares": squares,
        "fruits": fruits,
        "doubled": doubled,
        "evens": evens,
        "product": product
    }


def demonstrate_dictionaries():
    """
    Demonstrate dictionary operations.
    
    Returns:
        dict: Results of dictionary operations
    """
    person = {"name": "Alice", "age": 30}
    scores = {"math": 95, "science": 88}
    average_score = sum(scores.values()) / len(scores)
    
    return {
        "person": person,
        "scores": scores,
        "average_score": average_score
    }


def demonstrate_sets():
    """
    Demonstrate set operations.
    
    Returns:
        dict: Results of set operations
    """
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    return {
        "set1": set1,
        "set2": set2,
        "union": set1 | set2,
        "intersection": set1 & set2,
        "difference": set1 - set2
    }


def demonstrate_tuples():
    """
    Demonstrate tuple operations.
    
    Returns:
        dict: Results of tuple operations
    """
    point = (10, 20)
    x, y = point  # Tuple unpacking
    
    return {
        "original_point": point,
        "x_coordinate": x,
        "y_coordinate": y
    }


def generator_example():
    """
    Demonstrate generator expressions.
    
    Returns:
        list: Values from generator
    """
    gen = (x for x in range(3))
    return list(gen)
