"""
Python Metaclasses Demonstration

This module showcases metaclasses in Python:
- Understanding type as a metaclass
- Creating custom metaclasses
- Class creation customization
- Attribute validation and transformation
- Singleton pattern with metaclasses
- ORM-style field definitions

Metaclasses are "classes whose instances are classes". They control
how classes are created and can modify class behavior at definition time.
"""

import functools
from typing import Any, Dict, Type, Union


class SingletonMeta(type):
    """
    A metaclass that implements the Singleton pattern.
    
    Classes using this metaclass will have only one instance.
    """
    
    _instances: Dict[Type, Any] = {}
    
    def __call__(cls, *args, **kwargs):
        """Control instance creation to ensure singleton behavior."""
        if cls not in cls._instances:
            # Create the instance only if it doesn't exist
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print(f"Created new instance of {cls.__name__}")
        else:
            print(f"Returning existing instance of {cls.__name__}")
        
        return cls._instances[cls]


class ValidatedMeta(type):
    """
    A metaclass that adds validation to class attributes.
    
    This metaclass inspects class attributes and adds validation
    based on type annotations.
    """
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Create a new class with validation capabilities."""
        
        # Get type annotations from the class
        annotations = namespace.get('__annotations__', {})
        
        # Store original __init__ method
        original_init = namespace.get('__init__')
        
        def validated_init(self, **init_kwargs):
            """Enhanced __init__ with type validation."""
            
            # Call original __init__ if it exists
            if original_init:
                original_init(self, **init_kwargs)
            
            # Validate and set attributes
            for attr_name, attr_type in annotations.items():
                if attr_name in init_kwargs:
                    value = init_kwargs[attr_name]
                    
                    # Type validation
                    if not isinstance(value, attr_type):
                        raise TypeError(f"{attr_name} must be of type {attr_type.__name__}, "
                                      f"got {type(value).__name__}")
                    
                    setattr(self, attr_name, value)
        
        # Replace __init__ with validated version
        namespace['__init__'] = validated_init
        
        # Create the class
        cls = super().__new__(mcs, name, bases, namespace)
        
        print(f"Created validated class: {name}")
        if annotations:
            print(f"  Validated attributes: {list(annotations.keys())}")
        
        return cls


class AutoPropertyMeta(type):
    """
    A metaclass that automatically creates properties for private attributes.
    
    Attributes starting with underscore get automatic getter/setter properties.
    """
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Create properties for private attributes."""
        
        # Find attributes that should become properties
        private_attrs = []
        for key, value in list(namespace.items()):
            if key.startswith('_') and not key.startswith('__'):
                private_attrs.append(key)
        
        # Create properties for private attributes
        for attr_name in private_attrs:
            prop_name = attr_name[1:]  # Remove leading underscore
            
            def make_property(attr):
                """Create a property for the given attribute."""
                def getter(self):
                    return getattr(self, attr)
                
                def setter(self, value):
                    print(f"Setting {attr} = {value}")
                    setattr(self, attr, value)
                
                return property(getter, setter)
            
            # Add property to namespace
            namespace[prop_name] = make_property(attr_name)
        
        return super().__new__(mcs, name, bases, namespace)


