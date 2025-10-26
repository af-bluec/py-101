"""
Python Descriptors Demonstration

This module showcases the descriptor protocol in Python:
- Data descriptors vs non-data descriptors
- Property-like descriptors
- Validation descriptors
- Caching descriptors
- Method descriptors
- Descriptor usage in classes

Descriptors are a way to customize attribute access. They define how
attributes are get, set, and deleted on instances of a class.
"""

import weakref
import functools
from typing import Any, Callable, Optional, Dict, Union
from datetime import datetime


class Descriptor:
    """
    Base descriptor class demonstrating the descriptor protocol.
    
    Descriptors implement __get__, __set__, and/or __delete__ methods.
    """
    
    def __init__(self, name: str = None):
        self.name = name
    
    def __set_name__(self, owner, name):
        """Called when the descriptor is assigned to a class attribute."""
        if self.name is None:
            self.name = name
    
    def __get__(self, instance, owner):
        """Get the attribute value."""
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        """Set the attribute value."""
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        """Delete the attribute."""
        del instance.__dict__[self.name]


class TypedDescriptor(Descriptor):
    """
    A descriptor that enforces type validation.
    
    This is a data descriptor (has both __get__ and __set__).
    """
    
    def __init__(self, expected_type: type, name: str = None):
        super().__init__(name)
        self.expected_type = expected_type
    
    def __set__(self, instance, value):
        """Set the attribute value with type validation."""
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be of type {self.expected_type.__name__}, "
                          f"got {type(value).__name__}")
        super().__set__(instance, value)


