"""
String manipulation utilities.
"""
from typing import List, Dict


def greet(name: str) -> str:
    """
    Generate a greeting message for a given name.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def format_person_info(name: str, age: int) -> str:
    """
    Format person information into a readable string.
    
    Args:
        name: Person's name
        age: Person's age
        
    Returns:
        Formatted string with person information
    """
    return f"{name} is {age} years old."


def analyze_text(text: str) -> Dict[str, any]:
    """
    Analyze text and return various properties.
    
    Args:
        text: The text to analyze
        
    Returns:
        Dictionary containing text analysis results
    """
    return {
        'original': text,
        'uppercase': text.upper(),
        'lowercase': text.lower(),
        'length': len(text),
        'word_count': len(text.split()),
        'char_frequency': _get_char_frequency(text)
    }


def _get_char_frequency(text: str) -> Dict[str, int]:
    """
    Get character frequency in text (helper function).
    
    Args:
        text: Text to analyze
        
    Returns:
        Dictionary with character frequencies
    """
    frequency = {}
    for char in text.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


def reverse_words(text: str) -> str:
    """
    Reverse the order of words in a string.
    
    Args:
        text: Input text
        
    Returns:
        Text with words in reverse order
    """
    return ' '.join(text.split()[::-1])


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word.
    
    Args:
        text: Input text
        
    Returns:
        Text with each word capitalized
    """
    return text.title()


def remove_duplicates(text: str) -> str:
    """
    Remove duplicate characters while preserving order.
    
    Args:
        text: Input text
        
    Returns:
        Text with duplicate characters removed
    """
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