class FieldMeta(type):
    """
    A metaclass for creating ORM-style field definitions.
    
    This metaclass processes Field definitions and creates
    a schema for the class.
    """
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Process field definitions."""
        
        # Collect field definitions
        fields = {}
        for key, value in list(namespace.items()):
            if isinstance(value, Field):
                fields[key] = value
                # Remove field definition from namespace
                del namespace[key]
        
        # Store field metadata
        namespace['_fields'] = fields
        
        # Create enhanced __init__
        def field_init(self, **kwargs):
            """Initialize instance with field validation."""
            for field_name, field_obj in self._fields.items():
                if field_name in kwargs:
                    value = kwargs[field_name]
                    # Validate field
                    if not field_obj.validate(value):
                        raise ValueError(f"Invalid value for {field_name}: {value}")
                    setattr(self, field_name, value)
                elif field_obj.required:
                    raise ValueError(f"Required field {field_name} not provided")
                else:
                    setattr(self, field_name, field_obj.default)
        
        namespace['__init__'] = field_init
        
        # Add string representation
        def __repr__(self):
            field_values = []
            for field_name in self._fields:
                value = getattr(self, field_name, None)
                field_values.append(f"{field_name}={value!r}")
            return f"{name}({', '.join(field_values)})"
        
        namespace['__repr__'] = __repr__
        
        return super().__new__(mcs, name, bases, namespace)


class Field:
    """Base class for field definitions."""
    
    def __init__(self, field_type: Type, required: bool = True, default: Any = None):
        self.field_type = field_type
        self.required = required
        self.default = default
    
    def validate(self, value: Any) -> bool:
        """Validate a value for this field."""
        return isinstance(value, self.field_type)


class StringField(Field):
    """String field with additional validation."""
    
    def __init__(self, max_length: int = None, **kwargs):
        super().__init__(str, **kwargs)
        self.max_length = max_length
    
    def validate(self, value: Any) -> bool:
        """Validate string field."""
        if not super().validate(value):
            return False
        
        if self.max_length and len(value) > self.max_length:
            return False
        
        return True


class IntegerField(Field):
    """Integer field with range validation."""
    
    def __init__(self, min_value: int = None, max_value: int = None, **kwargs):
        super().__init__(int, **kwargs)
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value: Any) -> bool:
        """Validate integer field."""
        if not super().validate(value):
            return False
        
        if self.min_value is not None and value < self.min_value:
            return False
        
        if self.max_value is not None and value > self.max_value:
            return False
        
        return True


# Example classes using different metaclasses

class DatabaseConnection(metaclass=SingletonMeta):
    """A database connection using singleton pattern."""
    
    def __init__(self, connection_string: str = "default_connection"):
        self.connection_string = connection_string
        self.is_connected = False
    
    def connect(self):
        """Connect to the database."""
        self.is_connected = True
        print(f"Connected to database: {self.connection_string}")
    
    def disconnect(self):
        """Disconnect from the database."""
        self.is_connected = False
        print("Disconnected from database")


class Person(metaclass=ValidatedMeta):
    """A person class with validated attributes."""
    
    name: str
    age: int
    email: str
    
    def __init__(self, **kwargs):
        # The metaclass will handle validation
        pass
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"


class Temperature(metaclass=AutoPropertyMeta):
    """Temperature class with automatic properties."""
    
    def __init__(self, celsius: float):
        self._celsius = celsius
        self._fahrenheit = celsius * 9/5 + 32
    
    def __repr__(self):
        return f"Temperature({self.celsius}°C / {self.fahrenheit}°F)"


class User(metaclass=FieldMeta):
    """User model with field definitions."""
    
    name = StringField(max_length=50)
    age = IntegerField(min_value=0, max_value=150)
    email = StringField()
    is_active = Field(bool, required=False, default=True)


def demonstrate_metaclass_introspection():
    """Demonstrate metaclass introspection capabilities."""
    print("\n=== Metaclass Introspection ===")
    
    # Show class creation process
    print("1. Class hierarchy and metaclasses:")
    
    classes = [DatabaseConnection, Person, Temperature, User]
    for cls in classes:
        print(f"  {cls.__name__}:")
        print(f"    Metaclass: {type(cls).__name__}")
        print(f"    MRO: {[c.__name__ for c in cls.__mro__]}")
        
        # Show special attributes added by metaclass
        if hasattr(cls, '_fields'):
            print(f"    Fields: {list(cls._fields.keys())}")


def demonstrate_dynamic_class_creation():
    """Demonstrate creating classes dynamically with metaclasses."""
    print("\n=== Dynamic Class Creation ===")
    
    # Create a class dynamically using type (the default metaclass)
    def dynamic_init(self, value):
        self.value = value
    
    def dynamic_method(self):
        return f"DynamicClass with value: {self.value}"
    
    # Create class using type as metaclass
    DynamicClass = type('DynamicClass', (), {
        '__init__': dynamic_init,
        'get_info': dynamic_method
    })
    
    # Use the dynamically created class
    obj = DynamicClass("Hello, Metaclass!")
    print(f"Dynamic class instance: {obj.get_info()}")
    
    # Create a class with a custom metaclass dynamically
    ValidatedDynamic = ValidatedMeta('ValidatedDynamic', (), {
        '__annotations__': {'name': str, 'value': int},
        '__init__': lambda self, **kwargs: None
    })
    
    try:
        valid_obj = ValidatedDynamic(name="Test", value=42)
        print(f"Valid dynamic object created: name='{valid_obj.name}', value={valid_obj.value}")
    except TypeError as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    print("=== Python Metaclasses Demo ===")
    
    # Singleton metaclass demo
    print("\n1. Singleton Metaclass Demo:")
    db1 = DatabaseConnection("connection_1")
    db2 = DatabaseConnection("connection_2")  # Same instance as db1
    
    print(f"db1 is db2: {db1 is db2}")
    print(f"db1 connection string: {db1.connection_string}")
    
    # Validated metaclass demo
    print("\n2. Validated Metaclass Demo:")
    try:
        person1 = Person(name="Alice", age=30, email="alice@example.com")
        print(f"Valid person: {person1}")
        
        # This should raise a TypeError
        person2 = Person(name="Bob", age="thirty", email="bob@example.com")
    except TypeError as e:
        print(f"Validation error caught: {e}")
    
    # Auto-property metaclass demo
    print("\n3. Auto-Property Metaclass Demo:")
    temp = Temperature(25.0)
    print(f"Initial temperature: {temp}")
    
    # The metaclass created properties for _celsius and _fahrenheit
    temp.celsius = 30.0  # This will trigger the setter
    print(f"Updated temperature: {temp}")
    
    # Field metaclass demo
    print("\n4. Field Metaclass Demo:")
    try:
        user1 = User(name="John Doe", age=25, email="john@example.com")
        print(f"Valid user: {user1}")
        
        # This should raise a ValueError (age out of range)
        user2 = User(name="Jane Doe", age=200, email="jane@example.com")
    except ValueError as e:
        print(f"Field validation error: {e}")
    
    # Test with default values
    user3 = User(name="Bob", age=30, email="bob@example.com")
    print(f"User with default is_active: {user3}")
    
    # Run additional demonstrations
    demonstrate_metaclass_introspection()
    demonstrate_dynamic_class_creation()
    
    print("\n=== Metaclasses Demo Complete ===")
