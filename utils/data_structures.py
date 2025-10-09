"""
Data structure helper functions.

This module provides utilities for working with common Python data structures
including lists, dictionaries, sets, and tuples with advanced operations.
"""

from typing import List, Dict, Any, Set, Tuple, Union, Optional, Callable
from collections import defaultdict, Counter
import itertools


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list into a single-level list.
    
    Args:
        nested_list (List[Any]): Nested list structure
        
    Returns:
        List[Any]: Flattened list
        
    Example:
        >>> flatten_list([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    Remove duplicates from list while preserving order.
    
    Args:
        lst (List[Any]): Input list
        
    Returns:
        List[Any]: List without duplicates
        
    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any], merge_strategy: str = "overwrite") -> Dict[Any, Any]:
    """
    Merge two dictionaries with different strategies for handling conflicts.
    
    Args:
        dict1 (Dict): First dictionary
        dict2 (Dict): Second dictionary
        merge_strategy (str): How to handle key conflicts ("overwrite", "keep_first", "combine")
        
    Returns:
        Dict: Merged dictionary
        
    Example:
        >>> merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
        {"a": 1, "b": 3, "c": 4}
    """
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result:
            if merge_strategy == "overwrite":
                result[key] = value
            elif merge_strategy == "keep_first":
                pass  # Keep original value
            elif merge_strategy == "combine":
                if isinstance(result[key], list) and isinstance(value, list):
                    result[key].extend(value)
                elif isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
                    result[key] += value
                else:
                    result[key] = [result[key], value]
        else:
            result[key] = value
    
    return result


def group_by_key(lst: List[Dict[str, Any]], key: str) -> Dict[Any, List[Dict[str, Any]]]:
    """
    Group list of dictionaries by a specific key.
    
    Args:
        lst (List[Dict]): List of dictionaries
        key (str): Key to group by
        
    Returns:
        Dict: Grouped items
        
    Example:
        >>> group_by_key([{"type": "fruit", "name": "apple"}, {"type": "fruit", "name": "banana"}], "type")
        {"fruit": [{"type": "fruit", "name": "apple"}, {"type": "fruit", "name": "banana"}]}
    """
    grouped = defaultdict(list)
    for item in lst:
        if key in item:
            grouped[item[key]].append(item)
    return dict(grouped)


def sort_dict_by_value(d: Dict[Any, Any], reverse: bool = False) -> Dict[Any, Any]:
    """
    Sort dictionary by values.
    
    Args:
        d (Dict): Input dictionary
        reverse (bool): Sort in descending order if True
        
    Returns:
        Dict: Sorted dictionary
        
    Example:
        >>> sort_dict_by_value({"a": 3, "b": 1, "c": 2})
        {"b": 1, "c": 2, "a": 3}
    """
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Invert dictionary keys and values.
    
    Args:
        d (Dict): Input dictionary
        
    Returns:
        Dict: Inverted dictionary
        
    Example:
        >>> invert_dict({"a": 1, "b": 2})
        {1: "a", 2: "b"}
    """
    return {v: k for k, v in d.items()}


def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split list into chunks of specified size.
    
    Args:
        lst (List): Input list
        chunk_size (int): Size of each chunk
        
    Returns:
        List[List]: List of chunks
        
    Example:
        >>> chunk_list([1, 2, 3, 4, 5, 6], 2)
        [[1, 2], [3, 4], [5, 6]]
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def transpose_matrix(matrix: List[List[Any]]) -> List[List[Any]]:
    """
    Transpose a 2D matrix (swap rows and columns).
    
    Args:
        matrix (List[List]): Input matrix
        
    Returns:
        List[List]: Transposed matrix
        
    Example:
        >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not matrix or not matrix[0]:
        return []
    return list(map(list, zip(*matrix)))


def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Find common elements between two lists.
    
    Args:
        list1 (List): First list
        list2 (List): Second list
        
    Returns:
        List: Common elements
        
    Example:
        >>> find_common_elements([1, 2, 3], [2, 3, 4])
        [2, 3]
    """
    return list(set(list1) & set(list2))


def find_unique_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Find elements that are unique to each list (symmetric difference).
    
    Args:
        list1 (List): First list
        list2 (List): Second list
        
    Returns:
        List: Unique elements
        
    Example:
        >>> find_unique_elements([1, 2, 3], [2, 3, 4])
        [1, 4]
    """
    return list(set(list1) ^ set(list2))


