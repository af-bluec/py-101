"""
Function decorators for common functionality.
"""
import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator that measures and prints the execution time of a function.
    
    Args:
        func: Function to be timed
        
    Returns:
        Wrapped function that prints execution time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def logger(func: Callable) -> Callable:
    """
    Decorator that logs function calls with arguments and return values.
    
    Args:
        func: Function to be logged
        
    Returns:
        Wrapped function that logs calls
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={v!r}" for k, v in kwargs.items()])
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator that retries a function call on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retries in seconds
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed.")
            
            raise last_exception
        return wrapper
    return decorator


def validate_types(**expected_types):
    """
    Decorator that validates function argument types.
    
    Args:
        **expected_types: Mapping of argument names to expected types
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
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
                        raise TypeError(
                            f"Argument '{param_name}' must be of type {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def cache(func: Callable) -> Callable:
    """
    Simple memoization decorator for caching function results.
    
    Args:
        func: Function to be cached
        
    Returns:
        Wrapped function with caching
    """
    cache_dict = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache_dict:
            print(f"Cache hit for {func.__name__}")
            return cache_dict[key]
        
        print(f"Cache miss for {func.__name__}")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    
    return wrapper


def deprecated(message: str = "This function is deprecated"):
    """
    Decorator to mark functions as deprecated.
    
    Args:
        message: Deprecation message
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            import warnings
            warnings.warn(
                f"{func.__name__} is deprecated. {message}",
                DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Example decorated functions
@timer
@logger
def example_function(name: str) -> str:
    """Example function with multiple decorators."""
    time.sleep(0.1)  # Simulate some work
    return f"Hello, {name}!"


@cache
def expensive_calculation(n: int) -> int:
    """Example of cached function (simulates expensive operation)."""
    time.sleep(0.1)  # Simulate expensive computation
    return n ** 2


@validate_types(x=int, y=int)
def add_numbers(x: int, y: int) -> int:
    """Example function with type validation."""
    return x + y
