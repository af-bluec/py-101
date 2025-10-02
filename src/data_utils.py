"""
Data manipulation and utility functions.

This module provides functions for working with strings, lists, dictionaries,
and other data structures commonly used in Python applications.
"""

from typing import List, Dict, Any, Tuple, Union
from functools import reduce


def process_text(text: str) -> Dict[str, Union[str, int]]:
    """
    Process text and return various manipulations.
    
    Args:
        text (str): Input text to process
        
    Returns:
        Dict containing various text manipulations
    """
    return {
        'original': text,
        'uppercase': text.upper(),
        'lowercase': text.lower(),
        'title_case': text.title(),
        'length': len(text),
        'word_count': len(text.split()),
        'reversed': text[::-1],
        'stripped': text.strip()
    }


def filter_and_sort_numbers(numbers: List[Union[int, float]], 
                          filter_even: bool = True, 
                          reverse: bool = False) -> List[Union[int, float]]:
    """
    Filter and sort a list of numbers.
    
    Args:
        numbers: List of numbers to process
        filter_even: If True, return only even numbers; if False, return odd numbers
        reverse: If True, sort in descending order
        
    Returns:
        Filtered and sorted list of numbers
    """
    if filter_even:
        filtered = [num for num in numbers if num % 2 == 0]
    else:
        filtered = [num for num in numbers if num % 2 != 0]
    
    return sorted(filtered, reverse=reverse)


def create_squares_dict(limit: int) -> Dict[int, int]:
    """
    Create a dictionary mapping numbers to their squares.
    
    Args:
        limit: Upper limit (exclusive) for numbers
        
    Returns:
        Dictionary mapping numbers to their squares
    """
    return {x: x**2 for x in range(1, limit + 1)}


def merge_dictionaries(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple dictionaries into one.
    
    Args:
        *dicts: Variable number of dictionaries to merge
        
    Returns:
        Merged dictionary (later dictionaries override earlier ones)
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def analyze_list(data: List[Union[int, float]]) -> Dict[str, Union[int, float]]:
    """
    Analyze a list of numbers and return statistics.
    
    Args:
        data: List of numbers to analyze
        
    Returns:
        Dictionary containing statistical information
        
    Raises:
        ValueError: If the list is empty
    """
    if not data:
        raise ValueError("Cannot analyze empty list")
    
    return {
        'count': len(data),
        'sum': sum(data),
        'min': min(data),
        'max': max(data),
        'average': sum(data) / len(data),
        'range': max(data) - min(data)
    }


def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    """
    Group words by their length.
    
    Args:
        words: List of words to group
        
    Returns:
        Dictionary mapping lengths to lists of words
    """
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result


def flatten_nested_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flatten a list of lists into a single list.
    
    Args:
        nested_list: List containing sublists
        
    Returns:
        Flattened list
    """
    return [item for sublist in nested_list for item in sublist]


def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Find common elements between two lists.
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        List of common elements (no duplicates)
    """
    return list(set(list1) & set(list2))


def create_person_info(name: str, age: int, **kwargs) -> Dict[str, Any]:
    """
    Create a person information dictionary.
    
    Args:
        name: Person's name
        age: Person's age
        **kwargs: Additional person attributes
        
    Returns:
        Dictionary containing person information
    """
    info = {'name': name, 'age': age}
    info.update(kwargs)
    return info


def calculate_product(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the product of all numbers in a list.
    
    Args:
        numbers: List of numbers to multiply
        
    Returns:
        Product of all numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate product of empty list")
    
    return reduce(lambda x, y: x * y, numbers)


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        data: List to chunk
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
        
    Raises:
        ValueError: If chunk_size is less than 1
    """
    if chunk_size < 1:
        raise ValueError("Chunk size must be at least 1")
    
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def set_operations(set1: set, set2: set) -> Dict[str, set]:
    """
    Perform various set operations on two sets.
    
    Args:
        set1: First set
        set2: Second set
        
    Returns:
        Dictionary containing results of different set operations
    """
    return {
        'union': set1 | set2,
        'intersection': set1 & set2,
        'difference': set1 - set2,
        'symmetric_difference': set1 ^ set2,
        'is_subset': set1.issubset(set2),
        'is_superset': set1.issuperset(set2)
    }
