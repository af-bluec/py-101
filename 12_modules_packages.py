"""
Modules and Packages in Python
Demonstrates import systems, module creation, and package structure
"""

import sys
import os
import math
import random
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import json


def standard_library_imports():
    """Demonstrate standard library imports"""
    print("=" * 60)
    print("STANDARD LIBRARY IMPORTS")
    print("=" * 60)
    
    # Math module
    print(f"π = {math.pi:.4f}")
    print(f"e = {math.e:.4f}")
    print(f"sqrt(16) = {math.sqrt(16)}")
    print(f"sin(π/2) = {math.sin(math.pi/2):.4f}")
    
    # Random module
    print(f"\nRandom integer (1-10): {random.randint(1, 10)}")
    print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")
    print(f"Random float: {random.random():.4f}")
    
    # Datetime module
    now = datetime.now()
    print(f"\nCurrent time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    tomorrow = now + timedelta(days=1)
    print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
    
    print()


def different_import_styles():
    """Different ways to import modules"""
    print("=" * 60)
    print("IMPORT STYLES")
    print("=" * 60)
    
    # 1. Import entire module
    import statistics
    data = [1, 2, 3, 4, 5]
    print(f"Mean: {statistics.mean(data)}")
    
    # 2. Import specific items
    from statistics import median, stdev
    print(f"Median: {median(data)}")
    print(f"Std Dev: {stdev(data):.2f}")
    
    # 3. Import with alias
    import statistics as stats
    print(f"Mode: {stats.mode([1, 1, 2, 3, 3, 3])}")
    
    # 4. Import all (not recommended)
    # from statistics import *  # Avoid this in production code
    
    print()


def sys_module_info():
    """System information using sys module"""
    print("=" * 60)
    print("SYS MODULE - SYSTEM INFORMATION")
    print("=" * 60)
    
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Executable: {sys.executable}")
    print(f"\nModule search paths (first 3):")
    for path in sys.path[:3]:
        print(f"  {path}")
    
    # Command line arguments
    print(f"\nScript name: {sys.argv[0]}")
    print(f"Arguments count: {len(sys.argv)}")
    
    print()


def os_module_operations():
    """Operating system operations"""
    print("=" * 60)
    print("OS MODULE - FILE SYSTEM OPERATIONS")
    print("=" * 60)
    
    # Current directory
    print(f"Current directory: {os.getcwd()}")
    
    # Environment variables
    print(f"Home directory: {os.environ.get('HOME', 'N/A')}")
    print(f"User: {os.environ.get('USER', 'N/A')}")
    
    # Path operations
    path = "/home/user/documents/file.txt"
    print(f"\nPath: {path}")
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")
    print(f"Extension: {os.path.splitext(path)[1]}")
    
    # Join paths
    joined = os.path.join("folder", "subfolder", "file.txt")
    print(f"Joined path: {joined}")
    
    print()


def pathlib_modern_paths():
    """Modern path handling with pathlib"""
    print("=" * 60)
    print("PATHLIB - MODERN PATH HANDLING")
    print("=" * 60)
    
    # Create Path objects
    current = Path.cwd()
    print(f"Current directory: {current}")
    
    # Path operations
    file_path = Path("/home/user/documents/report.pdf")
    print(f"\nPath: {file_path}")
    print(f"Name: {file_path.name}")
    print(f"Stem: {file_path.stem}")
    print(f"Suffix: {file_path.suffix}")
    print(f"Parent: {file_path.parent}")
    
    # Path joining (more elegant than os.path.join)
    new_path = Path("data") / "files" / "output.txt"
    print(f"Joined path: {new_path}")
    
    # Check existence (would work with real files)
    print(f"Exists: {file_path.exists()}")
    print(f"Is file: {file_path.is_file()}")
    print(f"Is directory: {file_path.is_dir()}")
    
    print()


def collections_module():
    """Collections module - specialized data structures"""
    print("=" * 60)
    print("COLLECTIONS MODULE")
    print("=" * 60)
    
    # Counter - count occurrences
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counter = Counter(words)
    print(f"Word counts: {counter}")
    print(f"Most common: {counter.most_common(2)}")
    
    # defaultdict - default values for missing keys
    word_lengths = defaultdict(list)
    for word in words:
        word_lengths[len(word)].append(word)
    print(f"\nWords by length: {dict(word_lengths)}")
    
    # deque - double-ended queue
    from collections import deque
    queue = deque([1, 2, 3])
    queue.append(4)  # Add to right
    queue.appendleft(0)  # Add to left
    print(f"\nDeque: {queue}")
    print(f"Pop right: {queue.pop()}")
    print(f"Pop left: {queue.popleft()}")
    
    # namedtuple - tuple with named fields
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"\nPoint: {p}")
    print(f"X coordinate: {p.x}")
    print(f"Y coordinate: {p.y}")
    
    print()


def itertools_module():
    """Itertools - iterator building blocks"""
    print("=" * 60)
    print("ITERTOOLS MODULE")
    print("=" * 60)
    
    import itertools
    
    # count - infinite counter
    counter = itertools.count(start=10, step=2)
    print(f"First 5 from counter: {[next(counter) for _ in range(5)]}")
    
    # cycle - infinite cycle through iterable
    colors = itertools.cycle(['red', 'green', 'blue'])
    print(f"First 7 from cycle: {[next(colors) for _ in range(7)]}")
    
    # chain - combine iterables
    combined = list(itertools.chain([1, 2], [3, 4], [5, 6]))
    print(f"Chained: {combined}")
    
    # combinations and permutations
    items = ['A', 'B', 'C']
    combos = list(itertools.combinations(items, 2))
    print(f"Combinations (2): {combos}")
    
    perms = list(itertools.permutations(items, 2))
    print(f"Permutations (2): {perms}")
    
    # groupby - group consecutive items
    data = [1, 1, 2, 2, 2, 3, 1, 1]
    groups = [(k, list(g)) for k, g in itertools.groupby(data)]
    print(f"Grouped: {groups}")
    
    print()


