"""
Modern Python Features Showcase
Demonstrates dataclasses, type hints, pattern matching, and async/await
"""

from dataclasses import dataclass, field
from typing import List, Optional, Union, Protocol
from enum import Enum, auto
import asyncio


# Enum Example
class Status(Enum):
    """Status enumeration"""
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()


# Dataclass Example
@dataclass
class Person:
    """Person dataclass with automatic __init__, __repr__, etc."""
    name: str
    age: int
    email: str
    hobbies: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def add_hobby(self, hobby: str):
        self.hobbies.append(hobby)


@dataclass
class Task:
    """Task dataclass"""
    id: int
    title: str
    status: Status = Status.PENDING
    assignee: Optional[Person] = None
    
    def assign_to(self, person: Person):
        self.assignee = person
        self.status = Status.PROCESSING


# Protocol (Structural Subtyping)
class Drawable(Protocol):
    """Protocol for drawable objects"""
    def draw(self) -> str:
        ...


class Circle:
    """Circle class implementing Drawable protocol"""
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"


class Square:
    """Square class implementing Drawable protocol"""
    def __init__(self, side: float):
        self.side = side
    
    def draw(self) -> str:
        return f"Drawing square with side {self.side}"


def render(shape: Drawable) -> None:
    """Function accepting any Drawable protocol"""
    print(shape.draw())


# Pattern Matching (Python 3.10+)
def process_command(command: Union[str, tuple, list]) -> str:
    """Demonstrate pattern matching with match/case"""
    match command:
        case "start":
            return "Starting system..."
        case "stop":
            return "Stopping system..."
        case ["move", direction, distance]:
            return f"Moving {direction} by {distance} units"
        case {"action": "jump", "height": h}:
            return f"Jumping to height {h}"
        case _:
            return "Unknown command"


# Async/Await Example
async def fetch_data(id: int, delay: float) -> dict:
    """Simulate async data fetching"""
    print(f"Fetching data for ID {id}...")
    await asyncio.sleep(delay)
    return {"id": id, "data": f"Data for {id}", "delay": delay}


async def fetch_multiple_data(ids: List[int]) -> List[dict]:
    """Fetch multiple data items concurrently"""
    tasks = [fetch_data(id, 0.5) for id in ids]
    results = await asyncio.gather(*tasks)
    return results


# Walrus Operator Example
def process_numbers(numbers: List[int]) -> None:
    """Demonstrate walrus operator (:=)"""
    print("\nWalrus Operator Example:")
    
    # Without walrus operator
    squared = [x**2 for x in numbers]
    if len(squared) > 5:
        print(f"Many squares: {len(squared)} items")
    
    # With walrus operator
    if (n := len(numbers)) > 5:
        print(f"Processing {n} numbers")
    
    # In while loop
    data = numbers.copy()
    while (item := data.pop() if data else None) is not None:
        if item > 5:
            print(f"Found large number: {item}")
            break


# Type Hints with Union and Optional
def calculate(
    a: Union[int, float],
    b: Union[int, float],
    operation: str = "add"
) -> Optional[Union[int, float]]:
    """Calculate with type hints"""
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b if b != 0 else None
        case _:
            return None


def demonstrate_modern_features():
    """Main demonstration function"""
    print("=" * 50)
    print("Modern Python Features Showcase")
    print("=" * 50)
    
    # Dataclasses
    print("\n1. Dataclasses:")
    person = Person("Alice", 30, "alice@example.com")
    person.add_hobby("Reading")
    person.add_hobby("Coding")
    print(person)
    
    task = Task(1, "Implement feature X")
    task.assign_to(person)
    print(f"Task: {task.title}, Status: {task.status.name}")
    
    # Protocol
    print("\n2. Protocols (Structural Subtyping):")
    circle = Circle(5.0)
    square = Square(4.0)
    render(circle)
    render(square)
    
    # Pattern Matching
    print("\n3. Pattern Matching:")
    commands = [
        "start",
        ["move", "north", 10],
        {"action": "jump", "height": 5},
        "unknown"
    ]
    for cmd in commands:
        print(f"Command: {cmd} -> {process_command(cmd)}")
    
    # Type Hints
    print("\n4. Type Hints and Calculations:")
    print(f"10 + 5 = {calculate(10, 5, 'add')}")
    print(f"10 * 3.5 = {calculate(10, 3.5, 'multiply')}")
    print(f"10 / 0 = {calculate(10, 0, 'divide')}")
    
    # Walrus Operator
    print("\n5. Walrus Operator:")
    process_numbers([1, 3, 5, 7, 9, 11])
    
    # Async/Await
    print("\n6. Async/Await:")
    print("Fetching data asynchronously...")
    results = asyncio.run(fetch_multiple_data([1, 2, 3, 4, 5]))
    for result in results:
        print(f"  ID {result['id']}: {result['data']} (took {result['delay']}s)")


if __name__ == "__main__":
    demonstrate_modern_features()
