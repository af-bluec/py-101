"""
Demonstration of iterators and generators in Python.
Covers custom iterators, generator functions, and advanced iteration patterns.
"""

import itertools


# Custom Iterator
class Countdown:
    """Custom iterator that counts down from a number."""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


class FibonacciIterator:
    """Iterator for Fibonacci sequence."""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


# Generator Functions
def simple_generator():
    """Basic generator function."""
    yield 1
    yield 2
    yield 3


def infinite_sequence():
    """Generator that produces infinite sequence."""
    num = 0
    while True:
        yield num
        num += 1


def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def range_generator(start, end, step=1):
    """Custom range implementation using generator."""
    current = start
    while current < end:
        yield current
        current += step


def file_reader(filename):
    """Generator for reading large files line by line."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")


# Generator Expressions
def demonstrate_generator_expressions():
    """Show generator expressions."""
    print("=== GENERATOR EXPRESSIONS ===")
    
    # Basic generator expression
    squares = (x**2 for x in range(10))
    print(f"Generator: {squares}")
    print(f"Values: {list(squares)}")
    
    # Memory efficient
    sum_of_squares = sum(x**2 for x in range(1000000))
    print(f"Sum of million squares: {sum_of_squares}")
    
    # Filtering
    even_squares = (x**2 for x in range(20) if x % 2 == 0)
    print(f"Even squares: {list(even_squares)}")


# Advanced Generator Patterns
def chain_generators(*iterables):
    """Chain multiple iterables."""
    for iterable in iterables:
        for item in iterable:
            yield item


def take(n, iterable):
    """Take first n items from iterable."""
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item


def filter_generator(predicate, iterable):
    """Filter items based on predicate."""
    for item in iterable:
        if predicate(item):
            yield item


# Generator with send()
def echo_generator():
    """Generator that can receive values."""
    value = None
    while True:
        value = yield value
        if value is not None:
            value = f"Echo: {value}"


# Itertools demonstrations
def demonstrate_itertools():
    """Show useful itertools functions."""
    print("\n=== ITERTOOLS ===")
    
    # count - infinite counter
    counter = itertools.count(start=10, step=2)
    print(f"First 5 from count(10, 2): {list(take(5, counter))}")
    
    # cycle - repeat elements infinitely
    colors = itertools.cycle(['red', 'green', 'blue'])
    print(f"First 7 from cycle: {list(take(7, colors))}")
    
    # repeat - repeat single value
    repeated = itertools.repeat('A', 5)
    print(f"Repeat 'A' 5 times: {list(repeated)}")
    
    # chain - combine iterables
    chained = itertools.chain([1, 2, 3], ['a', 'b', 'c'])
    print(f"Chained: {list(chained)}")
    
    # compress - filter based on selectors
    data = ['A', 'B', 'C', 'D', 'E']
    selectors = [1, 0, 1, 0, 1]
    compressed = itertools.compress(data, selectors)
    print(f"Compressed: {list(compressed)}")
    
    # dropwhile - drop while condition is true
    numbers = [1, 3, 5, 6, 7, 8, 9]
    dropped = itertools.dropwhile(lambda x: x < 5, numbers)
    print(f"Drop while < 5: {list(dropped)}")
    
    # takewhile - take while condition is true
    taken = itertools.takewhile(lambda x: x < 5, numbers)
    print(f"Take while < 5: {list(taken)}")
    
    # groupby - group consecutive elements
    data = [1, 1, 2, 2, 2, 3, 3, 1, 1]
    grouped = [(k, list(g)) for k, g in itertools.groupby(data)]
    print(f"Grouped: {grouped}")
    
    # combinations
    items = ['A', 'B', 'C']
    combos = list(itertools.combinations(items, 2))
    print(f"Combinations of 2: {combos}")
    
    # permutations
    perms = list(itertools.permutations(items, 2))
    print(f"Permutations of 2: {perms}")
    
    # product - cartesian product
    prod = list(itertools.product([1, 2], ['a', 'b']))
    print(f"Product: {prod}")


def demonstrate_yield_from():
    """Demonstrate yield from for delegating to sub-generators."""
    print("\n=== YIELD FROM ===")
    
    def sub_generator(n):
        for i in range(n):
            yield i
    
    def main_generator():
        yield from sub_generator(3)
        yield from sub_generator(3)
    
    result = list(main_generator())
    print(f"Yield from result: {result}")


def practical_examples():
    """Practical uses of generators."""
    print("\n=== PRACTICAL EXAMPLES ===")
    
    # Reading large files efficiently
    def process_log_file(filename):
        """Process log file line by line."""
        for line in file_reader(filename):
            if "ERROR" in line:
                yield line
    
    # Infinite data stream
    def data_stream():
        """Simulate infinite data stream."""
        import random
        while True:
            yield random.randint(1, 100)
    
    stream = data_stream()
    sample = [next(stream) for _ in range(5)]
    print(f"Sample from data stream: {sample}")
    
    # Pipeline processing
    def pipeline_example():
        """Chain multiple generators for data processing."""
        numbers = range(100)
        evens = (x for x in numbers if x % 2 == 0)
        squares = (x**2 for x in evens)
        result = list(take(5, squares))
        return result
    
    print(f"Pipeline result: {pipeline_example()}")
    
    # Batch processing
    def batch_generator(iterable, batch_size):
        """Generate batches from iterable."""
        batch = []
        for item in iterable:
            batch.append(item)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
    
    data = range(25)
    batches = list(batch_generator(data, 10))
    print(f"Batches of 10: {batches}")


def main():
    print("=== CUSTOM ITERATORS ===")
    countdown = Countdown(5)
    print(f"Countdown: {list(countdown)}")
    
    fib = FibonacciIterator(10)
    print(f"Fibonacci: {list(fib)}")
    
    print("\n=== GENERATOR FUNCTIONS ===")
    gen = simple_generator()
    print(f"Simple generator: {list(gen)}")
    
    fib_gen = fibonacci_generator(10)
    print(f"Fibonacci generator: {list(fib_gen)}")
    
    custom_range = range_generator(0, 10, 2)
    print(f"Custom range: {list(custom_range)}")
    
    demonstrate_generator_expressions()
    
    print("\n=== ADVANCED PATTERNS ===")
    chained = chain_generators([1, 2, 3], ['a', 'b', 'c'], [True, False])
    print(f"Chained: {list(chained)}")
    
    inf = infinite_sequence()
    first_ten = list(take(10, inf))
    print(f"First 10 from infinite: {first_ten}")
    
    numbers = range(20)
    evens = filter_generator(lambda x: x % 2 == 0, numbers)
    print(f"Filtered evens: {list(evens)}")
    
    demonstrate_itertools()
    demonstrate_yield_from()
    practical_examples()
    
    print("\n=== GENERATOR WITH SEND ===")
    echo = echo_generator()
    next(echo)  # Prime the generator
    print(echo.send("Hello"))
    print(echo.send("World"))


if __name__ == "__main__":
    main()
