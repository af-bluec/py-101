# Contributing Guidelines

## Python 101 - How to Contribute

We welcome contributions to the Python 101 project! This guide will help you get started with contributing code, documentation, examples, and more.

---

## Table of Contents
- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Submitting Changes](#submitting-changes)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community Guidelines](#community-guidelines)

---

## Getting Started

### Before You Begin

1. **Read the documentation** - Familiarize yourself with the project structure and existing functions
2. **Check existing issues** - Look for open issues or feature requests
3. **Start small** - Consider beginning with documentation improvements or bug fixes
4. **Ask questions** - Don't hesitate to ask for clarification or help

### Ways to Contribute

- 🐛 **Report bugs**
- 💡 **Suggest new features**
- 📝 **Improve documentation** 
- 🔧 **Fix issues**
- ✨ **Add new functions**
- 🧪 **Write tests**
- 💬 **Help other contributors**

---

## Types of Contributions

### Bug Reports

When reporting bugs, please include:

- **Clear description** of the issue
- **Steps to reproduce** the problem
- **Expected vs actual behavior**
- **Python version** and operating system
- **Code sample** that demonstrates the issue

**Bug Report Template:**
```markdown
**Bug Description:**
A clear description of the bug.

**Steps to Reproduce:**
1. Go to '...'
2. Run function '...'
3. See error

**Expected Behavior:**
What should happen.

**Actual Behavior:**
What actually happens.

**Environment:**
- Python version: 3.x.x
- Operating System: [Windows/macOS/Linux]
- Project version: [if applicable]

**Code Sample:**
```python
# Minimal code that reproduces the issue
```

### Feature Requests

For new features, please provide:

- **Clear description** of the proposed feature
- **Use cases** and benefits
- **Possible implementation** ideas
- **Examples** of how it would be used

**Feature Request Template:**
```markdown
**Feature Description:**
Clear description of the proposed feature.

**Use Case:**
Explain why this feature would be useful.

**Proposed Implementation:**
Ideas for how this could be implemented.

**Examples:**
```python
# Example usage of the proposed feature
```

### Code Contributions

Before writing code:

1. **Open an issue** to discuss the change
2. **Fork the repository**
3. **Create a feature branch**
4. **Follow coding standards**
5. **Write tests** for new functionality
6. **Update documentation**

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/yourusername/py-101.git
cd py-101
```

### 2. Set Up Development Environment

```bash
# Create virtual environment (optional but recommended)
python -m venv py101_dev
source py101_dev/bin/activate  # On Windows: py101_dev\Scripts\activate

# The project uses only standard library, no additional packages needed
```

### 3. Verify Setup

```bash
# Run main script to ensure everything works
python main.py

# Run tests
python tests/test_functions.py
```

### 4. Configure Git

```bash
# Add upstream remote
git remote add upstream https://github.com/original-owner/py-101.git

# Configure your name and email
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

---

## Code Style Guidelines

### Python Style Standards

We follow **PEP 8** with some specific guidelines:

#### General Guidelines

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Maximum 79 characters
- **Encoding**: UTF-8
- **Imports**: Standard library first, then third-party, then local

#### Naming Conventions

```python
# Functions and variables: snake_case
def calculate_factorial(number):
    result_value = 1
    return result_value

# Constants: UPPER_CASE
MAX_RECURSION_DEPTH = 1000

# Classes: PascalCase (when needed)
class TextProcessor:
    pass
```

#### Function Documentation

All functions must have docstrings:

```python
def fibonacci_sequence(length):
    """
    Generate a Fibonacci sequence of specified length.
    
    Args:
        length (int): Length of sequence to generate
        
    Returns:
        list: List containing Fibonacci sequence
        
    Raises:
        ValueError: If length is negative
        
    Example:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
    """
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    # Implementation here
    pass
```

#### Error Handling

- Use specific exception types
- Provide meaningful error messages
- Handle edge cases appropriately

```python
def factorial(n):
    """Calculate factorial with proper error handling."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Implementation here
```

#### Type Hints (Recommended)

```python
from typing import List, Optional

def process_list(items: List[int], reverse: bool = False) -> List[int]:
    """Process a list of integers."""
    if reverse:
        return sorted(items, reverse=True)
    return sorted(items)
```

### Code Organization

#### File Structure

- **main.py**: Core demonstration functions
- **utils/**: Utility modules organized by functionality
- **examples/**: Usage examples
- **tests/**: Test files
- **docs/**: Documentation files

#### Module Organization

```python
# utils/new_module.py

"""
Brief module description.

This module provides functions for [specific purpose].
"""

# Imports
import os
import sys
from typing import List, Optional

# Constants
DEFAULT_VALUE = 42

# Functions
def primary_function():
    """Primary function with clear purpose."""
    pass

def helper_function():
    """Helper function for internal use.""" 
    pass
```

---

## Submitting Changes

### 1. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/add-new-function

# Or for bug fixes:
git checkout -b bugfix/fix-calculation-error
```

### 2. Make Your Changes

- Write clean, well-documented code
- Follow the style guidelines
- Add or update tests
- Update documentation

### 3. Test Your Changes

```bash
# Run all tests
python tests/test_functions.py

# Test your specific changes
python -c "from utils.your_module import your_function; print(your_function())"

# Run main demonstration
python main.py
```

### 4. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add new string manipulation function

- Add reverse_words function to string_utils.py
- Include comprehensive docstring and type hints
- Add tests for edge cases
- Update examples and documentation"
```

#### Commit Message Guidelines

- **Use imperative mood** ("Add feature" not "Added feature")
- **Capitalize first line** 
- **Keep first line under 50 characters**
- **Include detailed description** if needed

Good commit messages:
```
Add factorial function with error handling
Fix bug in prime number detection
Update documentation for string utilities
Refactor data structure helpers for clarity
```

### 5. Push Changes

```bash
# Push to your fork
git push origin feature/add-new-function
```

### 6. Create Pull Request

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill out the pull request template
4. Submit the pull request

#### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Other (please specify)

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Documentation
- [ ] Documentation updated
- [ ] Examples added/updated
- [ ] Docstrings added/updated

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] No breaking changes (or clearly documented)
```

---

## Testing

### Writing Tests

Create tests for new functions:

```python
# tests/test_new_feature.py

def test_new_function():
    """Test the new function with various inputs."""
    from utils.new_module import new_function
    
    # Test normal case
    assert new_function(5) == expected_result
    
    # Test edge cases
    assert new_function(0) == expected_edge_result
    assert new_function(-1) == expected_negative_result
    
    # Test error cases
    try:
        new_function("invalid")
        assert False, "Should have raised TypeError"
    except TypeError:
        pass  # Expected
```

### Test Categories

- **Unit tests**: Test individual functions
- **Integration tests**: Test function combinations
- **Edge case tests**: Test boundary conditions
- **Error tests**: Test exception handling

### Running Tests

```bash
# Run all tests
python tests/test_functions.py

# Run specific test file
python tests/test_new_feature.py

# Run with verbose output
python -m pytest tests/ -v  # If pytest is available
```

---

## Documentation

### Documentation Standards

All contributions should include appropriate documentation:

#### Function Documentation

- **Docstrings** for all functions
- **Type hints** where appropriate
- **Usage examples** in docstrings
- **Parameter descriptions**
- **Return value descriptions**
- **Exception descriptions**

#### File Documentation

- **Module docstrings** at the top of files
- **Clear comments** for complex logic
- **TODO comments** for future improvements

#### Example Documentation

```python
def complex_calculation(data: List[int], threshold: float = 0.5) -> dict:
    """
    Perform complex calculation on numerical data.
    
    This function analyzes a list of integers and returns statistics
    based on the provided threshold value.
    
    Args:
        data: List of integers to analyze
        threshold: Threshold value for filtering (default: 0.5)
        
    Returns:
        dict: Dictionary containing:
            - 'mean': Average value
            - 'filtered': Values above threshold
            - 'count': Number of filtered values
            
    Raises:
        ValueError: If data is empty
        TypeError: If data contains non-integers
        
    Example:
        >>> data = [1, 2, 3, 4, 5]
        >>> result = complex_calculation(data, 2.5)
        >>> print(result['filtered'])
        [3, 4, 5]
    """
    # Implementation here
    pass
```

### Updating Documentation

When adding new features:

1. **Update API.md** with function details
2. **Add examples** to EXAMPLES.md
3. **Update README.md** if necessary
4. **Add to appropriate utility documentation**

---

## Community Guidelines

### Code of Conduct

- **Be respectful** and inclusive
- **Help others** learn and grow
- **Provide constructive** feedback
- **Focus on the code**, not the person
- **Be patient** with newcomers

### Communication

- **Use clear, descriptive** language
- **Ask questions** when unsure
- **Share knowledge** and experiences
- **Be open** to feedback and suggestions

### Review Process

When reviewing pull requests:

- **Check functionality** - does it work as intended?
- **Review code quality** - is it clean and readable?
- **Test edge cases** - are they handled properly?
- **Verify documentation** - is it complete and accurate?
- **Suggest improvements** constructively

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Pull Request Comments**: For code-specific discussions
- **README**: For general project information
- **Documentation**: For usage and API details

---

## Development Workflow

### Typical Contribution Workflow

1. **Find or create issue** to work on
2. **Fork repository** and create branch
3. **Implement changes** following guidelines
4. **Write tests** for new functionality
5. **Update documentation** as needed
6. **Test thoroughly** before submitting
7. **Create pull request** with clear description
8. **Respond to feedback** and make improvements
9. **Merge approved** changes

### Release Process

The project follows semantic versioning:

- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes, backward compatible

---

## Recognition

Contributors will be recognized in:

- **README.md** contributor section
- **CHANGELOG.md** for significant contributions
- **GitHub contributors** page

---

## Questions?

If you have questions about contributing:

1. Check existing **documentation** and **issues**
2. **Search** for similar questions
3. **Create an issue** with the "question" label
4. Be **specific** about what you need help with

---

Thank you for contributing to Python 101! Your efforts help make this a better learning resource for everyone. 🐍✨

**Happy Contributing!**
