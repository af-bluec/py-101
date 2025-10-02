"""
Demo examples showcasing various Python features.

This module contains demonstrations of Python language features
including loops, conditionals, exception handling, and more.
"""

import logging
from datetime import date
from typing import Generator, List


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PythonFeatureDemo:
    """
    A class that demonstrates various Python features.
    """
    
    def __init__(self):
        self.demo_data = {
            "name": "Alice",
            "age": 30,
            "skills": ["Python", "JavaScript", "SQL"]
        }
    
    def demonstrate_loops(self) -> None:
        """Demonstrate different types of loops."""
        logger.info("Demonstrating loops...")
        
        # For loop with range
        logger.info("For loop with range:")
        for i in range(1, 6):
            logger.info(f"  Count: {i}")
        
        # While loop
        logger.info("While loop:")
        count = 0
        while count < 3:
            logger.info(f"  While iteration: {count}")
            count += 1
        
        # For loop with list
        logger.info("For loop with list:")
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            logger.info(f"  Fruit: {fruit}")
    
    def demonstrate_conditionals(self, age: int = 25) -> str:
        """
        Demonstrate conditional statements.
        
        Args:
            age (int): Age to evaluate
            
        Returns:
            str: Age category
        """
        logger.info(f"Evaluating age: {age}")
        
        if age >= 18:
            category = "Adult"
        elif age >= 13:
            category = "Teenager"
        else:
            category = "Child"
        
        logger.info(f"Category: {category}")
        return category
    
    def demonstrate_exception_handling(self) -> None:
        """Demonstrate exception handling patterns."""
        logger.info("Demonstrating exception handling...")
        
        # Basic try-except
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            logger.error(f"Caught division by zero: {e}")
        
        # Try-except-else
        try:
            num = int("123")
        except ValueError:
            logger.error("Invalid number format")
        else:
            logger.info(f"Successfully parsed number: {num}")
        
        # Try-except-finally
        try:
            with open("nonexistent.txt", "r") as file:
                content = file.read()
        except FileNotFoundError:
            logger.warning("File not found, using default content")
        finally:
            logger.info("Cleanup completed")
    
    def demonstrate_data_structures(self) -> dict:
        """
        Demonstrate various data structures.
        
        Returns:
            dict: Examples of different data structures
        """
        logger.info("Demonstrating data structures...")
        
        # List operations
        numbers = [1, 2, 3, 4, 5]
        numbers.append(6)
        
        # Dictionary operations
        person = {"name": "Bob", "age": 28, "city": "New York"}
        person["occupation"] = "Developer"
        
        # Set operations
        unique_numbers = {1, 2, 3, 3, 4, 4, 5}
        
        # Tuple (immutable)
        coordinates = (10, 20)
        
        return {
            "list_example": numbers,
            "dict_example": person,
            "set_example": unique_numbers,
            "tuple_example": coordinates
        }
    
    def demonstrate_comprehensions(self) -> dict:
        """
        Demonstrate list, dict, and set comprehensions.
        
        Returns:
            dict: Examples of comprehensions
        """
        logger.info("Demonstrating comprehensions...")
        
        numbers = range(1, 11)
        
        # List comprehension
        squares = [x**2 for x in numbers if x % 2 == 0]
        
        # Dictionary comprehension
        square_dict = {x: x**2 for x in numbers if x <= 5}
        
        # Set comprehension
        unique_squares = {x**2 for x in numbers}
        
        return {
            "list_comprehension": squares,
            "dict_comprehension": square_dict,
            "set_comprehension": unique_squares
        }
    
    def demonstrate_generators(self) -> Generator[int, None, None]:
        """
        Demonstrate generator functions.
        
        Yields:
            int: Numbers from 0 to 4
        """
        logger.info("Demonstrating generators...")
        for i in range(5):
            logger.info(f"Yielding: {i}")
            yield i
    
    def demonstrate_context_manager(self) -> None:
        """Demonstrate context manager usage."""
        logger.info("Demonstrating context manager...")
        
        # Simulate context manager behavior
        class SimpleContextManager:
            def __enter__(self):
                logger.info("Entering context")
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                logger.info("Exiting context")
                return False
        
        with SimpleContextManager():
            logger.info("Inside context manager")
    
    def demonstrate_string_formatting(self, name: str = "World") -> List[str]:
        """
        Demonstrate different string formatting methods.
        
        Args:
            name (str): Name to use in formatting examples
            
        Returns:
            List[str]: Examples of formatted strings
        """
        age = 25
        
        # f-string (modern)
        f_string = f"Hello {name}, you are {age} years old!"
        
        # .format() method
        format_method = "Hello {}, you are {} years old!".format(name, age)
        
        # % formatting (old style)
        percent_format = "Hello %s, you are %d years old!" % (name, age)
        
        return [f_string, format_method, percent_format]
    
    def demonstrate_date_operations(self) -> dict:
        """
        Demonstrate date operations.
        
        Returns:
            dict: Date-related information
        """
        today = date.today()
        
        return {
            "today": str(today),
            "year": today.year,
            "month": today.month,
            "day": today.day,
            "weekday": today.strftime("%A"),
            "formatted": today.strftime("%B %d, %Y")
        }
    
    def run_all_demos(self) -> None:
        """Run all demonstration methods."""
        logger.info("Starting Python feature demonstrations...")
        
        self.demonstrate_loops()
        self.demonstrate_conditionals()
        self.demonstrate_exception_handling()
        
        data_structures = self.demonstrate_data_structures()
        logger.info(f"Data structures demo: {data_structures}")
        
        comprehensions = self.demonstrate_comprehensions()
        logger.info(f"Comprehensions demo: {comprehensions}")
        
        logger.info("Generator demo:")
        for value in self.demonstrate_generators():
            logger.info(f"Generated value: {value}")
        
        self.demonstrate_context_manager()
        
        string_formats = self.demonstrate_string_formatting()
        for fmt in string_formats:
            logger.info(f"String format: {fmt}")
        
        date_info = self.demonstrate_date_operations()
        logger.info(f"Date operations: {date_info}")
        
        logger.info("All demonstrations completed!")
