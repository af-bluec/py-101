"""
Advanced Python examples and demonstrations.

This module showcases advanced Python features including decorators,
generators, context managers, and other sophisticated language constructs.
"""

from src.decorators import timer, logger, cache, CountCalls
from src.advanced_features import (
    countdown_generator, fibonacci_generator, timer_context,
    create_lambda_functions, CountUp, DatabaseConnection
)


def demonstrate_decorators():
    """Demonstrate various decorator patterns."""
    print("=== Decorators Demo ===")
    
    # Function with timer decorator
    @timer
    def slow_function():
        import time
        time.sleep(0.1)  # Simulate slow operation
        return "Completed!"
    
    print("Executing timed function:")
    result = slow_function()
    print(f"Result: {result}")
    
    # Function with logger decorator
    @logger
    def calculate_area(length, width):
        return length * width
    
    print("\nExecuting logged function:")
    area = calculate_area(5, 3)
    
    # Function with cache decorator
    @cache
    def expensive_calculation(n):
        print(f"Performing expensive calculation for {n}")
        return n ** 2 + n * 10
    
    print("\nExecuting cached function:")
    result1 = expensive_calculation(5)
    result2 = expensive_calculation(5)  # Should hit cache
    result3 = expensive_calculation(10)
    
    # Class-based decorator
    @CountCalls
    def greet(name):
        return f"Hello, {name}!"
    
    print("\nExecuting function with call counter:")
    greet("Alice")
    greet("Bob")
    greet("Charlie")


def demonstrate_generators():
    """Demonstrate generator functions and expressions."""
    print("\n=== Generators Demo ===")
    
    # Countdown generator
    print("Countdown generator:")
    for num in countdown_generator(5):
        print(f"  {num}")
    
    # Fibonacci generator (first 10 numbers)
    print("\nFirst 10 Fibonacci numbers:")
    fib_gen = fibonacci_generator()
    for _ in range(10):
        print(f"  {next(fib_gen)}")
    
    # Generator expression
    print("\nSquares generator expression:")
    squares_gen = (x**2 for x in range(1, 6))
    for square in squares_gen:
        print(f"  {square}")
    
    # Generator with yield from
    def combined_generator():
        yield from range(1, 4)
        yield from ['a', 'b', 'c']
        yield from countdown_generator(3)
    
    print("\nCombined generator:")
    for item in combined_generator():
        print(f"  {item}")


def demonstrate_context_managers():
    """Demonstrate context manager usage."""
    print("\n=== Context Managers Demo ===")
    
    # Timer context manager
    print("Using timer context manager:")
    with timer_context():
        # Simulate some work
        total = sum(range(1000000))
        print(f"Sum calculated: {total}")
    
    # Custom context manager simulation
    print("\nSimulating file context manager:")
    class SimulatedFile:
        def __init__(self, name):
            self.name = name
            self.is_open = False
        
        def __enter__(self):
            print(f"Opening file: {self.name}")
            self.is_open = True
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            print(f"Closing file: {self.name}")
            self.is_open = False
        
        def read(self):
            if self.is_open:
                return "File content here..."
            return "File is closed"
    
    with SimulatedFile("example.txt") as file:
        content = file.read()
        print(f"Content: {content}")


def demonstrate_lambda_functions():
    """Demonstrate lambda functions and functional programming."""
    print("\n=== Lambda Functions Demo ===")
    
    # Get lambda functions
    lambdas = create_lambda_functions()
    
    # Use various lambda functions
    numbers = [1, 2, 3, 4, 5]
    print(f"Original numbers: {numbers}")
    
    squared = list(map(lambdas['square'], numbers))
    print(f"Squared: {squared}")
    
    evens = list(filter(lambdas['is_even'], numbers))
    print(f"Even numbers: {evens}")
    
    # Lambda with reduce
    from functools import reduce
    product = reduce(lambdas['multiply'], numbers)
    print(f"Product of all numbers: {product}")
    
    # Sorting with lambda
    words = ["python", "java", "c++", "javascript", "go"]
    sorted_by_length = sorted(words, key=lambda x: len(x))
    print(f"Words sorted by length: {sorted_by_length}")


