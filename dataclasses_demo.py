"""
Python Dataclasses Demonstration

This module showcases dataclasses and modern Python type system features:
- Basic dataclasses with automatic __init__, __repr__, etc.
- Field definitions with default values and factories
- Type hints and annotations
- Post-init processing
- Frozen dataclasses (immutable)
- Inheritance with dataclasses
- Custom field validation
- JSON serialization/deserialization

Dataclasses provide a decorator and functions for automatically adding
generated special methods to user-defined classes.
"""

from dataclasses import dataclass, field, fields, asdict, astuple, InitVar
from typing import List, Dict, Optional, Union, Any, ClassVar
from datetime import datetime, date
from enum import Enum, auto
import json
from abc import ABC, abstractmethod


class Status(Enum):
    """Status enumeration for demonstration."""
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()
    ARCHIVED = auto()


@dataclass
class Person:
    """
    Basic dataclass representing a person.
    
    Automatically generates __init__, __repr__, __eq__, etc.
    """
    name: str
    age: int
    email: str = ""  # Default value
    active: bool = True
    
    def greet(self) -> str:
        """Custom method for greeting."""
        return f"Hello, I'm {self.name} and I'm {self.age} years old."


@dataclass
class Address:
    """Address dataclass with various field types."""
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"
    
    def full_address(self) -> str:
        """Return the full formatted address."""
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"


@dataclass
class Product:
    """
    Product dataclass demonstrating field() usage and factories.
    """
    name: str
    price: float
    category: str
    tags: List[str] = field(default_factory=list)  # Mutable default
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    
    # Class variable (not an instance field)
    total_products: ClassVar[int] = 0
    
    def __post_init__(self):
        """Called after __init__ for additional processing."""
        Product.total_products += 1
        
        # Validate price
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        
        # Ensure category is uppercase
        self.category = self.category.upper()
    
    def add_tag(self, tag: str) -> None:
        """Add a tag to the product."""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def set_metadata(self, key: str, value: Any) -> None:
        """Set metadata for the product."""
        self.metadata[key] = value


@dataclass(frozen=True)
class ImmutablePoint:
    """
    Frozen (immutable) dataclass representing a 2D point.
    
    frozen=True makes instances immutable after creation.
    """
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        """Calculate distance from origin (0, 0)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def distance_to(self, other: 'ImmutablePoint') -> float:
        """Calculate distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class Employee:
    """
    Employee dataclass with InitVar for parameters not stored as fields.
    """
    name: str
    position: str
    salary: float
    hire_date: date
    department: str = "General"
    
    # InitVar - used in __post_init__ but not stored as field
    years_experience: InitVar[int] = 0
    
    def __post_init__(self, years_experience: int):
        """Process InitVar parameters."""
        if years_experience > 0:
            # Adjust salary based on experience
            self.salary *= (1 + years_experience * 0.05)


@dataclass
class Manager(Employee):
    """
    Manager class inheriting from Employee dataclass.
    
    Demonstrates dataclass inheritance.
    """
    team_size: int = 0
    budget: float = 0.0
    
    def __post_init__(self, years_experience: int):
        """Call parent's __post_init__ and add manager-specific logic."""
        super().__post_init__(years_experience)
        
        # Manager bonus based on team size
        if self.team_size > 5:
            self.salary *= 1.1


@dataclass
class Order:
    """
    Order dataclass with complex field relationships.
    """
    order_id: str
    customer: Person
    items: List[Product] = field(default_factory=list)
    shipping_address: Optional[Address] = None
    status: Status = Status.PENDING
    total: float = field(init=False)  # Calculated field, not in __init__
    
    def __post_init__(self):
        """Calculate order total."""
        self.total = sum(item.price for item in self.items)
    
    def add_item(self, product: Product) -> None:
        """Add a product to the order."""
        self.items.append(product)
        self.total += product.price
    
    def remove_item(self, product: Product) -> None:
        """Remove a product from the order."""
        if product in self.items:
            self.items.remove(product)
            self.total -= product.price


# Abstract base dataclass
@dataclass
class Shape(ABC):
    """Abstract base dataclass for shapes."""
    color: str = "black"
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass


@dataclass
class Rectangle(Shape):
    """Rectangle shape implementation."""
    width: float
    height: float
    
    def area(self) -> float:
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)