def functools_module():
    """Functools - higher-order functions"""
    print("=" * 60)
    print("FUNCTOOLS MODULE")
    print("=" * 60)
    
    from functools import reduce, partial, lru_cache, wraps
    
    # reduce - apply function cumulatively
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of {numbers}: {product}")
    
    # partial - partial function application
    def power(base, exponent):
        return base ** exponent
    
    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    print(f"\n5 squared: {square(5)}")
    print(f"5 cubed: {cube(5)}")
    
    # lru_cache - memoization
    @lru_cache(maxsize=128)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"\nFibonacci(10): {fibonacci(10)}")
    print(f"Cache info: {fibonacci.cache_info()}")
    
    print()


def json_module():
    """JSON module - working with JSON data"""
    print("=" * 60)
    print("JSON MODULE")
    print("=" * 60)
    
    # Python object to JSON
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "coding", "gaming"],
        "is_active": True
    }
    
    json_string = json.dumps(data, indent=2)
    print("Python to JSON:")
    print(json_string)
    
    # JSON to Python object
    parsed = json.loads(json_string)
    print(f"\nParsed name: {parsed['name']}")
    print(f"Parsed hobbies: {parsed['hobbies']}")
    
    # Compact JSON
    compact = json.dumps(data)
    print(f"\nCompact JSON: {compact[:50]}...")
    
    print()


def module_attributes():
    """Module attributes and introspection"""
    print("=" * 60)
    print("MODULE ATTRIBUTES")
    print("=" * 60)
    
    # Module name
    print(f"Module name: {__name__}")
    
    # Module docstring
    print(f"Module doc: {__doc__[:50]}...")
    
    # Module file
    print(f"Module file: {__file__}")
    
    # List module contents
    import string
    print(f"\nString module contents (first 10):")
    contents = [item for item in dir(string) if not item.startswith('_')]
    for item in contents[:10]:
        print(f"  {item}")
    
    # Check if attribute exists
    print(f"\nHas 'ascii_letters': {hasattr(string, 'ascii_letters')}")
    print(f"ascii_letters: {string.ascii_letters}")
    
    print()


def creating_modules_example():
    """Example of how to create and structure modules"""
    print("=" * 60)
    print("CREATING MODULES - EXAMPLE STRUCTURE")
    print("=" * 60)
    
    example_module = '''
# my_module.py
"""
My custom module
Provides utility functions for data processing
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# Module-level constant
DEFAULT_TIMEOUT = 30

# Private function (by convention)
def _internal_helper():
    """This is a private function"""
    pass

# Public function
def process_data(data):
    """Process the input data"""
    return [x * 2 for x in data]

# Public class
class DataProcessor:
    """A class for processing data"""
    
    def __init__(self, name):
        self.name = name
    
    def process(self, data):
        return process_data(data)

# Module initialization code
if __name__ == "__main__":
    # This runs only when module is executed directly
    print("Running module tests...")
    test_data = [1, 2, 3]
    print(f"Result: {process_data(test_data)}")
'''
    
    print("Example module structure:")
    print(example_module)
    
    print("\nPackage structure example:")
    print("""
mypackage/
├── __init__.py          # Makes it a package
├── module1.py           # Submodule 1
├── module2.py           # Submodule 2
└── subpackage/
    ├── __init__.py
    └── module3.py
    
# Usage:
from mypackage import module1
from mypackage.subpackage import module3
""")
    
    print()


def import_best_practices():
    """Best practices for imports"""
    print("=" * 60)
    print("IMPORT BEST PRACTICES")
    print("=" * 60)
    
    best_practices = """
1. Import Order (PEP 8):
   - Standard library imports
   - Related third-party imports
   - Local application imports
   - Separate each group with a blank line

2. Avoid wildcard imports:
   ❌ from module import *
   ✅ from module import specific_function

3. Use absolute imports:
   ✅ from mypackage.submodule import function
   
4. Avoid circular imports:
   - Restructure code
   - Use local imports if necessary
   
5. Import at module level:
   - Not inside functions (unless necessary)
   
6. Use aliases for long names:
   import numpy as np
   import pandas as pd
   
7. One import per line:
   ✅ import os
   ✅ import sys
   ❌ import os, sys
   
8. Group related imports:
   from collections import Counter, defaultdict, deque
"""
    
    print(best_practices)
    print()


def main():
    """Run all module demonstrations"""
    print("\n" + "=" * 60)
    print("PYTHON MODULES AND PACKAGES SHOWCASE")
    print("=" * 60 + "\n")
    
    standard_library_imports()
    different_import_styles()
    sys_module_info()
    os_module_operations()
    pathlib_modern_paths()
    collections_module()
    itertools_module()
    functools_module()
    json_module()
    module_attributes()
    creating_modules_example()
    import_best_practices()
    
    print("=" * 60)
    print("Modules and packages demonstration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
