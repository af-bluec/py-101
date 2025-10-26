"""
Python Functional Programming Demonstration

This module showcases functional programming concepts in Python:
- Higher-order functions
- Lambda functions and closures
- Map, filter, reduce operations
- Function composition
- Partial functions
- Decorators for functional programming
- Immutable data structures
- Monads and functional patterns

Functional programming emphasizes functions as first-class citizens,
immutability, and declarative programming style.
"""

import functools
import operator
import itertools
from typing import Callable, Any, List, Iterator, Optional, TypeVar, Generic
from collections.abc import Iterable
from dataclasses import dataclass
from copy import deepcopy


T = TypeVar('T')
U = TypeVar('U')


# Higher-order functions
def apply_twice(func: Callable[[T], T]) -> Callable[[T], T]:
    """
    Higher-order function that returns a function that applies func twice.
    
    Args:
        func: Function to apply twice
        
    Returns:
        Function that applies func twice
    """
    return lambda x: func(func(x))


def compose(*functions):
    """
    Compose multiple functions into a single function.
    
    Args:
        functions: Functions to compose (applied right to left)
        
    Returns:
        Composed function
    """
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def pipe(*functions):
    """
    Pipe functions together (left to right composition).
    
    Args:
        functions: Functions to pipe (applied left to right)
        
    Returns:
        Piped function
    """
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)


# Currying and partial application
def curry(func: Callable) -> Callable:
    """
    Convert a function to its curried form.
    
    Args:
        func: Function to curry
        
    Returns:
        Curried function
    """
    @functools.wraps(func)
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
    
    return curried


@curry
def add_three(a: int, b: int, c: int) -> int:
    """Example function for currying demonstration."""
    return a + b + c


# Functional data structures
@dataclass(frozen=True)
class ImmutableList(Generic[T]):
    """
    Simple immutable list implementation.
    """
    _data: tuple = ()
    
    def __init__(self, data: Iterable[T] = ()):
        object.__setattr__(self, '_data', tuple(data))
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def append(self, item: T) -> 'ImmutableList[T]':
        """Return new list with item appended."""
        return ImmutableList(self._data + (item,))
    
    def prepend(self, item: T) -> 'ImmutableList[T]':
        """Return new list with item prepended."""
        return ImmutableList((item,) + self._data)
    
    def map(self, func: Callable[[T], U]) -> 'ImmutableList[U]':
        """Apply function to all elements."""
        return ImmutableList(func(item) for item in self._data)
    
    def filter(self, predicate: Callable[[T], bool]) -> 'ImmutableList[T]':
        """Filter elements by predicate."""
        return ImmutableList(item for item in self._data if predicate(item))
    
    def reduce(self, func: Callable[[U, T], U], initial: U) -> U:
        """Reduce list to single value."""
        return functools.reduce(func, self._data, initial)
    
    def __repr__(self):
        return f"ImmutableList({list(self._data)})"


# Maybe monad for handling None values
@dataclass(frozen=True)
class Maybe(Generic[T]):
    """
    Maybe monad for handling optional values.
    """
    value: Optional[T]
    
    @classmethod
    def some(cls, value: T) -> 'Maybe[T]':
        """Create a Maybe with a value."""
        return cls(value)
    
    @classmethod
    def none(cls) -> 'Maybe[T]':
        """Create an empty Maybe."""
        return cls(None)
    
    def is_some(self) -> bool:
        """Check if Maybe has a value."""
        return self.value is not None
    
    def is_none(self) -> bool:
        """Check if Maybe is empty."""
        return self.value is None
    
    def map(self, func: Callable[[T], U]) -> 'Maybe[U]':
        """Apply function if value exists."""
        if self.is_some():
            return Maybe.some(func(self.value))
        return Maybe.none()
    
    def flat_map(self, func: Callable[[T], 'Maybe[U]']) -> 'Maybe[U]':
        """Apply function that returns Maybe."""
        if self.is_some():
            return func(self.value)
        return Maybe.none()
    
    def filter(self, predicate: Callable[[T], bool]) -> 'Maybe[T]':
        """Filter value by predicate."""
        if self.is_some() and predicate(self.value):
            return self
        return Maybe.none()
    
    def or_else(self, default: T) -> T:
        """Get value or default."""
        return self.value if self.is_some() else default
    
    def __repr__(self):
        return f"Some({self.value})" if self.is_some() else "None"


