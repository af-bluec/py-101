"""
Demonstration of error handling and exceptions in Python.
Covers try-except, custom exceptions, and best practices.
"""


# Basic exception handling
def divide_numbers(a, b):
    """Demonstrate basic try-except."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid types for division!")
        return None


# Multiple exception types
def process_list(data, index):
    """Handle multiple exception types."""
    try:
        value = data[index]
        result = 100 / value
        return result
    except IndexError:
        print(f"Error: Index {index} is out of range")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid type in list")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Using else and finally
def read_file_safe(filename):
    """Demonstrate else and finally clauses."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    else:
        print("File read successfully")
        return content
    finally:
        print("Cleanup completed")


# Custom exceptions
class InsufficientFundsError(Exception):
    """Custom exception for banking operations."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance=${balance}, attempted=${amount}")


class InvalidAgeError(Exception):
    """Custom exception for age validation."""
    pass


class BankAccount:
    """Class demonstrating custom exceptions."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


def validate_age(age):
    """Validate age and raise custom exception."""
    if not isinstance(age, int):
        raise InvalidAgeError("Age must be an integer")
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age seems unrealistic")
    return True


# Exception chaining
def process_data(data):
    """Demonstrate exception chaining."""
    try:
        result = int(data) * 2
        return result
    except ValueError as e:
        raise TypeError("Data must be convertible to integer") from e


# Context managers for resource management
class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as e:
            print(f"Error opening file: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions


# Assertion errors
def calculate_average(numbers):
    """Use assertions for debugging."""
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All elements must be numbers"
    return sum(numbers) / len(numbers)


def main():
    print("=== BASIC EXCEPTION HANDLING ===")
    print(f"10 / 2 = {divide_numbers(10, 2)}")
    print(f"10 / 0 = {divide_numbers(10, 0)}")
    print(f"'10' / 2 = {divide_numbers('10', 2)}")
    
    print("\n=== MULTIPLE EXCEPTIONS ===")
    data = [10, 20, 0, 30]
    process_list(data, 0)  # Success
    process_list(data, 2)  # ZeroDivisionError
    process_list(data, 10)  # IndexError
    
    print("\n=== ELSE AND FINALLY ===")
    # Create a test file
    with open("test.txt", "w") as f:
        f.write("Test content")
    
    content = read_file_safe("test.txt")
    read_file_safe("nonexistent.txt")
    
    # Cleanup
    import os
    if os.path.exists("test.txt"):
        os.remove("test.txt")
    
    print("\n=== CUSTOM EXCEPTIONS ===")
    account = BankAccount("Alice", 100)
    try:
        account.withdraw(50)
        print(f"Withdrawal successful. Balance: ${account.balance}")
        account.withdraw(100)  # This will raise an exception
    except InsufficientFundsError as e:
        print(f"Transaction failed: {e}")
    
    print("\n=== AGE VALIDATION ===")
    test_ages = [25, -5, "thirty", 200]
    for age in test_ages:
        try:
            validate_age(age)
            print(f"Age {age} is valid")
        except InvalidAgeError as e:
            print(f"Invalid age {age}: {e}")
    
    print("\n=== EXCEPTION CHAINING ===")
    try:
        process_data("abc")
    except TypeError as e:
        print(f"Error: {e}")
        print(f"Caused by: {e.__cause__}")
    
    print("\n=== ASSERTIONS ===")
    try:
        avg = calculate_average([10, 20, 30])
        print(f"Average: {avg}")
        avg = calculate_average([])  # This will raise AssertionError
    except AssertionError as e:
        print(f"Assertion failed: {e}")
    
    print("\n=== BEST PRACTICES ===")
    print("1. Catch specific exceptions, not generic Exception")
    print("2. Use custom exceptions for domain-specific errors")
    print("3. Always clean up resources (use context managers)")
    print("4. Don't suppress exceptions unless necessary")
    print("5. Log errors for debugging")


if __name__ == "__main__":
    main()
