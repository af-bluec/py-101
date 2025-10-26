"""
Python Generators and Iterators Demonstration

This module showcases generators and iterators in Python:
- Generator functions with yield
- Generator expressions
- Custom iterators with __iter__ and __next__
- Itertools usage
- Coroutines and generator-based programming
- Memory-efficient data processing

Generators provide a memory-efficient way to create iterators and process
large amounts of data without loading everything into memory at once.
"""

import itertools
import random
import time
from typing import Iterator, Generator, Any, Iterable


# Basic generator function
def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers up to a limit.
    
    Args:
        limit: Maximum number of Fibonacci numbers to generate
        
    Yields:
        Fibonacci numbers
    """
    a, b = 0, 1
    count = 0
    
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def prime_generator(max_num: int) -> Generator[int, None, None]:
    """
    Generate prime numbers up to max_num using the Sieve of Eratosthenes.
    
    Args:
        max_num: Maximum number to check for primes
        
    Yields:
        Prime numbers
    """
    if max_num < 2:
        return
    
    # Initialize list of candidates
    candidates = list(range(2, max_num + 1))
    
    while candidates:
        # First number is always prime
        prime = candidates[0]
        yield prime
        
        # Remove all multiples of this prime
        candidates = [n for n in candidates if n % prime != 0]


def file_line_reader(filename: str) -> Generator[str, None, None]:
    """
    Generator to read file lines one at a time (memory efficient).
    
    Args:
        filename: Path to the file to read
        
    Yields:
        Lines from the file
    """
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                yield f"Line {line_num}: {line.strip()}"
    except FileNotFoundError:
        yield f"File '{filename}' not found"


class NumberRange:
    """
    A custom iterator class that generates numbers in a range.
    
    This demonstrates the iterator protocol using __iter__ and __next__.
    """
    
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        """Return the iterator object itself."""
        return self
    
    def __next__(self):
        """Return the next value in the sequence."""
        if (self.step > 0 and self.current >= self.end) or \
           (self.step < 0 and self.current <= self.end):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value


class RandomNumberStream:
    """
    An infinite iterator that generates random numbers.
    """
    
    def __init__(self, min_val: int = 1, max_val: int = 100):
        self.min_val = min_val
        self.max_val = max_val
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return random.randint(self.min_val, self.max_val)


def data_processor(data_source: Iterable[Any]) -> Generator[dict, None, None]:
    """
    A generator that processes data items and yields results.
    
    Args:
        data_source: An iterable source of data
        
    Yields:
        Processed data dictionaries
    """
    for i, item in enumerate(data_source):
        # Simulate some processing time
        time.sleep(0.01)
        
        processed_item = {
            'id': i,
            'original': item,
            'processed': str(item).upper() if isinstance(item, str) else item * 2,
            'timestamp': time.time()
        }
        
        yield processed_item


def generator_pipeline(numbers: Iterable[int]) -> Generator[int, None, None]:
    """
    A generator pipeline that applies multiple transformations.
    
    Args:
        numbers: Input numbers
        
    Yields:
        Transformed numbers
    """
    # Filter even numbers
    even_numbers = (n for n in numbers if n % 2 == 0)
    
    # Square the even numbers
    squared = (n ** 2 for n in even_numbers)
    
    # Filter numbers greater than 50
    filtered = (n for n in squared if n > 50)
    
    # Yield the results
    yield from filtered


def batch_generator(iterable: Iterable[Any], batch_size: int) -> Generator[list, None, None]:
    """
    Generator that yields batches of items from an iterable.
    
    Args:
        iterable: Source iterable
        batch_size: Size of each batch
        
    Yields:
        Lists containing batches of items
    """
    iterator = iter(iterable)
    
    while True:
        batch = list(itertools.islice(iterator, batch_size))
        if not batch:
            break
        yield batch


def coroutine_example():
    """
    Demonstrate a simple coroutine using generators.
    """
    def accumulator() -> Generator[int, int, None]:
        """A coroutine that accumulates sent values."""
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value
    
    # Create and initialize the coroutine
    acc = accumulator()
    next(acc)  # Prime the coroutine
    
    print("\n=== Coroutine Example ===")
    print(f"Initial total: {acc.send(10)}")  # Send 10
    print(f"After adding 20: {acc.send(20)}")  # Send 20
    print(f"After adding 5: {acc.send(5)}")   # Send 5
    
    acc.close()  # Close the coroutine


def demonstrate_itertools():
    """Demonstrate various itertools functions with generators."""
    print("\n=== Itertools Demonstration ===")
    
    # itertools.count - infinite counter
    print("1. Infinite counter (first 5):")
    counter = itertools.count(start=10, step=2)
    for i, value in enumerate(counter):
        if i >= 5:
            break
        print(f"  {value}")
    
    # itertools.cycle - cycle through values
    print("\n2. Cycling through colors (first 8):")
    colors = itertools.cycle(['red', 'green', 'blue'])
    for i, color in enumerate(colors):
        if i >= 8:
            break
        print(f"  {color}")
    
    # itertools.chain - chain iterables together
    print("\n3. Chaining iterables:")
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [10, 20]
    
    chained = itertools.chain(list1, list2, list3)
    print(f"  Chained: {list(chained)}")
    
    # itertools.combinations
    print("\n4. Combinations:")
    items = ['A', 'B', 'C', 'D']
    combinations = itertools.combinations(items, 2)
    print(f"  2-combinations of {items}:")
    for combo in combinations:
        print(f"    {combo}")
    
    # itertools.permutations
    print("\n5. Permutations:")
    perms = itertools.permutations(['X', 'Y', 'Z'], 2)
    print(f"  2-permutations of ['X', 'Y', 'Z']:")
    for perm in perms:
        print(f"    {perm}")


def memory_efficient_processing():
    """Demonstrate memory-efficient data processing with generators."""
    print("\n=== Memory Efficient Processing ===")
    
    # Generate large dataset without storing in memory
    def large_dataset(size: int) -> Generator[int, None, None]:
        """Generate a large dataset without storing it in memory."""
        for i in range(size):
            yield random.randint(1, 1000)
    
    # Process in batches
    dataset = large_dataset(100)
    batch_processor = batch_generator(dataset, batch_size=10)
    
    print("Processing data in batches of 10:")
    for batch_num, batch in enumerate(batch_processor, 1):
        batch_sum = sum(batch)
        batch_avg = batch_sum / len(batch)
        print(f"  Batch {batch_num}: Sum={batch_sum}, Average={batch_avg:.2f}")


if __name__ == "__main__":
    print("=== Python Generators and Iterators Demo ===")
    
    # Basic generator function
    print("\n1. Fibonacci Generator:")
    fib_gen = fibonacci_generator(10)
    fib_numbers = list(fib_gen)
    print(f"First 10 Fibonacci numbers: {fib_numbers}")
    
    # Prime generator
    print("\n2. Prime Number Generator:")
    prime_gen = prime_generator(30)
    primes = list(prime_gen)
    print(f"Prime numbers up to 30: {primes}")
    
    # Custom iterator class
    print("\n3. Custom Iterator (NumberRange):")
    number_range = NumberRange(5, 20, 3)
    numbers = list(number_range)
    print(f"Numbers from 5 to 20 (step 3): {numbers}")
    
    # Generator expressions
    print("\n4. Generator Expressions:")
    squares_gen = (x ** 2 for x in range(1, 11))
    even_squares = [x for x in squares_gen if x % 2 == 0]
    print(f"Even squares from 1-10: {even_squares}")
    
    # Generator pipeline
    print("\n5. Generator Pipeline:")
    input_numbers = range(1, 20)
    processed_numbers = list(generator_pipeline(input_numbers))
    print(f"Pipeline result: {processed_numbers}")
    
    # Data processing generator
    print("\n6. Data Processing Generator:")
    sample_data = ['hello', 'world', 'python', 'generator']
    processor = data_processor(sample_data)
    
    print("Processed data:")
    for processed in processor:
        print(f"  {processed}")
    
    # Infinite iterator (limited output)
    print("\n7. Infinite Random Number Stream (first 5):")
    random_stream = RandomNumberStream(1, 10)
    random_iterator = iter(random_stream)
    
    for i in range(5):
        print(f"  Random number {i + 1}: {next(random_iterator)}")
    
    # Batch processing
    print("\n8. Batch Processing:")
    data = range(1, 26)  # Numbers 1-25
    batches = list(batch_generator(data, 7))
    
    for i, batch in enumerate(batches, 1):
        print(f"  Batch {i}: {batch}")
    
    # Run additional demonstrations
    coroutine_example()
    demonstrate_itertools()
    memory_efficient_processing()
    
    print("\n=== Generators and Iterators Demo Complete ===")
