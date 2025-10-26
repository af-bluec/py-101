"""
Python Collections Module Demonstration

This module showcases the collections module features:
- Named tuples for structured data
- Counter for counting hashable objects
- defaultdict for dictionaries with default values
- deque for efficient double-ended operations
- OrderedDict for insertion-order preservation
- ChainMap for combining dictionaries
- UserDict, UserList, UserString for subclassing

The collections module provides specialized container datatypes
that are alternatives to Python's general purpose built-in containers.
"""

from collections import (
    namedtuple, Counter, defaultdict, deque, OrderedDict, 
    ChainMap, UserDict, UserList, UserString
)
from typing import Any, List, Dict
import json


# Named tuple examples
Person = namedtuple('Person', ['name', 'age', 'city'])
Point3D = namedtuple('Point3D', ['x', 'y', 'z'], defaults=[0, 0, 0])

# Named tuple with methods
class Employee(namedtuple('Employee', ['name', 'position', 'salary'])):
    """Extended named tuple with custom methods."""
    
    def annual_bonus(self, percentage: float = 0.1) -> float:
        """Calculate annual bonus."""
        return self.salary * percentage
    
    def promote(self, new_position: str, salary_increase: float = 0.15):
        """Return a new Employee instance with promotion."""
        new_salary = self.salary * (1 + salary_increase)
        return self._replace(position=new_position, salary=new_salary)


class CaseInsensitiveDict(UserDict):
    """
    A dictionary that treats keys as case-insensitive.
    
    Example of extending UserDict for custom behavior.
    """
    
    def __setitem__(self, key, value):
        if isinstance(key, str):
            key = key.lower()
        super().__setitem__(key, value)
    
    def __getitem__(self, key):
        if isinstance(key, str):
            key = key.lower()
        return super().__getitem__(key)
    
    def __contains__(self, key):
        if isinstance(key, str):
            key = key.lower()
        return super().__contains__(key)
    
    def get(self, key, default=None):
        if isinstance(key, str):
            key = key.lower()
        return super().get(key, default)


class UniqueList(UserList):
    """
    A list that only allows unique elements.
    
    Example of extending UserList for custom behavior.
    """
    
    def __init__(self, initlist=None):
        super().__init__()
        if initlist:
            for item in initlist:
                self.append(item)
    
    def append(self, item):
        """Add item only if it's not already in the list."""
        if item not in self.data:
            super().append(item)
    
    def extend(self, other):
        """Extend with unique items only."""
        for item in other:
            self.append(item)
    
    def insert(self, index, item):
        """Insert item only if it's not already in the list."""
        if item not in self.data:
            super().insert(index, item)


class RichString(UserString):
    """
    An enhanced string class with additional methods.
    
    Example of extending UserString for custom behavior.
    """
    
    def word_count(self) -> int:
        """Count the number of words."""
        return len(self.data.split())
    
    def char_frequency(self) -> Counter:
        """Return character frequency counter."""
        return Counter(self.data.lower())
    
    def reverse_words(self):
        """Return a new RichString with words reversed."""
        words = self.data.split()
        return RichString(' '.join(reversed(words)))
    
    def title_case(self):
        """Return title case version."""
        return RichString(self.data.title())


def demonstrate_namedtuple():
    """Demonstrate namedtuple usage."""
    print("=== Named Tuple Demo ===")
    
    # Basic named tuple
    person1 = Person("Alice", 30, "New York")
    person2 = Person("Bob", 25, "San Francisco")
    
    print(f"Person 1: {person1}")
    print(f"Name: {person1.name}, Age: {person1.age}, City: {person1.city}")
    
    # Named tuple with defaults
    origin = Point3D()  # Uses defaults
    point = Point3D(10, 20, 30)
    
    print(f"Origin: {origin}")
    print(f"Point: {point}")
    
    # Named tuple with methods
    employee = Employee("John Doe", "Developer", 75000)
    print(f"Employee: {employee}")
    print(f"Annual bonus: ${employee.annual_bonus():.2f}")
    
    # Immutable replacement
    promoted = employee.promote("Senior Developer", 0.20)
    print(f"After promotion: {promoted}")
    
    # Named tuple features
    print(f"\nNamedtuple features:")
    print(f"Fields: {employee._fields}")
    print(f"As dict: {employee._asdict()}")
    
    # Create from iterable
    data = ["Jane Smith", "Manager", 90000]
    manager = Employee._make(data)
    print(f"Created from list: {manager}")


def demonstrate_counter():
    """Demonstrate Counter usage."""
    print("\n=== Counter Demo ===")
    
    # Count characters
    text = "hello world"
    char_count = Counter(text)
    print(f"Character count in '{text}': {char_count}")
    
    # Count words
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    word_count = Counter(words)
    print(f"Word count: {word_count}")
    
    # Most common elements
    print(f"Most common 2: {word_count.most_common(2)}")
    
    # Counter arithmetic
    counter1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    counter2 = Counter(['a', 'b', 'b', 'd', 'd', 'd'])
    
    print(f"Counter 1: {counter1}")
    print(f"Counter 2: {counter2}")
    print(f"Addition: {counter1 + counter2}")
    print(f"Subtraction: {counter1 - counter2}")
    print(f"Intersection: {counter1 & counter2}")
    print(f"Union: {counter1 | counter2}")
    
    # Update counter
    counter1.update(['e', 'e', 'f'])
    print(f"After update: {counter1}")


