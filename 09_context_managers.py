"""
Demonstration of context managers in Python.
Covers with statements, custom context managers, and contextlib utilities.
"""

import time
from contextlib import contextmanager, suppress, redirect_stdout, ExitStack
import io


# Basic context manager class
class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        
        return False  # Don't suppress exceptions


# Timer context manager
class Timer:
    """Context manager to measure execution time."""
    
    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        print(f"Starting: {self.name}")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f"Finished: {self.name} in {elapsed:.4f}s")
        return False


# Database connection simulator
class DatabaseConnection:
    """Simulate database connection with context manager."""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from database: {self.db_name}")
        self.connected = False
        return False
    
    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected to database")
        return f"Results for: {sql}"


# Using @contextmanager decorator
@contextmanager
def temporary_value(obj, attr, value):
    """Temporarily change an object's attribute."""
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield obj
    finally:
        setattr(obj, attr, original)


@contextmanager
def timer_decorator(name):
    """Timer using contextmanager decorator."""
    print(f"Starting: {name}")
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"Finished: {name} in {elapsed:.4f}s")


@contextmanager
def error_handler(error_type, message):
    """Handle specific errors with custom message."""
    try:
        yield
    except error_type as e:
        print(f"{message}: {e}")


# Multiple context managers
def demonstrate_multiple_contexts():
    """Show using multiple context managers."""
    print("=== MULTIPLE CONTEXT MANAGERS ===")
    
    # Create test files
    with open("file1.txt", "w") as f:
        f.write("Content 1")
    with open("file2.txt", "w") as f:
        f.write("Content 2")
    
    # Use multiple context managers
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        print(f"File 1: {f1.read()}")
        print(f"File 2: {f2.read()}")
    
    # Cleanup
    import os
    os.remove("file1.txt")
    os.remove("file2.txt")


# Nested context managers
def demonstrate_nested_contexts():
    """Show nested context managers."""
    print("\n=== NESTED CONTEXT MANAGERS ===")
    
    with Timer("Outer operation"):
        time.sleep(0.1)
        with Timer("Inner operation"):
            time.sleep(0.2)
        time.sleep(0.1)


# contextlib.suppress
def demonstrate_suppress():
    """Show contextlib.suppress for ignoring exceptions."""
    print("\n=== SUPPRESS EXCEPTIONS ===")
    
    # Without suppress
    try:
        int("not a number")
    except ValueError:
        print("Caught ValueError (traditional way)")
    
    # With suppress
    with suppress(ValueError):
        int("not a number")
        print("This won't print")
    print("Continued after suppressed exception")
    
    # Suppress multiple exceptions
    with suppress(FileNotFoundError, PermissionError):
        with open("nonexistent.txt", "r") as f:
            f.read()
    print("File error suppressed")


# contextlib.redirect_stdout
def demonstrate_redirect_stdout():
    """Show redirecting stdout."""
    print("\n=== REDIRECT STDOUT ===")
    
    # Capture stdout
    output = io.StringIO()
    with redirect_stdout(output):
        print("This goes to StringIO")
        print("So does this")
    
    captured = output.getvalue()
    print(f"Captured output: {repr(captured)}")


# ExitStack for dynamic context managers
def demonstrate_exit_stack():
    """Show ExitStack for managing multiple contexts dynamically."""
    print("\n=== EXIT STACK ===")
    
    # Create test files
    filenames = ["stack1.txt", "stack2.txt", "stack3.txt"]
    for fname in filenames:
        with open(fname, "w") as f:
            f.write(f"Content of {fname}")
    
    # Open multiple files dynamically
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname, "r")) for fname in filenames]
        for f in files:
            print(f"Reading {f.name}: {f.read()}")
    
    print("All files closed automatically")
    
    # Cleanup
    import os
    for fname in filenames:
        os.remove(fname)


# Resource pool context manager
class ResourcePool:
    """Context manager for resource pooling."""
    
    def __init__(self, size):
        self.size = size
        self.resources = [f"Resource-{i}" for i in range(size)]
        self.in_use = []
    
    def __enter__(self):
        if not self.resources:
            raise RuntimeError("No resources available")
        resource = self.resources.pop()
        self.in_use.append(resource)
        print(f"Acquired: {resource}")
        return resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        resource = self.in_use.pop()
        self.resources.append(resource)
        print(f"Released: {resource}")
        return False


# Lock context manager simulation
class SimpleLock:
    """Simple lock implementation."""
    
    def __init__(self):
        self.locked = False
    
    def __enter__(self):
        if self.locked:
            raise RuntimeError("Lock already acquired")
        self.locked = True
        print("Lock acquired")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.locked = False
        print("Lock released")
        return False


def practical_examples():
    """Practical examples of context managers."""
    print("\n=== PRACTICAL EXAMPLES ===")
    
    # File operations
    print("\n1. File Manager:")
    with FileManager("test.txt", "w") as f:
        f.write("Hello, World!")
    
    with FileManager("test.txt", "r") as f:
        content = f.read()
        print(f"Content: {content}")
    
    import os
    os.remove("test.txt")
    
    # Timing operations
    print("\n2. Timer:")
    with Timer("Sleep operation"):
        time.sleep(0.2)
    
    # Database connection
    print("\n3. Database Connection:")
    with DatabaseConnection("mydb") as db:
        result = db.query("SELECT * FROM users")
        print(result)
    
    # Temporary value change
    print("\n4. Temporary Value:")
    class Config:
        debug = False
    
    config = Config()
    print(f"Debug mode: {config.debug}")
    
    with temporary_value(config, "debug", True):
        print(f"Debug mode (temporary): {config.debug}")
    
    print(f"Debug mode (restored): {config.debug}")
    
    # Error handling
    print("\n5. Error Handler:")
    with error_handler(ZeroDivisionError, "Division error"):
        result = 10 / 0
    
    # Resource pool
    print("\n6. Resource Pool:")
    pool = ResourcePool(2)
    with pool as resource1:
        print(f"Using {resource1}")
        with pool as resource2:
            print(f"Using {resource2}")
    
    # Lock
    print("\n7. Lock:")
    lock = SimpleLock()
    with lock:
        print("Critical section")


def main():
    print("=== CONTEXT MANAGERS IN PYTHON ===\n")
    
    practical_examples()
    demonstrate_multiple_contexts()
    demonstrate_nested_contexts()
    demonstrate_suppress()
    demonstrate_redirect_stdout()
    demonstrate_exit_stack()
    
    print("\n=== BENEFITS OF CONTEXT MANAGERS ===")
    print("1. Automatic resource cleanup")
    print("2. Exception-safe resource management")
    print("3. Cleaner, more readable code")
    print("4. Guaranteed cleanup even with exceptions")
    print("5. Reusable resource management patterns")


if __name__ == "__main__":
    main()
