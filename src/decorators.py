"""
Decorator functions and utilities.

This module provides various decorator examples and utilities for
function enhancement, logging, timing, and other common decorator patterns.
"""

import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator to time function execution.
    
    Args:
        func: Function to time
        
    Returns:
        Wrapped function that prints execution time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def logger(func: Callable) -> Callable:
    """
    Decorator to log function calls.
    
    Args:
        func: Function to log
        
    Returns:
        Wrapped function that logs calls
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry function execution on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between attempts in seconds
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


def validate_types(**expected_types):
    """
    Decorator to validate function argument types.
    
    Args:
        **expected_types: Expected types for arguments
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Validate types
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"Expected {expected_type} for {param_name}, got {type(value)}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def cache(func: Callable) -> Callable:
    """
    Simple memoization decorator.
    
    Args:
        func: Function to cache results for
        
    Returns:
        Wrapped function with caching
    """
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from args and kwargs
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache_dict:
            print(f"Cache hit for {func.__name__}")
            return cache_dict[key]
        
        result = func(*args, **kwargs)
        cache_dict[key] = result
        print(f"Cache miss for {func.__name__}, result cached")
        return result
    
    wrapper.cache_clear = lambda: cache_dict.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache_dict)}"
    return wrapper


def deprecated(message: str = "This function is deprecated"):
    """
    Decorator to mark functions as deprecated.
    
    Args:
        message: Custom deprecation message
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import warnings
            warnings.warn(f"{func.__name__} is deprecated. {message}", 
                         DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def rate_limit(max_calls: int, time_window: float):
    """
    Decorator to limit function call rate.
    
    Args:
        max_calls: Maximum number of calls allowed
        time_window: Time window in seconds
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        calls = []
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove old calls outside the time window
            calls[:] = [call_time for call_time in calls if now - call_time < time_window]
            
            if len(calls) >= max_calls:
                raise RuntimeError(f"Rate limit exceeded: {max_calls} calls per {time_window}s")
            
            calls.append(now)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


def singleton(cls):
    """
    Decorator to implement singleton pattern for classes.
    
    Args:
        cls: Class to make singleton
        
    Returns:
        Singleton class wrapper
    """
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


def property_decorator(getter: Callable = None, setter: Callable = None, deleter: Callable = None):
    """
    Custom property decorator example.
    
    Args:
        getter: Getter function
        setter: Setter function
        deleter: Deleter function
        
    Returns:
        Property descriptor
    """
    def decorator(func: Callable) -> property:
        return property(getter or func, setter, deleter, func.__doc__)
    return decorator


# Example of a class-based decorator
class CountCalls:
    """Decorator class to count function calls."""
    
    def __init__(self, func: Callable):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)
    
    def get_count(self) -> int:
        """Get the current call count."""
        return self.count
    
    def reset_count(self) -> None:
        """Reset the call count to zero."""
        self.count = 0
