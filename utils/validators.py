"""
Input validation utility functions.

This module provides various validation functions for common data types,
formats, and business logic validation.
"""

import re
from typing import Any, List, Union, Optional
from datetime import datetime


def is_valid_email(email: str) -> bool:
    """
    Validate email address format.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email format is valid
        
    Example:
        >>> is_valid_email("user@example.com")
        True
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_phone(phone: str, country_code: Optional[str] = None) -> bool:
    """
    Validate phone number format.
    
    Args:
        phone (str): Phone number to validate
        country_code (str, optional): Country code for specific validation
        
    Returns:
        bool: True if phone format is valid
        
    Example:
        >>> is_valid_phone("+1-555-123-4567")
        True
    """
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
    
    # Basic international format validation
    if cleaned.startswith('+'):
        # International format: +[country code][number]
        return re.match(r'^\+\d{7,15}$', cleaned) is not None
    else:
        # Domestic format validation (US style)
        return re.match(r'^\d{10}$', cleaned) is not None


def is_valid_url(url: str) -> bool:
    """
    Validate URL format.
    
    Args:
        url (str): URL to validate
        
    Returns:
        bool: True if URL format is valid
        
    Example:
        >>> is_valid_url("https://www.example.com")
        True
    """
    pattern = r'^https?://(?:[-\w.])+(?:\.[a-zA-Z]{2,})+(?:/[^?\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?$'
    return re.match(pattern, url) is not None


def is_valid_ip_address(ip: str, version: int = 4) -> bool:
    """
    Validate IP address format.
    
    Args:
        ip (str): IP address to validate
        version (int): IP version (4 or 6)
        
    Returns:
        bool: True if IP format is valid
        
    Example:
        >>> is_valid_ip_address("192.168.1.1")
        True
    """
    if version == 4:
        pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return re.match(pattern, ip) is not None
    elif version == 6:
        pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return re.match(pattern, ip) is not None
    else:
        return False


def is_valid_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Validate date string format.
    
    Args:
        date_string (str): Date string to validate
        date_format (str): Expected date format
        
    Returns:
        bool: True if date format is valid
        
    Example:
        >>> is_valid_date("2023-12-25")
        True
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def is_valid_credit_card(card_number: str) -> bool:
    """
    Validate credit card number using Luhn algorithm.
    
    Args:
        card_number (str): Credit card number
        
    Returns:
        bool: True if card number is valid
        
    Example:
        >>> is_valid_credit_card("4532015112830366")
        True
    """
    # Remove spaces and hyphens
    card_number = re.sub(r'[\s\-]', '', card_number)
    
    # Check if all characters are digits
    if not card_number.isdigit():
        return False
    
    # Check length (most cards are 13-19 digits)
    if not (13 <= len(card_number) <= 19):
        return False
    
    # Luhn algorithm
    def luhn_checksum(card_num):
        def digits_of(n):
            return [int(d) for d in str(n)]
        
        digits = digits_of(card_num)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10
    
    return luhn_checksum(card_number) == 0


def is_strong_password(password: str, min_length: int = 8, 
                      require_uppercase: bool = True,
                      require_lowercase: bool = True,
                      require_digits: bool = True,
                      require_special: bool = True) -> bool:
    """
    Validate password strength.
    
    Args:
        password (str): Password to validate
        min_length (int): Minimum password length
        require_uppercase (bool): Require uppercase letters
        require_lowercase (bool): Require lowercase letters
        require_digits (bool): Require digits
        require_special (bool): Require special characters
        
    Returns:
        bool: True if password meets requirements
        
    Example:
        >>> is_strong_password("MyP@ssw0rd")
        True
    """
    if len(password) < min_length:
        return False
    
    if require_uppercase and not re.search(r'[A-Z]', password):
        return False
    
    if require_lowercase and not re.search(r'[a-z]', password):
        return False
    
    if require_digits and not re.search(r'\d', password):
        return False
    
    if require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True


def is_numeric(value: str, allow_negative: bool = True, allow_decimal: bool = True) -> bool:
    """
    Check if string represents a valid number.
    
    Args:
        value (str): String to check
        allow_negative (bool): Allow negative numbers
        allow_decimal (bool): Allow decimal numbers
        
    Returns:
        bool: True if string is numeric
        
    Example:
        >>> is_numeric("-123.45")
        True
    """
    if not value:
        return False
    
    pattern = r'^'
    if allow_negative:
        pattern += r'-?'
    pattern += r'\d+'
    if allow_decimal:
        pattern += r'(?:\.\d+)?'
    pattern += r'$'
    
    return re.match(pattern, value) is not None


def is_integer(value: str, allow_negative: bool = True) -> bool:
    """
    Check if string represents a valid integer.
    
    Args:
        value (str): String to check
        allow_negative (bool): Allow negative integers
        
    Returns:
        bool: True if string is integer
        
    Example:
        >>> is_integer("-123")
        True
    """
    return is_numeric(value, allow_negative=allow_negative, allow_decimal=False)


def is_in_range(value: Union[int, float], min_val: Union[int, float], 
                max_val: Union[int, float], inclusive: bool = True) -> bool:
    """
    Check if value is within specified range.
    
    Args:
        value: Value to check
        min_val: Minimum value
        max_val: Maximum value
        inclusive (bool): Whether range is inclusive
        
    Returns:
        bool: True if value is in range
        
    Example:
        >>> is_in_range(5, 1, 10)
        True
    """
    if inclusive:
        return min_val <= value <= max_val
    else:
        return min_val < value < max_val


def is_valid_length(text: str, min_length: int = 0, max_length: Optional[int] = None) -> bool:
    """
    Validate string length.
    
    Args:
        text (str): Text to validate
        min_length (int): Minimum length
        max_length (int, optional): Maximum length
        
    Returns:
        bool: True if length is valid
        
    Example:
        >>> is_valid_length("Hello", min_length=3, max_length=10)
        True
    """
    length = len(text)
    if length < min_length:
        return False
    if max_length is not None and length > max_length:
        return False
    return True


def contains_only_alphanumeric(text: str, allow_spaces: bool = False) -> bool:
    """
    Check if text contains only alphanumeric characters.
    
    Args:
        text (str): Text to check
        allow_spaces (bool): Allow space characters
        
    Returns:
        bool: True if text is alphanumeric
        
    Example:
        >>> contains_only_alphanumeric("Hello123")
        True
    """
    if allow_spaces:
        pattern = r'^[a-zA-Z0-9\s]+$'
    else:
        pattern = r'^[a-zA-Z0-9]+$'
    
    return re.match(pattern, text) is not None


def is_valid_username(username: str, min_length: int = 3, max_length: int = 20,
                     allow_underscore: bool = True, allow_dash: bool = True) -> bool:
    """
    Validate username format.
    
    Args:
        username (str): Username to validate
        min_length (int): Minimum length
        max_length (int): Maximum length
        allow_underscore (bool): Allow underscore character
        allow_dash (bool): Allow dash character
        
    Returns:
        bool: True if username is valid
        
    Example:
        >>> is_valid_username("user_123")
        True
    """
    if not is_valid_length(username, min_length, max_length):
        return False
    
    # Must start with letter
    if not username[0].isalpha():
        return False
    
    # Build allowed character pattern
    pattern = r'^[a-zA-Z0-9'
    if allow_underscore:
        pattern += '_'
    if allow_dash:
        pattern += '-'
    pattern += ']+$'
    
    return re.match(pattern, username) is not None


def is_empty_or_whitespace(text: str) -> bool:
    """
    Check if string is empty or contains only whitespace.
    
    Args:
        text (str): Text to check
        
    Returns:
        bool: True if empty or whitespace only
        
    Example:
        >>> is_empty_or_whitespace("   ")
        True
    """
    return not text or text.isspace()


def validate_list_items(items: List[Any], validator_func, allow_empty: bool = False) -> bool:
    """
    Validate all items in a list using validator function.
    
    Args:
        items (List): List of items to validate
        validator_func: Function to validate each item
        allow_empty (bool): Allow empty list
        
    Returns:
        bool: True if all items are valid
        
    Example:
        >>> validate_list_items([1, 2, 3], lambda x: x > 0)
        True
    """
    if not items and not allow_empty:
        return False
    
    return all(validator_func(item) for item in items)


def is_valid_json_string(json_string: str) -> bool:
    """
    Check if string is valid JSON.
    
    Args:
        json_string (str): JSON string to validate
        
    Returns:
        bool: True if valid JSON
        
    Example:
        >>> is_valid_json_string('{"key": "value"}')
        True
    """
    import json
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def is_valid_hex_color(color: str) -> bool:
    """
    Validate hexadecimal color code.
    
    Args:
        color (str): Color code to validate
        
    Returns:
        bool: True if valid hex color
        
    Example:
        >>> is_valid_hex_color("#FF5733")
        True
    """
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    return re.match(pattern, color) is not None


def is_valid_postal_code(postal_code: str, country: str = "US") -> bool:
    """
    Validate postal code format for specific countries.
    
    Args:
        postal_code (str): Postal code to validate
        country (str): Country code (US, CA, UK, etc.)
        
    Returns:
        bool: True if postal code format is valid
        
    Example:
        >>> is_valid_postal_code("12345", "US")
        True
    """
    patterns = {
        "US": r'^\d{5}(-\d{4})?$',  # 12345 or 12345-6789
        "CA": r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$',  # A1A 1A1
        "UK": r'^[A-Z]{1,2}\d[A-Z\d]? \d[A-Z]{2}$',  # SW1A 1AA
        "DE": r'^\d{5}$',  # 12345
        "FR": r'^\d{5}$',  # 12345
    }
    
    pattern = patterns.get(country.upper())
    if not pattern:
        return False
    
    return re.match(pattern, postal_code) is not None