class RangeDescriptor(Descriptor):
    """
    A descriptor that enforces value range validation.
    """
    
    def __init__(self, min_value: float = None, max_value: float = None, name: str = None):
        super().__init__(name)
        self.min_value = min_value
        self.max_value = max_value
    
    def __set__(self, instance, value):
        """Set the attribute value with range validation."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        
        super().__set__(instance, value)


class CachedProperty:
    """
    A descriptor that caches the result of a method call.
    
    Similar to functools.cached_property but with custom implementation.
    """
    
    def __init__(self, func: Callable):
        self.func = func
        self.name = func.__name__
        self.__doc__ = func.__doc__
    
    def __get__(self, instance, owner):
        """Get the cached value or compute and cache it."""
        if instance is None:
            return self
        
        # Check if value is already cached
        cache_attr = f'_cached_{self.name}'
        
        if hasattr(instance, cache_attr):
            return getattr(instance, cache_attr)
        
        # Compute and cache the value
        value = self.func(instance)
        setattr(instance, cache_attr, value)
        return value
    
    def __set__(self, instance, value):
        """Allow manual setting of cached value."""
        cache_attr = f'_cached_{self.name}'
        setattr(instance, cache_attr, value)
    
    def __delete__(self, instance):
        """Clear the cached value."""
        cache_attr = f'_cached_{self.name}'
        if hasattr(instance, cache_attr):
            delattr(instance, cache_attr)


class LoggingDescriptor:
    """
    A descriptor that logs all attribute access.
    """
    
    def __init__(self, name: str = None):
        self.name = name
        self.access_log = []
    
    def __set_name__(self, owner, name):
        if self.name is None:
            self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        value = instance.__dict__.get(self.name)
        self.access_log.append(f"GET {self.name}: {value} at {datetime.now()}")
        return value
    
    def __set__(self, instance, value):
        old_value = instance.__dict__.get(self.name, "<not set>")
        instance.__dict__[self.name] = value
        self.access_log.append(f"SET {self.name}: {old_value} -> {value} at {datetime.now()}")
    
    def get_access_log(self):
        """Get the access log for this descriptor."""
        return self.access_log.copy()


class WeakRefDescriptor:
    """
    A descriptor that stores object references using weak references.
    
    Useful for avoiding circular references.
    """
    
    def __init__(self, name: str = None):
        self.name = name
        self.data = weakref.WeakKeyDictionary()
    
    def __set_name__(self, owner, name):
        if self.name is None:
            self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance)
    
    def __set__(self, instance, value):
        self.data[instance] = value
    
    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]


class ValidatedProperty:
    """
    A descriptor factory for creating validated properties.
    """
    
    def __init__(self, validator: Callable[[Any], bool], error_message: str = None):
        self.validator = validator
        self.error_message = error_message or "Validation failed"
    
    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)
    
    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"{self.name}: {self.error_message}")
        setattr(instance, self.private_name, value)


class MethodDescriptor:
    """
    A descriptor that wraps methods with additional functionality.
    """
    
    def __init__(self, func: Callable):
        self.func = func
        functools.update_wrapper(self, func)
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Return a bound method with additional functionality
        def wrapper(*args, **kwargs):
            print(f"Calling method {self.func.__name__} on {instance}")
            result = self.func(instance, *args, **kwargs)
            print(f"Method {self.func.__name__} completed")
            return result
        
        return wrapper


# Example classes using descriptors

class Person:
    """Person class using various descriptors for validation."""
    
    name = TypedDescriptor(str)
    age = RangeDescriptor(0, 150)
    email = ValidatedProperty(
        lambda x: isinstance(x, str) and '@' in x,
        "Email must be a string containing '@'"
    )
    logged_attribute = LoggingDescriptor()
    
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
        self.logged_attribute = "initial_value"
    
    @MethodDescriptor
    def greet(self):
        """Greet with method descriptor wrapper."""
        return f"Hello, I'm {self.name}"


class ComputationClass:
    """Class demonstrating cached properties."""
    
    def __init__(self, base_value: float):
        self.base_value = base_value
    
    @CachedProperty
    def expensive_computation(self):
        """Simulate an expensive computation that should be cached."""
        print("Performing expensive computation...")
        import time
        time.sleep(0.1)  # Simulate work
        return self.base_value ** 10
    
    @CachedProperty
    def complex_calculation(self):
        """Another cached computation."""
        print("Performing complex calculation...")
        result = 0
        for i in range(1000000):
            result += i * self.base_value
        return result


class Node:
    """Node class demonstrating weak reference descriptors to avoid circular references."""
    
    parent = WeakRefDescriptor()
    
    def __init__(self, name: str, parent: 'Node' = None):
        self.name = name
        self.children = []
        if parent:
            self.parent = parent
            parent.children.append(self)
    
    def __repr__(self):
        parent_name = self.parent.name if self.parent else None
        return f"Node(name='{self.name}', parent={parent_name})"


def demonstrate_descriptor_introspection():
    """Demonstrate introspection of descriptors."""
    print("\n=== Descriptor Introspection ===")
    
    # Inspect Person class descriptors
    print("Person class descriptors:")
    for attr_name in dir(Person):
        if not attr_name.startswith('_'):
            attr = getattr(Person, attr_name)
            if hasattr(attr, '__get__') or hasattr(attr, '__set__'):
                descriptor_type = []
                if hasattr(attr, '__get__'):
                    descriptor_type.append('get')
                if hasattr(attr, '__set__'):
                    descriptor_type.append('set')
                if hasattr(attr, '__delete__'):
                    descriptor_type.append('delete')
                
                print(f"  {attr_name}: {type(attr).__name__} ({', '.join(descriptor_type)})")


def demonstrate_descriptor_priority():
    """Demonstrate descriptor resolution priority."""
    print("\n=== Descriptor Priority Demo ===")
    
    class TestClass:
        # Data descriptor (has both __get__ and __set__)
        data_desc = TypedDescriptor(str)
        
        # Non-data descriptor (only has __get__)
        class NonDataDescriptor:
            def __get__(self, instance, owner):
                return "non-data descriptor value"
        
        non_data_desc = NonDataDescriptor()
    
    obj = TestClass()
    
    # Data descriptor takes priority over instance dict
    obj.data_desc = "hello"
    obj.__dict__['data_desc'] = "instance value"  # This won't be seen
    print(f"data_desc (data descriptor): {obj.data_desc}")
    
    # Instance dict takes priority over non-data descriptor
    obj.__dict__['non_data_desc'] = "instance override"
    print(f"non_data_desc (non-data descriptor): {obj.non_data_desc}")
    
    # Remove from instance dict to see descriptor
    del obj.__dict__['non_data_desc']
    print(f"non_data_desc (after del): {obj.non_data_desc}")


if __name__ == "__main__":
    print("=== Python Descriptors Demo ===")
    
    # Basic descriptor usage
    print("\n1. Basic Descriptor Usage:")
    try:
        person = Person("Alice", 30, "alice@example.com")
        print(f"Person created: {person.name}, {person.age}, {person.email}")
        
        # Test validation
        person.age = 25  # Valid
        print(f"Updated age: {person.age}")
        
        # This should raise an error
        person.age = -5
    except ValueError as e:
        print(f"Validation error caught: {e}")
    
    try:
        # This should also raise an error
        person.name = 123
    except TypeError as e:
        print(f"Type error caught: {e}")
    
    # Logging descriptor
    print("\n2. Logging Descriptor:")
    person.logged_attribute = "new value"
    value = person.logged_attribute
    person.logged_attribute = "another value"
    
    # Get the access log
    log_entries = Person.logged_attribute.get_access_log()
    print("Access log:")
    for entry in log_entries[-3:]:  # Show last 3 entries
        print(f"  {entry}")
    
    # Method descriptor
    print("\n3. Method Descriptor:")
    greeting = person.greet()
    print(f"Greeting result: {greeting}")
    
    # Cached properties
    print("\n4. Cached Properties:")
    calc = ComputationClass(2.5)
    
    print("First access to expensive_computation:")
    result1 = calc.expensive_computation
    print(f"Result: {result1}")
    
    print("Second access to expensive_computation (should be cached):")
    result2 = calc.expensive_computation
    print(f"Result: {result2}")
    
    # Clear cache and access again
    del calc.expensive_computation
    print("After clearing cache:")
    result3 = calc.expensive_computation
    print(f"Result: {result3}")
    
    # Weak reference descriptors
    print("\n5. Weak Reference Descriptors:")
    root = Node("root")
    child1 = Node("child1", root)
    child2 = Node("child2", root)
    grandchild = Node("grandchild", child1)
    
    print(f"Root: {root}")
    print(f"Child1: {child1}")
    print(f"Grandchild: {grandchild}")
    print(f"Root children: {[child.name for child in root.children]}")
    
    # Test weak reference behavior
    print("Deleting child1...")
    del child1
    print(f"Grandchild parent after deletion: {grandchild.parent}")
    
    # Run additional demonstrations
    demonstrate_descriptor_introspection()
    demonstrate_descriptor_priority()
    
    print("\n=== Descriptors Demo Complete ===")
