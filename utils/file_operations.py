"""
File operations module.

This module contains file handling examples and utilities.
Note: These are simulation functions for demonstration purposes.
"""

import os
from contextlib import contextmanager


def simulate_file_read(filename="sample.txt"):
    """
    Simulate reading from a file.
    
    Args:
        filename (str): Name of the file to simulate reading
        
    Returns:
        str: Simulated file content
    """
    return f"Simulating file read from {filename}: This is sample content."


def simulate_file_write(filename, content):
    """
    Simulate writing to a file.
    
    Args:
        filename (str): Name of the file to simulate writing
        content (str): Content to simulate writing
        
    Returns:
        str: Success message
    """
    return f"Simulated writing to {filename}: '{content}'"


def handle_file_operations():
    """
    Demonstrate file operation error handling.
    
    Returns:
        dict: Results of file operations
    """
    results = {}
    
    # Simulate file not found
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
            results["file_content"] = content
    except FileNotFoundError:
        results["error"] = "File not found"
    finally:
        results["cleanup"] = "Cleanup done"
    
    return results


@contextmanager
def simulate_context_manager(resource_name="Resource"):
    """
    Simulate a context manager for resource management.
    
    Args:
        resource_name (str): Name of the resource to manage
    """
    print(f"{resource_name} acquired")
    try:
        yield resource_name
    finally:
        print(f"{resource_name} released")


def demonstrate_context_manager():
    """
    Demonstrate context manager usage.
    """
    with simulate_context_manager("Database Connection") as resource:
        print(f"Using {resource}")
        return f"Successfully used {resource}"
