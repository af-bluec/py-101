"""
String utilities examples.

This file demonstrates usage of various string manipulation functions.
"""

from utils.string_utils import (
    clean_text, is_palindrome, count_words, capitalize_words,
    reverse_string, remove_vowels, extract_numbers, word_frequency,
    longest_word, truncate_text, snake_case_to_camel_case,
    camel_case_to_snake_case, is_email_format, extract_emails
)


def run_string_examples():
    """Run examples of string utility functions."""
    
    print("=== STRING UTILITY EXAMPLES ===\n")
    
    # Text cleaning examples
    print("1. Text Cleaning:")
    messy_text = "   Hello    World   from   Python!   "
    clean = clean_text(messy_text)
    print(f"Original: '{messy_text}'")
    print(f"Cleaned:  '{clean}'\n")
    
    # Palindrome checking
    print("2. Palindrome Checking:")
    test_strings = ["racecar", "A man a plan a canal Panama", "hello", "Madam"]
    for text in test_strings:
        is_palin = is_palindrome(text)
        print(f"'{text}' -> {is_palin}")
    print()
    
    # Word counting
    print("3. Word Counting:")
    sample_text = "The quick brown fox jumps over the lazy dog"
    word_count = count_words(sample_text)
    print(f"Text: '{sample_text}'")
    print(f"Word count: {word_count}\n")
    
    # Text transformation
    print("4. Text Transformation:")
    original = "hello world from python programming"
    print(f"Original: {original}")
    print(f"Capitalized: {capitalize_words(original)}")
    print(f"Reversed: {reverse_string(original)}")
    print(f"No vowels: {remove_vowels(original)}\n")
    
    # Number extraction
    print("5. Number Extraction:")
    text_with_numbers = "I have 5 cats, 10 dogs, and 100 fish in my aquarium"
    numbers = extract_numbers(text_with_numbers)
    print(f"Text: {text_with_numbers}")
    print(f"Numbers found: {numbers}\n")
    
    # Word frequency analysis
    print("6. Word Frequency Analysis:")
    repeated_text = "hello world hello python world programming python hello"
    frequency = word_frequency(repeated_text)
    print(f"Text: {repeated_text}")
    print("Word frequencies:")
    for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word}: {count}")
    print()
    
    # Finding longest word
    print("7. Finding Longest Word:")
    sentence = "The extraordinarily sophisticated algorithm"
    longest = longest_word(sentence)
    print(f"Sentence: {sentence}")
    print(f"Longest word: '{longest}'\n")
    
    # Text truncation
    print("8. Text Truncation:")
    long_text = "This is a very long sentence that needs to be truncated"
    truncated = truncate_text(long_text, 20)
    print(f"Original: {long_text}")
    print(f"Truncated: {truncated}\n")
    
    # Case conversions
    print("9. Case Conversions:")
    snake_case = "hello_world_example_function"
    camel_case = "helloWorldExampleFunction"
    
    print(f"Snake to Camel: {snake_case} -> {snake_case_to_camel_case(snake_case)}")
    print(f"Camel to Snake: {camel_case} -> {camel_case_to_snake_case(camel_case)}\n")
    
    # Email validation and extraction
    print("10. Email Processing:")
    email_text = "Contact us at info@company.com or support@example.org for help"
    emails = extract_emails(email_text)
    print(f"Text: {email_text}")
    print(f"Emails found: {emails}")
    
    for email in emails:
        is_valid = is_email_format(email)
        print(f"  {email} -> Valid: {is_valid}")
    print()


if __name__ == "__main__":
    run_string_examples()