def demonstrate_iterators():
    """Demonstrate custom iterators."""
    print("\n=== Custom Iterators Demo ===")
    
    # Count up iterator
    print("CountUp iterator (0 to 4):")
    for num in CountUp(5):
        print(f"  {num}")
    
    # Manual iteration
    print("\nManual iteration:")
    counter = CountUp(3)
    iterator = iter(counter)
    try:
        while True:
            value = next(iterator)
            print(f"  Next value: {value}")
    except StopIteration:
        print("  Iterator exhausted")


def demonstrate_advanced_classes():
    """Demonstrate advanced class features."""
    print("\n=== Advanced Classes Demo ===")
    
    # Singleton pattern
    print("Singleton pattern:")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"Same instance? {db1 is db2}")
    db1.connect()
    print(f"DB2 connected? {db2.connected}")
    
    # Property example
    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            return self._radius
        
        @radius.setter
        def radius(self, value):
            if value < 0:
                raise ValueError("Radius cannot be negative")
            self._radius = value
        
        @property
        def area(self):
            return 3.14159 * self._radius ** 2
        
        @property
        def circumference(self):
            return 2 * 3.14159 * self._radius
    
    circle = Circle(5)
    print(f"Circle radius: {circle.radius}")
    print(f"Circle area: {circle.area:.2f}")
    print(f"Circle circumference: {circle.circumference:.2f}")


def demonstrate_comprehensions():
    """Demonstrate advanced comprehension patterns."""
    print("\n=== Advanced Comprehensions Demo ===")
    
    # Nested list comprehension
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Matrix: {matrix}")
    print(f"Flattened: {flattened}")
    
    # Dictionary comprehension with condition
    numbers = range(1, 11)
    even_squares = {num: num**2 for num in numbers if num % 2 == 0}
    print(f"Even squares: {even_squares}")
    
    # Set comprehension
    words = ["hello", "world", "python", "programming"]
    lengths = {len(word) for word in words}
    print(f"Unique word lengths: {lengths}")
    
    # Conditional comprehension
    data = [1, -2, 3, -4, 5, -6]
    processed = [abs(x) if x < 0 else x**2 for x in data]
    print(f"Original: {data}")
    print(f"Processed: {processed}")


def demonstrate_async_simulation():
    """Simulate asynchronous programming concepts."""
    print("\n=== Async Concepts Simulation ===")
    
    # Simulate async-like behavior with generators
    def async_task(name, duration):
        print(f"Starting task: {name}")
        for i in range(duration):
            yield f"{name}: step {i+1}/{duration}"
        print(f"Completed task: {name}")
    
    # Simulate concurrent execution
    tasks = [
        async_task("Download", 3),
        async_task("Process", 2),
        async_task("Upload", 4)
    ]
    
    print("Simulating concurrent execution:")
    active_tasks = list(tasks)
    step = 0
    
    while active_tasks:
        step += 1
        print(f"\n--- Step {step} ---")
        
        completed_tasks = []
        for i, task in enumerate(active_tasks):
            try:
                result = next(task)
                print(f"  {result}")
            except StopIteration:
                completed_tasks.append(i)
        
        # Remove completed tasks (in reverse order to maintain indices)
        for i in reversed(completed_tasks):
            active_tasks.pop(i)


def run_all_advanced_examples():
    """Run all advanced examples."""
    print("🚀 ADVANCED PYTHON FEATURES DEMONSTRATION 🚀")
    print("=" * 60)
    
    demonstrate_decorators()
    demonstrate_generators()
    demonstrate_context_managers()
    demonstrate_lambda_functions()
    demonstrate_iterators()
    demonstrate_advanced_classes()
    demonstrate_comprehensions()
    demonstrate_async_simulation()
    
    print("\n" + "=" * 60)
    print("✅ All advanced examples completed!")


if __name__ == "__main__":
    run_all_advanced_examples()
