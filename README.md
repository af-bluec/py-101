# Python Features Showcase - README

This collection demonstrates 10 advanced Python features through comprehensive examples with detailed documentation.

## Files Overview

### 1. **decorators_demo.py** - Function decorators, class decorators, and property decorators
- Basic function decorators with timing and retry functionality
- Parameterized decorators for configurable behavior
- Class decorators for automatic method generation
- Method decorators with validation
- Chaining multiple decorators

### 2. **context_managers.py** - Custom context managers using `__enter__`/`__exit__` and contextlib
- Custom context manager classes with the `__enter__`/`__exit__` protocol
- Context managers using `@contextlib.contextmanager` decorator
- Exception handling and resource cleanup
- Nested context managers
- Database transaction management with rollback

### 3. **generators_iterators.py** - Generator functions, generator expressions, and custom iterators
- Generator functions with `yield`
- Custom iterator classes implementing `__iter__` and `__next__`
- Generator expressions for memory-efficient processing
- Infinite iterators and data streaming
- Coroutines using generators

### 4. **metaclasses_demo.py** - Metaclasses and class creation customization
- Custom metaclasses for singleton pattern
- Attribute validation at class creation time
- Automatic property generation
- ORM-style field definitions
- Dynamic class creation and introspection

### 5. **async_programming.py** - Async/await, asyncio, and concurrent programming
- Basic async functions and `await` usage
- Async context managers and iterators
- Concurrent task execution with `asyncio.gather()`
- Producer-consumer patterns with async queues
- Task cancellation and error handling

### 6. **dataclasses_demo.py** - Dataclasses, type hints, and modern Python features
- Basic dataclass definitions with automatic method generation
- Field definitions with defaults and factories
- Frozen (immutable) dataclasses
- Post-init processing and validation
- Inheritance with dataclasses and abstract base classes

### 7. **descriptors_demo.py** - Descriptor protocol and property management
- Data vs non-data descriptors
- Validation descriptors for type and range checking
- Caching descriptors for expensive computations
- Logging descriptors for access tracking
- Weak reference descriptors to avoid circular references

### 8. **collections_demo.py** - Collections module features and custom collections
- `namedtuple` for structured data
- `Counter` for counting and arithmetic operations
- `defaultdict` for automatic default values
- `deque` for efficient double-ended operations
- `OrderedDict`, `ChainMap`, and custom collection classes

### 9. **pathlib_demo.py** - Modern path handling with pathlib
- Object-oriented path operations
- Cross-platform path handling
- File and directory operations
- Path pattern matching and globbing
- File system navigation and metadata

### 10. **functional_programming.py** - Functional programming concepts in Python
- Higher-order functions and function composition
- Currying and partial application
- Immutable data structures
- Maybe monad for safe computations
- Memoization for optimization

## Running the Examples

Each file can be run independently to see demonstrations of the features:

```bash
python3 decorators_demo.py
python3 context_managers.py
python3 generators_iterators.py
python3 metaclasses_demo.py
python3 async_programming.py
python3 dataclasses_demo.py
python3 descriptors_demo.py
python3 collections_demo.py
python3 pathlib_demo.py
python3 functional_programming.py
```

## Key Learning Points

- **Decorators**: Powerful way to modify or extend function/class behavior
- **Context Managers**: Proper resource management and cleanup
- **Generators**: Memory-efficient data processing and lazy evaluation
- **Metaclasses**: Control over class creation and behavior
- **Async Programming**: Concurrent execution for I/O-bound operations
- **Dataclasses**: Modern way to create structured data classes
- **Descriptors**: Fine-grained control over attribute access
- **Collections**: Specialized data structures for specific use cases
- **Pathlib**: Modern, object-oriented file system operations
- **Functional Programming**: Pure functions, immutability, and composition

Each example includes comprehensive documentation, error handling, and practical use cases to demonstrate real-world applications of these Python features.
