"""
Demonstration of Python comprehensions.
Covers list, dict, set comprehensions and generator expressions.
"""


def list_comprehensions():
    """Demonstrate list comprehensions."""
    print("=== LIST COMPREHENSIONS ===")
    
    # Basic list comprehension
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")
    
    # With condition
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers: {evens}")
    
    # With if-else
    labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
    print(f"Labels: {labels}")
    
    # Nested comprehension
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Multiplication table:\n{matrix}")
    
    # Flattening a matrix
    flat = [num for row in matrix for num in row]
    print(f"Flattened: {flat}")
    
    # String manipulation
    words = ["hello", "world", "python"]
    uppercase = [word.upper() for word in words]
    print(f"Uppercase: {uppercase}")
    
    # Filtering with multiple conditions
    numbers = range(1, 51)
    filtered = [x for x in numbers if x % 3 == 0 and x % 5 == 0]
    print(f"Divisible by 3 and 5: {filtered}")


def dict_comprehensions():
    """Demonstrate dictionary comprehensions."""
    print("\n=== DICTIONARY COMPREHENSIONS ===")
    
    # Basic dict comprehension
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squares dict: {squares_dict}")
    
    # From two lists
    keys = ["name", "age", "city"]
    values = ["Alice", 30, "NYC"]
    person = {k: v for k, v in zip(keys, values)}
    print(f"Person: {person}")
    
    # With condition
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    print(f"Even squares: {even_squares}")
    
    # Swapping keys and values
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(f"Original: {original}")
    print(f"Swapped: {swapped}")
    
    # Filtering dictionary
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
    high_scores = {name: score for name, score in scores.items() if score >= 90}
    print(f"High scores (>=90): {high_scores}")
    
    # Nested dict comprehension
    multiplication_table = {
        i: {j: i * j for j in range(1, 6)}
        for i in range(1, 6)
    }
    print(f"Multiplication table: {multiplication_table}")


def set_comprehensions():
    """Demonstrate set comprehensions."""
    print("\n=== SET COMPREHENSIONS ===")
    
    # Basic set comprehension
    squares_set = {x**2 for x in range(-5, 6)}
    print(f"Squares set: {squares_set}")
    
    # Removing duplicates
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = {x for x in numbers}
    print(f"Unique numbers: {unique}")
    
    # With condition
    vowels = {char.lower() for char in "Hello World" if char.lower() in "aeiou"}
    print(f"Vowels: {vowels}")
    
    # Set operations with comprehensions
    set1 = {x for x in range(10) if x % 2 == 0}
    set2 = {x for x in range(10) if x % 3 == 0}
    print(f"Even numbers: {set1}")
    print(f"Divisible by 3: {set2}")
    print(f"Intersection: {set1 & set2}")


def generator_expressions():
    """Demonstrate generator expressions."""
    print("\n=== GENERATOR EXPRESSIONS ===")
    
    # Basic generator
    squares_gen = (x**2 for x in range(10))
    print(f"Generator object: {squares_gen}")
    print(f"First 5 squares: {[next(squares_gen) for _ in range(5)]}")
    
    # Memory efficient for large datasets
    sum_of_squares = sum(x**2 for x in range(1000000))
    print(f"Sum of first million squares: {sum_of_squares}")
    
    # Generator with condition
    even_gen = (x for x in range(20) if x % 2 == 0)
    print(f"Even numbers: {list(even_gen)}")
    
    # Using in functions
    max_square = max(x**2 for x in range(10))
    print(f"Max square: {max_square}")
    
    # Chaining generators
    numbers = range(100)
    filtered = (x for x in numbers if x % 2 == 0)
    squared = (x**2 for x in filtered)
    result = list(squared)[:5]
    print(f"First 5 even squares: {result}")


def practical_examples():
    """Practical examples of comprehensions."""
    print("\n=== PRACTICAL EXAMPLES ===")
    
    # Parse CSV-like data
    data = "name:Alice,age:30,city:NYC"
    parsed = {item.split(":")[0]: item.split(":")[1] for item in data.split(",")}
    print(f"Parsed data: {parsed}")
    
    # Count word lengths
    sentence = "Python comprehensions are powerful and concise"
    word_lengths = {word: len(word) for word in sentence.split()}
    print(f"Word lengths: {word_lengths}")
    
    # Filter and transform
    prices = {"apple": 0.5, "banana": 0.3, "cherry": 0.8, "date": 1.2}
    expensive = {fruit: price * 1.1 for fruit, price in prices.items() if price > 0.5}
    print(f"Expensive items (+10%): {expensive}")
    
    # Nested data processing
    students = [
        {"name": "Alice", "grades": [85, 90, 92]},
        {"name": "Bob", "grades": [78, 82, 88]},
        {"name": "Charlie", "grades": [95, 93, 97]}
    ]
    averages = {
        student["name"]: sum(student["grades"]) / len(student["grades"])
        for student in students
    }
    print(f"Student averages: {averages}")
    
    # Matrix transpose
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"Original matrix: {matrix}")
    print(f"Transposed: {transposed}")


def performance_comparison():
    """Compare comprehensions vs traditional loops."""
    print("\n=== PERFORMANCE NOTES ===")
    print("Comprehensions are generally faster than equivalent loops")
    print("Generator expressions are memory-efficient for large datasets")
    print("Use comprehensions for readability when appropriate")
    
    import time
    
    # Traditional loop
    start = time.time()
    result = []
    for x in range(100000):
        result.append(x**2)
    loop_time = time.time() - start
    
    # List comprehension
    start = time.time()
    result = [x**2 for x in range(100000)]
    comp_time = time.time() - start
    
    print(f"\nLoop time: {loop_time:.4f}s")
    print(f"Comprehension time: {comp_time:.4f}s")
    print(f"Speedup: {loop_time/comp_time:.2f}x")


def main():
    list_comprehensions()
    dict_comprehensions()
    set_comprehensions()
    generator_expressions()
    practical_examples()
    performance_comparison()


if __name__ == "__main__":
    main()