def rotate_list(lst: List[Any], positions: int) -> List[Any]:
    """
    Rotate list by specified positions.
    
    Args:
        lst (List): Input list
        positions (int): Number of positions to rotate (positive = right, negative = left)
        
    Returns:
        List: Rotated list
        
    Example:
        >>> rotate_list([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
    """
    if not lst:
        return lst
    positions = positions % len(lst)
    return lst[-positions:] + lst[:-positions]


def get_nested_value(data: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    """
    Get value from nested dictionary using list of keys.
    
    Args:
        data (Dict): Nested dictionary
        keys (List[str]): List of keys representing path
        default: Default value if key path not found
        
    Returns:
        Any: Value at key path or default
        
    Example:
        >>> get_nested_value({"a": {"b": {"c": 42}}}, ["a", "b", "c"])
        42
    """
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def set_nested_value(data: Dict[str, Any], keys: List[str], value: Any) -> Dict[str, Any]:
    """
    Set value in nested dictionary using list of keys.
    
    Args:
        data (Dict): Nested dictionary (modified in place)
        keys (List[str]): List of keys representing path
        value (Any): Value to set
        
    Returns:
        Dict: Modified dictionary
        
    Example:
        >>> set_nested_value({}, ["a", "b", "c"], 42)
        {"a": {"b": {"c": 42}}}
    """
    current = data
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value
    return data


def count_elements(lst: List[Any]) -> Dict[Any, int]:
    """
    Count occurrences of each element in list.
    
    Args:
        lst (List): Input list
        
    Returns:
        Dict: Element counts
        
    Example:
        >>> count_elements([1, 2, 2, 3, 1, 1])
        {1: 3, 2: 2, 3: 1}
    """
    return dict(Counter(lst))


def most_frequent_element(lst: List[Any]) -> Any:
    """
    Find most frequent element in list.
    
    Args:
        lst (List): Input list
        
    Returns:
        Any: Most frequent element
        
    Example:
        >>> most_frequent_element([1, 2, 2, 3, 1, 1])
        1
    """
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]


def filter_dict(d: Dict[Any, Any], predicate: Callable[[Any, Any], bool]) -> Dict[Any, Any]:
    """
    Filter dictionary based on predicate function.
    
    Args:
        d (Dict): Input dictionary
        predicate (Callable): Function that takes key, value and returns bool
        
    Returns:
        Dict: Filtered dictionary
        
    Example:
        >>> filter_dict({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1)
        {"b": 2, "c": 3}
    """
    return {k: v for k, v in d.items() if predicate(k, v)}


def cartesian_product(list1: List[Any], list2: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Generate cartesian product of two lists.
    
    Args:
        list1 (List): First list
        list2 (List): Second list
        
    Returns:
        List[Tuple]: Cartesian product pairs
        
    Example:
        >>> cartesian_product([1, 2], ["a", "b"])
        [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
    """
    return list(itertools.product(list1, list2))


def partition_list(lst: List[Any], predicate: Callable[[Any], bool]) -> Tuple[List[Any], List[Any]]:
    """
    Partition list into two lists based on predicate.
    
    Args:
        lst (List): Input list
        predicate (Callable): Function that returns bool
        
    Returns:
        Tuple[List, List]: (elements matching predicate, elements not matching)
        
    Example:
        >>> partition_list([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        ([2, 4], [1, 3, 5])
    """
    true_list, false_list = [], []
    for item in lst:
        (true_list if predicate(item) else false_list).append(item)
    return true_list, false_list


def sliding_window(lst: List[Any], window_size: int) -> List[List[Any]]:
    """
    Create sliding windows of specified size over list.
    
    Args:
        lst (List): Input list
        window_size (int): Size of each window
        
    Returns:
        List[List]: List of sliding windows
        
    Example:
        >>> sliding_window([1, 2, 3, 4, 5], 3)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    if window_size > len(lst):
        return []
    return [lst[i:i + window_size] for i in range(len(lst) - window_size + 1)]


def deep_copy_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Create a deep copy of a dictionary (simple implementation).
    
    Args:
        d (Dict): Input dictionary
        
    Returns:
        Dict: Deep copy of dictionary
    """
    import copy
    return copy.deepcopy(d)


def merge_sorted_lists(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1 (List): First sorted list
        list2 (List): Second sorted list
        
    Returns:
        List: Merged sorted list
        
    Example:
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result
