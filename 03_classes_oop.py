"""
Demonstration of Object-Oriented Programming in Python.
Covers classes, inheritance, polymorphism, and special methods.
"""

# Basic class
class Person:
    """Basic class with constructor and methods."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! Now {self.age} years old."


# Class with class variables and methods
class BankAccount:
    """Class demonstrating class variables and methods."""
    
    interest_rate = 0.02  # Class variable
    total_accounts = 0
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0


# Inheritance
class Animal:
    """Base class for inheritance example."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    """Derived class demonstrating inheritance."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    """Another derived class."""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture!"


# Special methods (magic methods)
class Vector:
    """Class demonstrating special methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5


# Property decorators
class Temperature:
    """Class demonstrating property decorators."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9


def main():
    print("=== BASIC CLASS ===")
    person = Person("Alice", 30)
    print(person.introduce())
    print(person.have_birthday())
    
    print("\n=== CLASS VARIABLES AND METHODS ===")
    account1 = BankAccount("Bob", 1000)
    account2 = BankAccount("Charlie", 500)
    print(account1.deposit(500))
    print(account1.withdraw(200))
    print(f"Total accounts: {BankAccount.get_total_accounts()}")
    print(f"Valid amount? {BankAccount.validate_amount(100)}")
    
    print("\n=== INHERITANCE ===")
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    print(dog.info())
    print(f"{dog.name} says: {dog.make_sound()}")
    print(dog.fetch())
    print(cat.info())
    print(f"{cat.name} says: {cat.make_sound()}")
    print(cat.scratch())
    
    print("\n=== POLYMORPHISM ===")
    animals = [dog, cat]
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")
    
    print("\n=== SPECIAL METHODS ===")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 2: {v1 * 2}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
    
    print("\n=== PROPERTIES ===")
    temp = Temperature(25)
    print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")
    temp.fahrenheit = 86
    print(f"After setting to 86°F: {temp.celsius}°C")


if __name__ == "__main__":
    main()
