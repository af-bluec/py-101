"""
String operations module.

This module contains various string manipulation functions and examples.
"""


def greet(name):
    """
    Print a greeting message.
    
    Args:
        name (str): The name to greet
    """
    print(f"Hello, {name}!")


def demonstrate_string_operations(text="Python is fun!"):
    """
    Demonstrate various string operations.
    
    Args:
        text (str): The text to manipulate
        
    Returns:
        dict: Results of string operations
    """
    return {
        "original": text,
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "length": len(text),
        "reversed": text[::-1],
        "words": text.split(),
        "replace_fun_with_awesome": text.replace("fun", "awesome")
    }


def format_person_info(name, age):
    """
    Format person information using f-strings.
    
    Args:
        name (str): Person's name
        age (int): Person's age
        
    Returns:
        str: Formatted string with person info
    """
    return f"{name} is {age} years old."


def work_with_bytes(text="Hello"):
    """
    Demonstrate working with bytes.
    
    Args:
        text (str): Text to convert to bytes
        
    Returns:
        dict: Byte operations results
    """
    byte_data = text.encode('utf-8')
    decoded_data = byte_data.decode('utf-8')
    
    return {
        "original": text,
        "as_bytes": byte_data,
        "decoded": decoded_data
    }