@dataclass
class Circle(Shape):
    """Circle shape implementation."""
    radius: float
    
    def area(self) -> float:
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle perimeter (circumference)."""
        import math
        return 2 * math.pi * self.radius


def demonstrate_serialization():
    """Demonstrate dataclass serialization to/from JSON."""
    print("\n=== Dataclass Serialization Demo ===")
    
    # Create a product with complex data
    product = Product(
        name="Laptop",
        price=999.99,
        category="electronics",
        tags=["computer", "portable", "business"],
        metadata={"brand": "TechCorp", "model": "TC-2023", "warranty": 2}
    )
    
    print(f"Original product: {product}")
    
    # Convert to dictionary
    product_dict = asdict(product)
    print(f"\nAs dictionary: {product_dict}")
    
    # Convert to JSON string
    json_str = json.dumps(product_dict, default=str, indent=2)
    print(f"\nAs JSON:\n{json_str}")
    
    # Convert back from dictionary (manual reconstruction)
    loaded_dict = json.loads(json_str)
    # Note: datetime needs special handling
    loaded_dict['created_at'] = datetime.fromisoformat(loaded_dict['created_at'])
    
    reconstructed_product = Product(**loaded_dict)
    print(f"\nReconstructed product: {reconstructed_product}")
    
    # Convert to tuple
    product_tuple = astuple(product)
    print(f"\nAs tuple: {product_tuple}")


def demonstrate_field_introspection():
    """Demonstrate introspection of dataclass fields."""
    print("\n=== Dataclass Field Introspection ===")
    
    # Get field information
    product_fields = fields(Product)
    
    print("Product fields:")
    for field_info in product_fields:
        print(f"  {field_info.name}: {field_info.type}")
        if field_info.default != field_info.default_factory:
            if field_info.default_factory != field_info.default_factory.__class__():
                print(f"    Default factory: {field_info.default_factory}")
            else:
                print(f"    Default: {field_info.default}")
    
    # Create instance and inspect values
    product = Product("Test Product", 50.0, "test")
    
    print(f"\nProduct instance field values:")
    for field_info in fields(product):
        value = getattr(product, field_info.name)
        print(f"  {field_info.name}: {value}")


def demonstrate_comparison_and_hashing():
    """Demonstrate dataclass comparison and hashing behavior."""
    print("\n=== Dataclass Comparison and Hashing ===")
    
    # Regular dataclass (mutable, hashable by default in simple cases)
    person1 = Person("Alice", 30, "alice@example.com")
    person2 = Person("Alice", 30, "alice@example.com")
    person3 = Person("Bob", 25, "bob@example.com")
    
    print(f"person1 == person2: {person1 == person2}")  # True - same values
    print(f"person1 == person3: {person1 == person3}")  # False - different values
    print(f"person1 is person2: {person1 is person2}")  # False - different objects
    
    # Frozen dataclass (immutable, hashable)
    point1 = ImmutablePoint(3.0, 4.0)
    point2 = ImmutablePoint(3.0, 4.0)
    point3 = ImmutablePoint(1.0, 2.0)
    
    print(f"\npoint1 == point2: {point1 == point2}")  # True
    print(f"point1 == point3: {point1 == point3}")  # False
    
    # Frozen dataclasses are hashable
    point_set = {point1, point2, point3}
    print(f"Unique points in set: {len(point_set)}")  # 2 (point1 and point2 are equal)
    
    try:
        # This would raise an error - frozen objects can't be modified
        # point1.x = 5.0
        print("Cannot modify frozen dataclass (would raise FrozenInstanceError)")
    except AttributeError:
        print("Frozen dataclass is immutable")


if __name__ == "__main__":
    print("=== Python Dataclasses Demo ===")
    
    # Basic dataclass usage
    print("\n1. Basic Dataclass Usage:")
    person = Person("Alice Johnson", 28, "alice@example.com")
    print(f"Person: {person}")
    print(f"Greeting: {person.greet()}")
    
    # Dataclass with field factories
    print("\n2. Dataclass with Field Factories:")
    product1 = Product("Smartphone", 599.99, "electronics")
    product1.add_tag("mobile")
    product1.add_tag("communication")
    product1.set_metadata("brand", "TechPhone")
    
    print(f"Product: {product1}")
    print(f"Total products created: {Product.total_products}")
    
    product2 = Product("Tablet", 399.99, "electronics", ["portable", "entertainment"])
    print(f"Another product: {product2}")
    print(f"Total products created: {Product.total_products}")
    
    # Frozen dataclass
    print("\n3. Frozen (Immutable) Dataclass:")
    point1 = ImmutablePoint(3.0, 4.0)
    point2 = ImmutablePoint(0.0, 0.0)
    
    print(f"Point 1: {point1}")
    print(f"Distance from origin: {point1.distance_from_origin():.2f}")
    print(f"Distance to {point2}: {point1.distance_to(point2):.2f}")
    
    # InitVar usage
    print("\n4. InitVar and Inheritance:")
    employee = Employee("John Doe", "Developer", 50000, date.today(), years_experience=5)
    print(f"Employee: {employee}")
    
    manager = Manager("Jane Smith", "Engineering Manager", 80000, date.today(), 
                     team_size=8, budget=500000, years_experience=10)
    print(f"Manager: {manager}")
    
    # Complex dataclass with relationships
    print("\n5. Complex Dataclass Relationships:")
    customer = Person("Bob Customer", 35, "bob@customer.com")
    address = Address("123 Main St", "Anytown", "CA", "12345")
    
    order = Order("ORD-001", customer, shipping_address=address)
    order.add_item(product1)
    order.add_item(product2)
    
    print(f"Order: {order}")
    print(f"Order total: ${order.total:.2f}")
    print(f"Shipping to: {address.full_address()}")
    
    # Abstract dataclass and inheritance
    print("\n6. Abstract Dataclass and Shapes:")
    rectangle = Rectangle("blue", 5.0, 3.0)
    circle = Circle("red", 2.5)
    
    shapes = [rectangle, circle]
    for shape in shapes:
        print(f"{type(shape).__name__} ({shape.color}): "
              f"Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
    
    # Run additional demonstrations
    demonstrate_serialization()
    demonstrate_field_introspection()
    demonstrate_comparison_and_hashing()
    
    print("\n=== Dataclasses Demo Complete ===")
