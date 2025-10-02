"""
Generator functions for various number sequences and patterns.
"""
from typing import Generator, Iterator


def number_generator(start: int = 0, end: int = 10, step: int = 1) -> Generator[int, None, None]:
    """
    Generate numbers in a range.
    
    Args:
        start: Starting number (inclusive)
        end: Ending number (exclusive)
        step: Step size
        
    Yields:
        Numbers in the specified range
    """
    current = start
    while current < end:
        yield current
        current += step


def fibonacci_generator() -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers infinitely.
    
    Yields:
        Fibonacci numbers starting from 0, 1, 1, 2, 3, 5, ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator(limit: int = None) -> Generator[int, None, None]:
    """
    Generate prime numbers up to a limit or infinitely.
    
    Args:
        limit: Maximum number to check (None for infinite)
        
    Yields:
        Prime numbers
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while limit is None or num <= limit:
        if is_prime(num):
            yield num
        num += 1


def even_numbers(start: int = 0, limit: int = None) -> Generator[int, None, None]:
    """
    Generate even numbers starting from a given number.
    
    Args:
        start: Starting number
        limit: Maximum number (None for infinite)
        
    Yields:
        Even numbers
    """
    current = start if start % 2 == 0 else start + 1
    while limit is None or current <= limit:
        yield current
        current += 2


def odd_numbers(start: int = 1, limit: int = None) -> Generator[int, None, None]:
    """
    Generate odd numbers starting from a given number.
    
    Args:
        start: Starting number
        limit: Maximum number (None for infinite)
        
    Yields:
        Odd numbers
    """
    current = start if start % 2 == 1 else start + 1
    while limit is None or current <= limit:
        yield current
        current += 2


def square_generator(limit: int = None) -> Generator[int, None, None]:
    """
    Generate perfect squares.
    
    Args:
        limit: Maximum value (None for infinite)
        
    Yields:
        Perfect squares (1, 4, 9, 16, ...)
    """
    n = 1
    while True:
        square = n * n
        if limit is not None and square > limit:
            break
        yield square
        n += 1


def countdown_generator(start: int) -> Generator[int, None, None]:
    """
    Generate countdown from a starting number to 0.
    
    Args:
        start: Starting number for countdown
        
    Yields:
        Numbers counting down to 0
    """
    while start >= 0:
        yield start
        start -= 1


def alphabet_generator(uppercase: bool = False) -> Generator[str, None, None]:
    """
    Generate alphabet letters.
    
    Args:
        uppercase: Whether to generate uppercase letters
        
    Yields:
        Letters of the alphabet
    """
    start_ord = ord('A') if uppercase else ord('a')
    for i in range(26):
        yield chr(start_ord + i)


def batch_generator(iterable: Iterator, batch_size: int) -> Generator[list, None, None]:
    """
    Group items from an iterable into batches.
    
    Args:
        iterable: Input iterable
        batch_size: Size of each batch
        
    Yields:
        Lists containing batched items
    """
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    # Yield remaining items if any
    if batch:
        yield batch


def cycle_generator(items: list, max_cycles: int = None) -> Generator:
    """
    Cycle through items infinitely or for a specified number of cycles.
    
    Args:
        items: List of items to cycle through
        max_cycles: Maximum number of complete cycles (None for infinite)
        
    Yields:
        Items cycling through the list
    """
    if not items:
        return
    
    cycles = 0
    while max_cycles is None or cycles < max_cycles:
        for item in items:
            yield item
        cycles += 1


def random_number_generator(min_val: int = 1, max_val: int = 100, count: int = None) -> Generator[int, None, None]:
    """
    Generate random numbers within a range.
    
    Args:
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
        count: Number of random numbers to generate (None for infinite)
        
    Yields:
        Random integers within the specified range
    """
    import random
    
    generated = 0
    while count is None or generated < count:
        yield random.randint(min_val, max_val)
        generated += 1


# Example usage functions
def demonstrate_generators():
    """Demonstrate various generators with examples."""
    print("=== Generator Demonstrations ===")
    
    # Fibonacci first 10 numbers
    print("First 10 Fibonacci numbers:")
    fib_gen = fibonacci_generator()
    for i, num in enumerate(fib_gen):
        if i >= 10:
            break
        print(num, end=" ")
    print("\n")
    
    # First 10 prime numbers
    print("First 10 prime numbers:")
    prime_gen = prime_generator()
    for i, prime in enumerate(prime_gen):
        if i >= 10:
            break
        print(prime, end=" ")
    print("\n")
    
    # Even numbers up to 20
    print("Even numbers up to 20:")
    for num in even_numbers(0, 20):
        print(num, end=" ")
    print("\n")
    
    # Squares up to 100
    print("Perfect squares up to 100:")
    for square in square_generator(100):
        print(square, end=" ")
    print("\n")
    
    # Batch example
    print("Numbers 1-10 in batches of 3:")
    for batch in batch_generator(range(1, 11), 3):
        print(batch)
    print()
