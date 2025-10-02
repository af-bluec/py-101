"""
Error handling and exception management examples.

This module demonstrates various error handling patterns, custom exceptions,
and best practices for managing errors in Python applications.
"""

import logging
from typing import Union, List, Dict, Any
from src.calculator import Calculator


# Custom exception classes
class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, message: str, field: str = None):
        super().__init__(message)
        self.field = field


class NetworkError(Exception):
    """Custom exception for network-related errors."""
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    pass


# Error handling examples
def demonstrate_basic_error_handling():
    """Demonstrate basic try-except patterns."""
    print("=== Basic Error Handling Demo ===")
    
    # Simple try-except
    print("1. Simple division error handling:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("   Error: Cannot divide by zero!")
    
    # Multiple exception types
    print("\n2. Multiple exception types:")
    test_values = ["123", "not_a_number", "45.67"]
    
    for value in test_values:
        try:
            number = int(value)
            result = 100 / number
            print(f"   {value} -> {result:.2f}")
        except ValueError:
            print(f"   {value} -> Invalid number format")
        except ZeroDivisionError:
            print(f"   {value} -> Division by zero")
    
    # Generic exception handling
    print("\n3. Generic exception handling:")
    try:
        # This will raise a TypeError
        result = "hello" + 42
    except Exception as e:
        print(f"   Caught exception: {type(e).__name__}: {e}")


def demonstrate_exception_details():
    """Demonstrate accessing exception details."""
    print("\n=== Exception Details Demo ===")
    
    import traceback
    
    def problematic_function(x):
        if x < 0:
            raise ValueError("Negative value not allowed")
        elif x == 0:
            raise ZeroDivisionError("Cannot process zero")
        else:
            return 100 / x
    
    test_values = [5, -1, 0, "not_a_number"]
    
    for value in test_values:
        try:
            result = problematic_function(value)
            print(f"   {value} -> {result}")
        except (ValueError, ZeroDivisionError, TypeError) as e:
            print(f"   {value} -> {type(e).__name__}: {e}")
        except Exception as e:
            print(f"   {value} -> Unexpected error: {e}")
            print("   Full traceback:")
            traceback.print_exc()


def demonstrate_try_except_else_finally():
    """Demonstrate complete try-except-else-finally structure."""
    print("\n=== Try-Except-Else-Finally Demo ===")
    
    def process_data(data):
        print(f"   Processing: {data}")
        
        try:
            # Simulate data processing
            if not data:
                raise ValueError("Empty data")
            
            if not isinstance(data, (int, float)):
                raise TypeError("Data must be numeric")
            
            if data < 0:
                raise ValueError("Data must be positive")
            
            result = data ** 2
            
        except ValueError as e:
            print(f"   Validation error: {e}")
            return None
        except TypeError as e:
            print(f"   Type error: {e}")
            return None
        else:
            print(f"   Processing successful: {result}")
            return result
        finally:
            print("   Cleanup completed")
    
    test_data = [4, -2, "invalid", None, 0, 3.14]
    
    for data in test_data:
        process_data(data)
        print()


def demonstrate_custom_exceptions():
    """Demonstrate custom exception classes."""
    print("=== Custom Exceptions Demo ===")
    
    def validate_user_data(user_data: Dict[str, Any]):
        """Validate user data and raise custom exceptions."""
        
        if not isinstance(user_data, dict):
            raise ValidationError("User data must be a dictionary")
        
        if "name" not in user_data:
            raise ValidationError("Name is required", field="name")
        
        if not user_data["name"] or not isinstance(user_data["name"], str):
            raise ValidationError("Name must be a non-empty string", field="name")
        
        if "age" in user_data:
            age = user_data["age"]
            if not isinstance(age, int) or age < 0 or age > 150:
                raise ValidationError("Age must be between 0 and 150", field="age")
        
        if "email" in user_data:
            email = user_data["email"]
            if "@" not in email:
                raise ValidationError("Invalid email format", field="email")
    
    # Test cases
    test_users = [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},  # Valid
        {"name": ""},  # Invalid name
        {"name": "Bob", "age": -5},  # Invalid age
        {"name": "Charlie", "email": "invalid-email"},  # Invalid email
        "not_a_dict"  # Invalid type
    ]
    
    for i, user in enumerate(test_users, 1):
        try:
            validate_user_data(user)
            print(f"   User {i}: Valid ✓")
        except ValidationError as e:
            field_info = f" (field: {e.field})" if e.field else ""
            print(f"   User {i}: {e}{field_info}")
        except Exception as e:
            print(f"   User {i}: Unexpected error: {e}")


