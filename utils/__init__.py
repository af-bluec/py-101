"""
Utility modules for common operations.
"""

from .math_utils import (
    factorial, 
    is_prime, 
    fibonacci_sequence, 
    gcd, 
    lcm
)

from .string_utils import (
    greet,
    format_person_info,
    analyze_text,
    reverse_words,
    capitalize_words,
    remove_duplicates
)

from .data_structures import (
    demonstrate_lists,
    demonstrate_sets,
    demonstrate_dictionaries,
    demonstrate_tuples,
    demonstrate_advanced_operations,
    create_nested_structure
)

__all__ = [
    # Math utilities
    'factorial', 'is_prime', 'fibonacci_sequence', 'gcd', 'lcm',
    # String utilities  
    'greet', 'format_person_info', 'analyze_text', 'reverse_words',
    'capitalize_words', 'remove_duplicates',
    # Data structure utilities
    'demonstrate_lists', 'demonstrate_sets', 'demonstrate_dictionaries',
    'demonstrate_tuples', 'demonstrate_advanced_operations', 'create_nested_structure'
]
