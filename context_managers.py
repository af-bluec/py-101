"""
Python Context Managers Demonstration

This module showcases context managers in Python:
- Using built-in context managers
- Creating custom context managers with __enter__/__exit__
- Using contextlib decorators
- Nested context managers
- Exception handling in context managers

Context managers provide a way to allocate and release resources precisely
when you want to. The most common use is the 'with' statement.
"""

import contextlib
import sqlite3
import tempfile
import os
import time
from typing import Any, Iterator, Optional


class FileManager:
    """
    A custom context manager for file operations with automatic cleanup.
    
    This demonstrates the context manager protocol using __enter__ and __exit__.
    """
    
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context - close the file."""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        # Return False to propagate any exceptions
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        return False


class DatabaseTransaction:
    """
    A context manager for database transactions with rollback on error.
    """
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
    
    def __enter__(self):
        """Enter the context - start transaction."""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        print("Database transaction started")
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context - commit or rollback."""
        if exc_type is None:
            # No exception - commit the transaction
            self.conn.commit()
            print("Transaction committed successfully")
        else:
            # Exception occurred - rollback
            self.conn.rollback()
            print(f"Transaction rolled back due to: {exc_type.__name__}")
        
        self.conn.close()
        print("Database connection closed")
        
        # Don't suppress the exception
        return False


@contextlib.contextmanager
def timer_context(operation_name: str) -> Iterator[dict]:
    """
    A context manager created using contextlib.contextmanager decorator.
    
    Args:
        operation_name: Name of the operation being timed
        
    Yields:
        A dictionary to store timing information
    """
    timing_info = {'start_time': None, 'end_time': None, 'duration': None}
    
    print(f"Starting operation: {operation_name}")
    timing_info['start_time'] = time.time()
    
    try:
        yield timing_info
    finally:
        timing_info['end_time'] = time.time()
        timing_info['duration'] = timing_info['end_time'] - timing_info['start_time']
        print(f"Operation '{operation_name}' completed in {timing_info['duration']:.4f} seconds")


@contextlib.contextmanager
def temporary_directory() -> Iterator[str]:
    """
    A context manager that creates and cleans up a temporary directory.
    
    Yields:
        Path to the temporary directory
    """
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    
    try:
        yield temp_dir
    finally:
        # Clean up the temporary directory
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Cleaned up temporary directory: {temp_dir}")


class ResourcePool:
    """
    A context manager for managing a pool of resources.
    """
    
    def __init__(self, resource_name: str, max_resources: int = 3):
        self.resource_name = resource_name
        self.max_resources = max_resources
        self.available_resources = list(range(1, max_resources + 1))
        self.used_resources = set()
    
    @contextlib.contextmanager
    def acquire_resource(self) -> Iterator[int]:
        """
        Acquire a resource from the pool.
        
        Yields:
            Resource ID
        """
        if not self.available_resources:
            raise RuntimeError(f"No {self.resource_name} resources available")
        
        resource_id = self.available_resources.pop()
        self.used_resources.add(resource_id)
        print(f"Acquired {self.resource_name} resource #{resource_id}")
        
        try:
            yield resource_id
        finally:
            self.used_resources.remove(resource_id)
            self.available_resources.append(resource_id)
            print(f"Released {self.resource_name} resource #{resource_id}")


@contextlib.contextmanager
def suppress_exceptions(*exception_types):
    """
    A context manager that suppresses specified exception types.
    
    Args:
        exception_types: Exception types to suppress
    """
    try:
        yield
    except exception_types as e:
        print(f"Suppressed exception: {type(e).__name__}: {e}")


def demonstrate_nested_context_managers():
    """Demonstrate using multiple context managers together."""
    print("\n=== Nested Context Managers Demo ===")
    
    # Create a temporary file for demonstration
    with temporary_directory() as temp_dir:
        file_path = os.path.join(temp_dir, "test.txt")
        
        # Nested context managers
        with timer_context("File operations"):
            with FileManager(file_path, 'w') as f:
                f.write("Hello, World!\n")
                f.write("This is a test file.\n")
            
            # Read the file back
            with FileManager(file_path, 'r') as f:
                content = f.read()
                print(f"File content:\n{content}")


def demonstrate_database_transaction():
    """Demonstrate database transaction context manager."""
    print("\n=== Database Transaction Demo ===")
    
    with temporary_directory() as temp_dir:
        db_path = os.path.join(temp_dir, "test.db")
        
        # Successful transaction
        print("\n1. Successful transaction:")
        with DatabaseTransaction(db_path) as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE
                )
            """)
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                         ("Alice", "alice@example.com"))
        
        # Transaction with error (will be rolled back)
        print("\n2. Transaction with error (rollback):")
        try:
            with DatabaseTransaction(db_path) as cursor:
                cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                             ("Bob", "bob@example.com"))
                # This will cause a constraint violation
                cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                             ("Charlie", "alice@example.com"))  # Duplicate email
        except sqlite3.IntegrityError:
            print("Caught integrity error - transaction was rolled back")


def demonstrate_resource_pool():
    """Demonstrate resource pool context manager."""
    print("\n=== Resource Pool Demo ===")
    
    pool = ResourcePool("Database Connection", max_resources=2)
    
    # Acquire and use resources
    with pool.acquire_resource() as resource1:
        print(f"Using resource {resource1}")
        
        with pool.acquire_resource() as resource2:
            print(f"Using resource {resource2}")
            
            # Try to acquire a third resource (should fail)
            try:
                with pool.acquire_resource() as resource3:
                    print(f"Using resource {resource3}")
            except RuntimeError as e:
                print(f"Expected error: {e}")


def demonstrate_exception_suppression():
    """Demonstrate exception suppression context manager."""
    print("\n=== Exception Suppression Demo ===")
    
    # Suppress specific exceptions
    with suppress_exceptions(ValueError, TypeError):
        print("About to raise a ValueError...")
        raise ValueError("This error will be suppressed")
    
    print("Code continues after suppressed exception")
    
    # Exception that won't be suppressed
    try:
        with suppress_exceptions(ValueError):
            print("About to raise a RuntimeError...")
            raise RuntimeError("This error will NOT be suppressed")
    except RuntimeError as e:
        print(f"Caught unsuppressed exception: {e}")


if __name__ == "__main__":
    print("=== Python Context Managers Demo ===")
    
    # Basic context manager demo
    print("\n1. Basic Custom Context Manager:")
    with temporary_directory() as temp_dir:
        test_file = os.path.join(temp_dir, "example.txt")
        
        with FileManager(test_file, 'w') as f:
            f.write("Hello from custom context manager!")
        
        with FileManager(test_file, 'r') as f:
            content = f.read()
            print(f"Read content: {content}")
    
    # Timer context manager
    print("\n2. Timer Context Manager:")
    with timer_context("Calculating sum") as timing:
        result = sum(i ** 2 for i in range(1000))
        print(f"Sum result: {result}")
    print(f"Operation took: {timing['duration']:.6f} seconds")
    
    # Run other demonstrations
    demonstrate_nested_context_managers()
    demonstrate_database_transaction()
    demonstrate_resource_pool()
    demonstrate_exception_suppression()
    
    print("\n=== Context Managers Demo Complete ===")