# Functional decorators
def memoize(func: Callable) -> Callable:
    """
    Memoization decorator for caching function results.
    
    Args:
        func: Function to memoize
        
    Returns:
        Memoized function
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        
        return cache[key]
    
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper


def tail_call_optimize(func: Callable) -> Callable:
    """
    Tail call optimization decorator (simplified version).
    
    Args:
        func: Function to optimize
        
    Returns:
        Optimized function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # This is a simplified example - real TCO is more complex
        result = func(*args, **kwargs)
        return result
    
    return wrapper


# Functional utilities
def take(n: int, iterable: Iterable[T]) -> List[T]:
    """Take first n items from iterable."""
    return list(itertools.islice(iterable, n))


def drop(n: int, iterable: Iterable[T]) -> Iterator[T]:
    """Drop first n items from iterable."""
    iterator = iter(iterable)
    for _ in range(n):
        next(iterator, None)
    return iterator


def partition(predicate: Callable[[T], bool], iterable: Iterable[T]) -> tuple:
    """Partition iterable into two lists based on predicate."""
    true_items, false_items = [], []
    for item in iterable:
        (true_items if predicate(item) else false_items).append(item)
    return true_items, false_items


def flat_map(func: Callable[[T], Iterable[U]], iterable: Iterable[T]) -> Iterator[U]:
    """Apply function and flatten results."""
    for item in iterable:
        yield from func(item)


