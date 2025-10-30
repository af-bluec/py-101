"""
Demonstration of advanced Python features.
Covers metaclasses, descriptors, type hints, dataclasses, and more.
"""

from typing import List, Dict, Optional, Union, Callable, TypeVar, Generic
from dataclasses import dataclass, field, asdict
from functools import wraps, lru_cache, partial
from collections import namedtuple, defaultdict, Counter, deque
from enum import Enum, auto
import operator


# Type hints and annotations
def greet(name: str, times: int = 1) -> str:
    """Function with type hints."""
    return (name + "! ") * times


def process_items(items: List[int]) -> Dict[str, int]:
    """Process list and return statistics."""
    return {
        "count": len(items),
        "sum": sum(items),
        "max": max(items) if items else 0
    }


# Generic types
T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation."""
    
    def __init__(self):
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None


# Dataclasses
@dataclass
class Person:
    """Person dataclass with automatic methods."""
    name: str
    age: int
    email: str = ""
    hobbies: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


@dataclass(frozen=True)
class Point:
    """Immutable dataclass."""
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


# Enums
class Color(Enum):
    """Color enumeration."""
    RED = 1
    GREEN = 2
    BLUE = 3


class Status(Enum):
    """Status with auto values."""
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()


# Named tuples
Point2D = namedtuple('Point2D', ['x', 'y'])
Person_NT = namedtuple('Person', ['name', 'age', 'city'])


# Descriptors
class ValidatedAttribute:
    """Descriptor for validated attributes."""
    
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        obj.__dict__[self.name] = value


class Person_Validated:
    """Class using descriptors."""
    age = ValidatedAttribute('age', lambda x: isinstance(x, int) and x >= 0)
    name = ValidatedAttribute('name', lambda x: isinstance(x, str) and len(x) > 0)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Property with getter, setter, deleter
class Temperature:
    """Class demonstrating property decorators."""
    
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self):
        print("Deleting celsius")
        del self._celsius


# Metaclass
class SingletonMeta(type):
    """Metaclass for singleton pattern."""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Singleton database class."""
    
    def __init__(self):
        self.connection = "Connected"


# Advanced decorators
def retry(times: int):
    """Decorator with arguments."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
        return wrapper
    return decorator


def memoize(func):
    """Simple memoization decorator."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


# Using functools
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """Fibonacci with LRU cache."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Collections demonstrations
def demonstrate_collections():
    """Show advanced collection types."""
    print("=== COLLECTIONS ===")
    
    # defaultdict
    word_count = defaultdict(int)
    for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
        word_count[word] += 1
    print(f"Word count: {dict(word_count)}")
    
    # Counter
    counter = Counter(["a", "b", "a", "c", "b", "a"])
    print(f"Counter: {counter}")
    print(f"Most common: {counter.most_common(2)}")
    
    # deque (double-ended queue)
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(f"Deque: {list(dq)}")
    dq.rotate(2)
    print(f"After rotate(2): {list(dq)}")


# Operator module
def demonstrate_operators():
    """Show operator module usage."""
    print("\n=== OPERATOR MODULE ===")
    
    numbers = [5, 2, 8, 1, 9]
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Product: {eval('*'.join(map(str, numbers)))}")
    
    # Using operator functions
    from functools import reduce
    product = reduce(operator.mul, numbers)
    print(f"Product (operator): {product}")
    
    # Sorting with operator
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sorted_by_age = sorted(people, key=operator.itemgetter(1))
    print(f"Sorted by age: {sorted_by_age}")


# Partial functions
def demonstrate_partial():
    """Show partial function application."""
    print("\n=== PARTIAL FUNCTIONS ===")
    
    def power(base, exponent):
        return base ** exponent
    
    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    
    print(f"Square of 5: {square(5)}")
    print(f"Cube of 5: {cube(5)}")


# Slots for memory optimization
class Point_Slots:
    """Class using __slots__ for memory efficiency."""
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    print("=== TYPE HINTS ===")
    result = greet("Alice", 3)
    print(result)
    
    stats = process_items([1, 2, 3, 4, 5])
    print(f"Stats: {stats}")
    
    print("\n=== GENERIC TYPES ===")
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Popped: {stack.pop()}")
    
    print("\n=== DATACLASSES ===")
    person = Person("Bob", 25, "bob@example.com", ["reading", "coding"])
    print(person)
    print(f"As dict: {asdict(person)}")
    
    point = Point(3.0, 4.0)
    print(f"Point: {point}, Distance: {point.distance_from_origin():.2f}")
    
    print("\n=== ENUMS ===")
    color = Color.RED
    print(f"Color: {color}, Value: {color.value}")
    
    status = Status.PROCESSING
    print(f"Status: {status.name}")
    
    print("\n=== NAMED TUPLES ===")
    p = Point2D(10, 20)
    print(f"Point: {p}, x={p.x}, y={p.y}")
    
    person_nt = Person_NT("Alice", 30, "NYC")
    print(f"Person: {person_nt}")
    
    print("\n=== DESCRIPTORS ===")
    try:
        validated = Person_Validated("Charlie", 25)
        print(f"Valid person: {validated.name}, {validated.age}")
        validated.age = -5  # This will raise an error
    except ValueError as e:
        print(f"Validation error: {e}")
    
    print("\n=== PROPERTIES ===")
    temp = Temperature()
    temp.celsius = 25
    print(f"Temperature: {temp.celsius}°C")
    
    print("\n=== METACLASSES (Singleton) ===")
    db1 = Database()
    db2 = Database()
    print(f"Same instance? {db1 is db2}")
    
    print("\n=== DECORATORS ===")
    
    @retry(times=3)
    def unreliable_function():
        import random
        if random.random() < 0.7:
            raise Exception("Random failure")
        return "Success"
    
    @memoize
    def slow_function(n):
        return n ** 2
    
    print(f"Fibonacci(10): {fibonacci(10)}")
    
    demonstrate_collections()
    demonstrate_operators()
    demonstrate_partial()
    
    print("\n=== SLOTS ===")
    p1 = Point_Slots(1, 2)
    print(f"Point with slots: ({p1.x}, {p1.y})")
    
    print("\n=== SUMMARY ===")
    print("Advanced features make Python powerful and expressive")
    print("Type hints improve code clarity and enable better tooling")
    print("Dataclasses reduce boilerplate code")
    print("Descriptors and properties enable controlled attribute access")
    print("Metaclasses allow customization of class creation")


if __name__ == "__main__":
    main()