def demonstrate_exception_chaining():
    """Demonstrate exception chaining and context."""
    print("\n=== Exception Chaining Demo ===")
    
    def database_operation():
        """Simulate a database operation that fails."""
        raise ConnectionError("Database connection failed")
    
    def business_logic():
        """Business logic that depends on database."""
        try:
            database_operation()
        except ConnectionError as e:
            # Chain the exception
            raise DataProcessingError("Failed to process user data") from e
    
    def api_handler():
        """API handler that catches and re-raises."""
        try:
            business_logic()
        except DataProcessingError:
            print("   API Error: Unable to complete request")
            print("   Original cause:")
            raise
    
    try:
        api_handler()
    except DataProcessingError as e:
        print(f"   Final error: {e}")
        if e.__cause__:
            print(f"   Caused by: {e.__cause__}")


def demonstrate_context_manager_errors():
    """Demonstrate error handling in context managers."""
    print("\n=== Context Manager Error Handling Demo ===")
    
    class ResourceManager:
        def __init__(self, name, should_fail=False):
            self.name = name
            self.should_fail = should_fail
            self.acquired = False
        
        def __enter__(self):
            print(f"   Acquiring resource: {self.name}")
            self.acquired = True
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            print(f"   Releasing resource: {self.name}")
            if exc_type:
                print(f"   Exception occurred: {exc_type.__name__}: {exc_value}")
            self.acquired = False
            return False  # Don't suppress exceptions
        
        def do_work(self):
            if self.should_fail:
                raise RuntimeError(f"Work failed for {self.name}")
            print(f"   Work completed for {self.name}")
    
    # Successful case
    print("1. Successful resource usage:")
    try:
        with ResourceManager("Database") as resource:
            resource.do_work()
    except Exception as e:
        print(f"   Caught: {e}")
    
    # Failure case
    print("\n2. Failed resource usage:")
    try:
        with ResourceManager("NetworkService", should_fail=True) as resource:
            resource.do_work()
    except Exception as e:
        print(f"   Caught: {e}")


def demonstrate_error_recovery():
    """Demonstrate error recovery and retry patterns."""
    print("\n=== Error Recovery Demo ===")
    
    import random
    import time
    
    class UnreliableService:
        def __init__(self, success_rate=0.3):
            self.success_rate = success_rate
            self.attempt_count = 0
        
        def call_service(self):
            self.attempt_count += 1
            if random.random() < self.success_rate:
                return f"Success on attempt {self.attempt_count}"
            else:
                raise NetworkError(f"Service unavailable (attempt {self.attempt_count})", 503)
    
    def retry_operation(operation, max_retries=3, delay=0.1):
        """Retry an operation with exponential backoff."""
        for attempt in range(max_retries):
            try:
                return operation()
            except NetworkError as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"   Attempt {attempt + 1} failed: {e}")
                time.sleep(delay * (2 ** attempt))  # Exponential backoff
        return None
    
    service = UnreliableService(success_rate=0.4)
    
    try:
        result = retry_operation(service.call_service, max_retries=4)
        print(f"   Final result: {result}")
    except NetworkError as e:
        print(f"   All retries failed: {e}")


def demonstrate_logging_errors():
    """Demonstrate error logging patterns."""
    print("\n=== Error Logging Demo ===")
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    
    logger = logging.getLogger(__name__)
    
    def risky_calculation(x, y):
        """Function that might fail with logging."""
        logger.info(f"Starting calculation: {x} / {y}")
        
        try:
            if y == 0:
                raise ZeroDivisionError("Division by zero")
            
            result = x / y
            logger.info(f"Calculation successful: {result}")
            return result
            
        except ZeroDivisionError as e:
            logger.error(f"Calculation failed: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.critical(f"Unexpected error: {e}", exc_info=True)
            raise
    
    test_cases = [(10, 2), (15, 0), (8, 4)]
    
    for x, y in test_cases:
        try:
            risky_calculation(x, y)
        except Exception:
            pass  # Already logged


def run_all_error_examples():
    """Run all error handling examples."""
    print("⚠️  ERROR HANDLING DEMONSTRATION ⚠️")
    print("=" * 50)
    
    demonstrate_basic_error_handling()
    demonstrate_exception_details()
    demonstrate_try_except_else_finally()
    demonstrate_custom_exceptions()
    demonstrate_exception_chaining()
    demonstrate_context_manager_errors()
    demonstrate_error_recovery()
    demonstrate_logging_errors()
    
    print("\n" + "=" * 50)
    print("✅ All error handling examples completed!")


if __name__ == "__main__":
    run_all_error_examples()
