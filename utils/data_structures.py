"""
Data structure utilities and demonstrations.
"""
from typing import List, Dict, Set, Tuple, Any
from functools import reduce


def demonstrate_lists() -> Dict[str, Any]:
    """
    Demonstrate list operations and methods.
    
    Returns:
        Dictionary with list operation results
    """
    # List comprehension example
    squares = [x**2 for x in range(1, 6)]
    
    # List methods demonstration
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    fruits.sort()
    
    return {
        'squares': squares,
        'fruits': fruits,
        'doubled_numbers': list(map(lambda x: x * 2, [1, 2, 3, 4])),
        'even_numbers': list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    }


def demonstrate_sets() -> Dict[str, Set[int]]:
    """
    Demonstrate set operations.
    
    Returns:
        Dictionary with set operation results
    """
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    return {
        'set1': set1,
        'set2': set2,
        'union': set1 | set2,
        'intersection': set1 & set2,
        'difference': set1 - set2,
        'symmetric_difference': set1 ^ set2
    }


def demonstrate_dictionaries() -> Dict[str, Any]:
    """
    Demonstrate dictionary operations.
    
    Returns:
        Dictionary with dictionary operation results
    """
    person = {"name": "Alice", "age": 30, "city": "New York"}
    scores = {"math": 95, "science": 88, "english": 92}
    
    return {
        'person': person,
        'scores': scores,
        'average_score': sum(scores.values()) / len(scores),
        'keys': list(person.keys()),
        'values': list(person.values()),
        'items': list(person.items())
    }


def demonstrate_tuples() -> Dict[str, Any]:
    """
    Demonstrate tuple operations and unpacking.
    
    Returns:
        Dictionary with tuple operation results
    """
    point = (10, 20)
    x, y = point
    
    coordinates = [(1, 2), (3, 4), (5, 6)]
    
    return {
        'point': point,
        'x_coordinate': x,
        'y_coordinate': y,
        'coordinates': coordinates,
        'distances': [((x1**2 + y1**2)**0.5) for x1, y1 in coordinates]
    }


def demonstrate_advanced_operations(numbers: List[int]) -> Dict[str, Any]:
    """
    Demonstrate advanced data structure operations.
    
    Args:
        numbers: List of numbers to operate on
        
    Returns:
        Dictionary with advanced operation results
    """
    # Reduce operation
    try:
        product = reduce(lambda x, y: x * y, numbers) if numbers else 0
    except TypeError:
        product = None
    
    # Enumerate
    enumerated = list(enumerate(numbers))
    
    # Zip operation
    letters = ['a', 'b', 'c', 'd'][:len(numbers)]
    zipped = list(zip(numbers, letters))
    
    return {
        'original_numbers': numbers,
        'product': product,
        'sum': sum(numbers),
        'max': max(numbers) if numbers else None,
        'min': min(numbers) if numbers else None,
        'enumerated': enumerated,
        'zipped_with_letters': zipped
    }


def create_nested_structure() -> Dict[str, Any]:
    """
    Create and demonstrate nested data structures.
    
    Returns:
        Complex nested data structure
    """
    return {
        'students': [
            {
                'name': 'John',
                'grades': {'math': 85, 'science': 92},
                'hobbies': ['reading', 'swimming']
            },
            {
                'name': 'Jane',
                'grades': {'math': 95, 'science': 88},
                'hobbies': ['painting', 'hiking']
            }
        ],
        'metadata': {
            'school': 'Tech High',
            'year': 2024,
            'subjects': ['math', 'science']
        }
    }
