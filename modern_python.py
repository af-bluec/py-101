"""
Modern Python Features Showcase
Demonstrates dataclasses, type hints, async/await, and more
"""

from dataclasses import dataclass, field, asdict
from typing import Optional, Union, List, Dict, Any
from enum import Enum, auto
import asyncio
from collections import defaultdict, Counter, namedtuple
import json


# Enums
class Status(Enum):
    """Status enumeration"""
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()


# Dataclasses
@dataclass
class Person:
    """Person dataclass with type hints"""
    name: str
    age: int
    email: str
    hobbies: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(asdict(self), indent=2)
    
    def is_adult(self) -> bool:
        """Check if person is an adult"""
        return self.age >= 18


@dataclass
class Task:
    """Task dataclass with default values"""
    title: str
    description: str = ""
    status: Status = Status.PENDING
    priority: int = 1
    tags: List[str] = field(default_factory=list)
    
    def mark_completed(self):
        """Mark task as completed"""
        self.status = Status.COMPLETED
    
    def __str__(self) -> str:
        return f"Task({self.title}, {self.status.name}, priority={self.priority})"


# Type Hints and Union Types
def process_data(data: Union[str, int, List[int]]) -> Optional[int]:
    """Process different types of data"""
    if isinstance(data, str):
        return len(data)
    elif isinstance(data, int):
        return data * 2
    elif isinstance(data, list):
        return sum(data)
    return None


# Async/Await
async def fetch_data(url: str, delay: float = 1.0) -> Dict[str, Any]:
    """Simulate async data fetching"""
    print(f"🌐 Fetching data from {url}...")
    await asyncio.sleep(delay)
    return {
        'url': url,
        'status': 200,
        'data': f'Content from {url}'
    }


async def fetch_multiple(urls: List[str]) -> List[Dict[str, Any]]:
    """Fetch multiple URLs concurrently"""
    tasks = [fetch_data(url, 0.5) for url in urls]
    results = await asyncio.gather(*tasks)
    return results


async def async_generator(n: int):
    """Async generator example"""
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i ** 2


# Collections
def collections_demo():
    """Demonstrate various collection types"""
    print("\n📦 COLLECTIONS DEMO")
    print("-" * 60)
    
    # defaultdict
    word_count = defaultdict(int)
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    for word in words:
        word_count[word] += 1
    print(f"Word count (defaultdict): {dict(word_count)}")
    
    # Counter
    counter = Counter(words)
    print(f"Most common: {counter.most_common(2)}")
    
    # namedtuple
    Point = namedtuple('Point', ['x', 'y', 'z'])
    p = Point(1, 2, 3)
    print(f"Point: x={p.x}, y={p.y}, z={p.z}")
    
    # Dictionary comprehension
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squares dict: {squares_dict}")
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")


# Walrus Operator (Python 3.8+)
def walrus_operator_demo():
    """Demonstrate walrus operator :="""
    print("\n🦭 WALRUS OPERATOR DEMO")
    print("-" * 60)
    
    # Traditional way
    data = [1, 2, 3, 4, 5]
    length = len(data)
    if length > 3:
        print(f"Traditional: List has {length} items (more than 3)")
    
    # With walrus operator
    if (length := len(data)) > 3:
        print(f"Walrus: List has {length} items (more than 3)")
    
    # In list comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    doubled_evens = [doubled for n in numbers if (doubled := n * 2) > 10]
    print(f"Doubled evens > 10: {doubled_evens}")


# F-strings with expressions
def fstring_demo():
    """Demonstrate advanced f-string features"""
    print("\n🔤 F-STRING DEMO")
    print("-" * 60)
    
    name = "Python"
    version = 3.12
    
    # Basic f-string
    print(f"Language: {name}, Version: {version}")
    
    # Expressions in f-strings
    print(f"10 squared is {10**2}")
    
    # Formatting
    pi = 3.14159265359
    print(f"Pi to 2 decimals: {pi:.2f}")
    
    # Alignment
    print(f"{'Left':<10} {'Center':^10} {'Right':>10}")
    
    # Debug feature (Python 3.8+)
    x, y = 10, 20
    print(f"{x=}, {y=}, {x+y=}")


# Main demonstration
async def main():
    """Main async function"""
    print("=" * 60)
    print("🐍 MODERN PYTHON FEATURES SHOWCASE")
    print("=" * 60)
    
    # Dataclasses
    print("\n1️⃣  DATACLASSES")
    print("-" * 60)
    person = Person(
        name="Alice Johnson",
        age=28,
        email="alice@example.com",
        hobbies=["reading", "coding", "hiking"],
        metadata={"country": "USA", "occupation": "Developer"}
    )
    print(person)
    print(f"Is adult: {person.is_adult()}")
    print(f"JSON:\n{person.to_json()}")
    
    task = Task(
        title="Learn Python",
        description="Master modern Python features",
        priority=5,
        tags=["education", "programming"]
    )
    print(f"\n{task}")
    task.mark_completed()
    print(f"After completion: {task}")
    
    # Type Hints
    print("\n2️⃣  TYPE HINTS & UNION TYPES")
    print("-" * 60)
    print(f"process_data('hello'): {process_data('hello')}")
    print(f"process_data(10): {process_data(10)}")
    print(f"process_data([1,2,3,4,5]): {process_data([1, 2, 3, 4, 5])}")
    
    # Async/Await
    print("\n3️⃣  ASYNC/AWAIT")
    print("-" * 60)
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/comments"
    ]
    results = await fetch_multiple(urls)
    for result in results:
        print(f"✅ {result['url']}: {result['status']}")
    
    # Async generator
    print("\nAsync generator:")
    async for value in async_generator(5):
        print(f"Generated: {value}")
    
    # Collections
    collections_demo()
    
    # Walrus Operator
    walrus_operator_demo()
    
    # F-strings
    fstring_demo()
    
    print("\n" + "=" * 60)
    print("✨ Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
