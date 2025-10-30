"""
Demonstration of Python's built-in data structures.
Covers lists, tuples, sets, and dictionaries with common operations.
"""

def demonstrate_lists():
    """Lists are mutable, ordered collections."""
    print("=== LISTS ===")
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")
    
    # Adding elements
    fruits.append("date")
    fruits.insert(1, "blueberry")
    print(f"After additions: {fruits}")
    
    # Removing elements
    fruits.remove("banana")
    popped = fruits.pop()
    print(f"After removals: {fruits}, popped: {popped}")
    
    # Slicing
    print(f"First two: {fruits[:2]}")
    print(f"Last two: {fruits[-2:]}")
    
    # List comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")
    
    # Filtering with comprehension
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers: {evens}\n")


def demonstrate_tuples():
    """Tuples are immutable, ordered collections."""
    print("=== TUPLES ===")
    coordinates = (10, 20, 30)
    print(f"Tuple: {coordinates}")
    
    # Unpacking
    x, y, z = coordinates
    print(f"Unpacked: x={x}, y={y}, z={z}")
    
    # Named tuples (using regular tuple)
    person = ("Alice", 30, "Engineer")
    name, age, job = person
    print(f"Person: {name}, {age}, {job}")
    
    # Tuple as dictionary key (immutable)
    locations = {(0, 0): "origin", (1, 1): "diagonal"}
    print(f"Locations: {locations}\n")


def demonstrate_sets():
    """Sets are unordered collections of unique elements."""
    print("=== SETS ===")
    numbers = {1, 2, 3, 4, 5}
    print(f"Set: {numbers}")
    
    # Adding duplicates has no effect
    numbers.add(3)
    numbers.add(6)
    print(f"After adding 3 and 6: {numbers}")
    
    # Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")
    print(f"Symmetric difference: {set1 ^ set2}\n")


def demonstrate_dictionaries():
    """Dictionaries are key-value mappings."""
    print("=== DICTIONARIES ===")
    student = {
        "name": "Bob",
        "age": 20,
        "grades": [85, 90, 92]
    }
    print(f"Student: {student}")
    
    # Accessing values
    print(f"Name: {student['name']}")
    print(f"Age: {student.get('age', 'Unknown')}")
    
    # Adding/updating
    student["major"] = "Computer Science"
    student["age"] = 21
    print(f"Updated: {student}")
    
    # Dictionary methods
    print(f"Keys: {list(student.keys())}")
    print(f"Values: {list(student.values())}")
    print(f"Items: {list(student.items())}")
    
    # Dictionary comprehension
    squared_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squared dict: {squared_dict}\n")


if __name__ == "__main__":
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_sets()
    demonstrate_dictionaries()