# Example functions for demonstrations
@memoize
def fibonacci(n: int) -> int:
    """Fibonacci function with memoization."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def safe_divide(a: float, b: float) -> Maybe[float]:
    """Safe division that returns Maybe."""
    if b == 0:
        return Maybe.none()
    return Maybe.some(a / b)


def safe_sqrt(x: float) -> Maybe[float]:
    """Safe square root that returns Maybe."""
    if x < 0:
        return Maybe.none()
    return Maybe.some(x ** 0.5)


def demonstrate_higher_order_functions():
    """Demonstrate higher-order functions."""
    print("=== Higher-Order Functions Demo ===")
    
    # Apply twice
    increment = lambda x: x + 1
    double = lambda x: x * 2
    
    increment_twice = apply_twice(increment)
    double_twice = apply_twice(double)
    
    print(f"increment_twice(5) = {increment_twice(5)}")
    print(f"double_twice(3) = {double_twice(3)}")
    
    # Function composition
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    # Compose: square(multiply_by_two(add_one(x)))
    composed = compose(square, multiply_by_two, add_one)
    print(f"compose(square, *2, +1)(3) = {composed(3)}")
    
    # Pipe: add_one -> multiply_by_two -> square
    piped = pipe(add_one, multiply_by_two, square)
    print(f"pipe(+1, *2, square)(3) = {piped(3)}")


def demonstrate_map_filter_reduce():
    """Demonstrate map, filter, reduce operations."""
    print("\n=== Map, Filter, Reduce Demo ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original numbers: {numbers}")
    
    # Map
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Squared: {squared}")
    
    # Filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Reduce
    total = functools.reduce(operator.add, numbers, 0)
    product = functools.reduce(operator.mul, numbers, 1)
    print(f"Sum: {total}")
    print(f"Product: {product}")
    
    # Chaining operations
    result = functools.reduce(
        operator.add,
        map(lambda x: x ** 2,
            filter(lambda x: x % 2 == 0, numbers)),
        0
    )
    print(f"Sum of squares of even numbers: {result}")


def demonstrate_currying_and_partial():
    """Demonstrate currying and partial application."""
    print("\n=== Currying and Partial Application Demo ===")
    
    # Currying
    add_5 = add_three(5)  # Partially applied
    add_5_and_3 = add_5(3)  # Further partial application
    result = add_5_and_3(2)  # Final application
    
    print(f"Curried add_three(5)(3)(2) = {result}")
    
    # Partial application with functools.partial
    multiply = lambda x, y: x * y
    double = functools.partial(multiply, 2)
    triple = functools.partial(multiply, 3)
    
    print(f"double(8) = {double(8)}")
    print(f"triple(7) = {triple(7)}")
    
    # Partial with multiple arguments
    def greet(greeting: str, name: str, punctuation: str = "!") -> str:
        return f"{greeting}, {name}{punctuation}"
    
    hello = functools.partial(greet, "Hello")
    goodbye = functools.partial(greet, "Goodbye", punctuation=".")
    
    print(f"hello('Alice') = {hello('Alice')}")
    print(f"goodbye('Bob') = {goodbye('Bob')}")


def demonstrate_immutable_data_structures():
    """Demonstrate immutable data structures."""
    print("\n=== Immutable Data Structures Demo ===")
    
    # Immutable list
    original = ImmutableList([1, 2, 3])
    print(f"Original: {original}")
    
    # Operations return new lists
    appended = original.append(4)
    prepended = original.prepend(0)
    
    print(f"After append(4): {appended}")
    print(f"After prepend(0): {prepended}")
    print(f"Original unchanged: {original}")
    
    # Functional operations
    doubled = original.map(lambda x: x * 2)
    evens = original.filter(lambda x: x % 2 == 0)
    sum_result = original.reduce(operator.add, 0)
    
    print(f"Doubled: {doubled}")
    print(f"Evens: {evens}")
    print(f"Sum: {sum_result}")


def demonstrate_maybe_monad():
    """Demonstrate Maybe monad for safe computations."""
    print("\n=== Maybe Monad Demo ===")
    
    # Safe division chain
    def safe_computation(x: float, y: float, z: float) -> Maybe[float]:
        return (Maybe.some(x)
                .flat_map(lambda a: safe_divide(a, y))
                .flat_map(lambda b: safe_sqrt(b))
                .flat_map(lambda c: safe_divide(c, z)))
    
    # Successful computation
    result1 = safe_computation(16.0, 2.0, 2.0)
    print(f"safe_computation(16, 2, 2) = {result1}")
    print(f"Value or default: {result1.or_else(0.0)}")
    
    # Failed computation (division by zero)
    result2 = safe_computation(16.0, 0.0, 2.0)
    print(f"safe_computation(16, 0, 2) = {result2}")
    print(f"Value or default: {result2.or_else(0.0)}")
    
    # Failed computation (negative sqrt)
    result3 = safe_computation(-16.0, 2.0, 2.0)
    print(f"safe_computation(-16, 2, 2) = {result3}")
    print(f"Value or default: {result3.or_else(0.0)}")


def demonstrate_memoization():
    """Demonstrate memoization for optimization."""
    print("\n=== Memoization Demo ===")
    
    # Calculate fibonacci numbers
    print("Calculating Fibonacci numbers with memoization:")
    for i in [10, 20, 30]:
        result = fibonacci(i)
        print(f"fibonacci({i}) = {result}")
    
    # Show cache
    cache_size = len(fibonacci.cache)
    print(f"Cache size: {cache_size}")
    
    # Clear cache
    fibonacci.cache_clear()
    print("Cache cleared")


def demonstrate_functional_utilities():
    """Demonstrate functional utility functions."""
    print("\n=== Functional Utilities Demo ===")
    
    numbers = range(1, 21)
    
    # Take and drop
    first_five = take(5, numbers)
    after_ten = list(drop(10, numbers))
    
    print(f"First 5: {first_five}")
    print(f"After dropping 10: {after_ten}")
    
    # Partition
    evens, odds = partition(lambda x: x % 2 == 0, numbers)
    print(f"Evens: {evens}")
    print(f"Odds: {odds}")
    
    # Flat map
    words = ["hello", "world", "python"]
    characters = list(flat_map(list, words))
    print(f"All characters: {characters}")
    
    # Nested list flattening
    nested = [[1, 2], [3, 4, 5], [6]]
    flattened = list(flat_map(lambda x: x, nested))
    print(f"Flattened: {flattened}")


if __name__ == "__main__":
    print("=== Python Functional Programming Demo ===")
    
    demonstrate_higher_order_functions()
    demonstrate_map_filter_reduce()
    demonstrate_currying_and_partial()
    demonstrate_immutable_data_structures()
    demonstrate_maybe_monad()
    demonstrate_memoization()
    demonstrate_functional_utilities()
    
    print("\n=== Functional Programming Demo Complete ===")