def demonstrate_defaultdict():
    """Demonstrate defaultdict usage."""
    print("\n=== DefaultDict Demo ===")
    
    # Group items by key
    data = [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana'), 
            ('vegetable', 'broccoli'), ('fruit', 'orange')]
    
    grouped = defaultdict(list)
    for category, item in data:
        grouped[category].append(item)
    
    print("Grouped items:")
    for category, items in grouped.items():
        print(f"  {category}: {items}")
    
    # Count nested items
    nested_counter = defaultdict(lambda: defaultdict(int))
    
    transactions = [
        ('2023', 'January', 100),
        ('2023', 'February', 150),
        ('2023', 'January', 200),
        ('2024', 'January', 175),
    ]
    
    for year, month, amount in transactions:
        nested_counter[year][month] += amount
    
    print("\nTransaction totals:")
    for year, months in nested_counter.items():
        print(f"  {year}:")
        for month, total in months.items():
            print(f"    {month}: ${total}")


def demonstrate_deque():
    """Demonstrate deque usage."""
    print("\n=== Deque Demo ===")
    
    # Create deque
    dq = deque(['a', 'b', 'c'])
    print(f"Initial deque: {dq}")
    
    # Add to both ends
    dq.appendleft('LEFT')
    dq.append('RIGHT')
    print(f"After adding to both ends: {dq}")
    
    # Remove from both ends
    left = dq.popleft()
    right = dq.pop()
    print(f"Removed '{left}' from left, '{right}' from right: {dq}")
    
    # Rotation
    dq.extend([1, 2, 3])
    print(f"Extended deque: {dq}")
    
    dq.rotate(2)  # Rotate right
    print(f"Rotated right by 2: {dq}")
    
    dq.rotate(-3)  # Rotate left
    print(f"Rotated left by 3: {dq}")
    
    # Limited size deque (useful for recent items)
    recent_items = deque(maxlen=3)
    for i in range(10):
        recent_items.append(f"item_{i}")
        print(f"Added item_{i}, recent items: {list(recent_items)}")


def demonstrate_ordereddict():
    """Demonstrate OrderedDict usage."""
    print("\n=== OrderedDict Demo ===")
    
    # Create ordered dictionary
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3
    
    print(f"OrderedDict: {od}")
    print(f"Keys in order: {list(od.keys())}")
    
    # Move to end
    od.move_to_end('first')
    print(f"After moving 'first' to end: {list(od.keys())}")
    
    # Move to beginning
    od.move_to_end('third', last=False)
    print(f"After moving 'third' to beginning: {list(od.keys())}")
    
    # Pop last item
    last_item = od.popitem(last=True)
    print(f"Popped last item: {last_item}, remaining: {od}")
    
    # Pop first item
    first_item = od.popitem(last=False)
    print(f"Popped first item: {first_item}, remaining: {od}")


def demonstrate_chainmap():
    """Demonstrate ChainMap usage."""
    print("\n=== ChainMap Demo ===")
    
    # Create multiple dictionaries
    defaults = {'color': 'red', 'user': 'guest'}
    environment = {'user': 'admin'}
    command_line = {'color': 'blue'}
    
    # Chain them together (command_line overrides environment overrides defaults)
    combined = ChainMap(command_line, environment, defaults)
    
    print(f"Defaults: {defaults}")
    print(f"Environment: {environment}")
    print(f"Command line: {command_line}")
    print(f"Combined: {dict(combined)}")
    print(f"Color: {combined['color']}")  # From command_line
    print(f"User: {combined['user']}")    # From environment
    
    # Show all maps
    print(f"All maps: {combined.maps}")
    
    # Add new map
    runtime = {'debug': True}
    combined = combined.new_child(runtime)
    print(f"After adding runtime config: {dict(combined)}")
    
    # Modify through ChainMap
    combined['temp_setting'] = 'temporary'
    print(f"After setting temp_setting: {dict(combined)}")
    print(f"Runtime map now: {runtime}")  # temp_setting was added here


def demonstrate_custom_collections():
    """Demonstrate custom collection classes."""
    print("\n=== Custom Collections Demo ===")
    
    # Case-insensitive dictionary
    ci_dict = CaseInsensitiveDict()
    ci_dict['Name'] = 'John'
    ci_dict['EMAIL'] = 'john@example.com'
    
    print(f"Case-insensitive dict: {ci_dict}")
    print(f"Access 'name': {ci_dict['name']}")      # lowercase
    print(f"Access 'Email': {ci_dict['Email']}")    # mixed case
    print(f"'NAME' in dict: {'NAME' in ci_dict}")   # uppercase
    
    # Unique list
    unique_list = UniqueList([1, 2, 3, 2, 4, 1, 5])
    print(f"\nUnique list: {unique_list}")
    
    unique_list.append(6)
    unique_list.append(3)  # Won't be added (duplicate)
    print(f"After appending 6 and 3: {unique_list}")
    
    unique_list.extend([7, 8, 5, 9])
    print(f"After extending: {unique_list}")
    
    # Rich string
    text = RichString("Hello World Python Programming")
    print(f"\nRich string: {text}")
    print(f"Word count: {text.word_count()}")
    print(f"Character frequency: {text.char_frequency().most_common(3)}")
    print(f"Reversed words: {text.reverse_words()}")
    print(f"Title case: {text.title_case()}")


if __name__ == "__main__":
    print("=== Python Collections Module Demo ===")
    
    demonstrate_namedtuple()
    demonstrate_counter()
    demonstrate_defaultdict()
    demonstrate_deque()
    demonstrate_ordereddict()
    demonstrate_chainmap()
    demonstrate_custom_collections()
    
    print("\n=== Collections Demo Complete ===")
