"""
String manipulation utility functions.

This module provides various string processing and manipulation functions
including cleaning, validation, formatting, and analysis operations.
"""

import re
from typing import List, Dict, Optional


def clean_text(text: str) -> str:
    """
    Remove extra whitespace from beginning, end, and between words.
    
    Args:
        text (str): Input text to clean
        
    Returns:
        str: Cleaned text with normalized whitespace
        
    Example:
        >>> clean_text("  Hello    World  ")
        "Hello World"
    """
    return ' '.join(text.split())


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): Text to check
        ignore_case (bool): Whether to ignore case differences
        ignore_spaces (bool): Whether to ignore spaces and punctuation
        
    Returns:
        bool: True if text is palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    if ignore_spaces:
        text = re.sub(r'[^a-zA-Z0-9]', '', text)
    
    if ignore_case:
        text = text.lower()
    
    return text == text[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of words
        
    Example:
        >>> count_words("Hello world from Python")
        4
    """
    return len(text.split())


def count_characters(text: str, include_spaces: bool = True) -> int:
    """
    Count characters in text.
    
    Args:
        text (str): Input text
        include_spaces (bool): Whether to count spaces
        
    Returns:
        int: Character count
    """
    if not include_spaces:
        text = text.replace(' ', '')
    return len(text)


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with each word capitalized
        
    Example:
        >>> capitalize_words("hello world from python")
        "Hello World From Python"
    """
    return ' '.join(word.capitalize() for word in text.split())


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Reversed text
        
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]


def remove_vowels(text: str) -> str:
    """
    Remove all vowels from text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text without vowels
        
    Example:
        >>> remove_vowels("hello world")
        "hll wrld"
    """
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)


def extract_numbers(text: str) -> List[int]:
    """
    Extract all numbers from a text string.
    
    Args:
        text (str): Input text
        
    Returns:
        List[int]: List of extracted numbers
        
    Example:
        >>> extract_numbers("I have 5 cats and 10 dogs")
        [5, 10]
    """
    return [int(match) for match in re.findall(r'\d+', text)]


def word_frequency(text: str) -> Dict[str, int]:
    """
    Count frequency of each word in text.
    
    Args:
        text (str): Input text
        
    Returns:
        Dict[str, int]: Dictionary with word frequencies
        
    Example:
        >>> word_frequency("hello world hello")
        {"hello": 2, "world": 1}
    """
    words = clean_text(text.lower()).split()
    return {word: words.count(word) for word in set(words)}


def longest_word(text: str) -> str:
    """
    Find the longest word in text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Longest word found
        
    Example:
        >>> longest_word("The quick brown fox jumps")
        "jumps"
    """
    words = text.split()
    return max(words, key=len) if words else ""


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to maximum length with optional suffix.
    
    Args:
        text (str): Input text
        max_length (int): Maximum allowed length
        suffix (str): Suffix to add when truncating
        
    Returns:
        str: Truncated text
        
    Example:
        >>> truncate_text("This is a long sentence", 10)
        "This is..."
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def snake_case_to_camel_case(text: str) -> str:
    """
    Convert snake_case to camelCase.
    
    Args:
        text (str): Snake case string
        
    Returns:
        str: Camel case string
        
    Example:
        >>> snake_case_to_camel_case("hello_world_test")
        "helloWorldTest"
    """
    components = text.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


def camel_case_to_snake_case(text: str) -> str:
    """
    Convert camelCase to snake_case.
    
    Args:
        text (str): Camel case string
        
    Returns:
        str: Snake case string
        
    Example:
        >>> camel_case_to_snake_case("helloWorldTest")
        "hello_world_test"
    """
    return re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')


def contains_only_digits(text: str) -> bool:
    """
    Check if string contains only digits.
    
    Args:
        text (str): Input text
        
    Returns:
        bool: True if contains only digits
        
    Example:
        >>> contains_only_digits("12345")
        True
    """
    return text.isdigit()


def contains_only_letters(text: str) -> bool:
    """
    Check if string contains only letters.
    
    Args:
        text (str): Input text
        
    Returns:
        bool: True if contains only letters
        
    Example:
        >>> contains_only_letters("HelloWorld")
        True
    """
    return text.isalpha()


def title_case(text: str) -> str:
    """
    Convert text to title case (first letter of each word capitalized).
    
    Args:
        text (str): Input text
        
    Returns:
        str: Title case text
        
    Example:
        >>> title_case("hello world from python")
        "Hello World From Python"
    """
    return text.title()


def count_lines(text: str) -> int:
    """
    Count number of lines in text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of lines
    """
    return len(text.split('\n'))


def remove_extra_spaces(text: str) -> str:
    """
    Remove extra spaces between words, keeping single spaces.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with normalized spacing
    """
    return ' '.join(text.split())


def is_email_format(email: str) -> bool:
    """
    Basic email format validation.
    
    Args:
        email (str): Email string to validate
        
    Returns:
        bool: True if basic email format is valid
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text.
    
    Args:
        text (str): Input text
        
    Returns:
        List[str]: List of found email addresses
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)
