"""
Regular Expressions in Python
Demonstrates pattern matching, text processing, and regex operations
"""

import re
from typing import List, Optional


def basic_patterns():
    """Basic regex pattern matching"""
    print("=" * 60)
    print("BASIC PATTERN MATCHING")
    print("=" * 60)
    
    text = "The quick brown fox jumps over the lazy dog"
    
    # Simple search
    match = re.search(r"fox", text)
    if match:
        print(f"Found 'fox' at position {match.start()}-{match.end()}")
    
    # Case-insensitive search
    match = re.search(r"QUICK", text, re.IGNORECASE)
    if match:
        print(f"Found (case-insensitive): {match.group()}")
    
    # Match at beginning
    if re.match(r"The", text):
        print("Text starts with 'The'")
    
    # Full string match
    if re.fullmatch(r".*dog", text):
        print("Text ends with 'dog'")
    
    print()


def character_classes():
    """Character classes and special sequences"""
    print("=" * 60)
    print("CHARACTER CLASSES")
    print("=" * 60)
    
    # Digits
    text = "Order #12345 placed on 2024-10-30"
    digits = re.findall(r"\d+", text)
    print(f"Digits found: {digits}")
    
    # Words
    words = re.findall(r"\w+", text)
    print(f"Words found: {words}")
    
    # Whitespace
    spaces = re.findall(r"\s+", text)
    print(f"Whitespace count: {len(spaces)}")
    
    # Custom character class
    vowels = re.findall(r"[aeiou]", text, re.IGNORECASE)
    print(f"Vowels found: {len(vowels)} - {vowels[:10]}...")
    
    print()


def quantifiers():
    """Quantifiers: *, +, ?, {n,m}"""
    print("=" * 60)
    print("QUANTIFIERS")
    print("=" * 60)
    
    # Zero or more (*)
    text = "color colour colouur"
    matches = re.findall(r"colou*r", text)
    print(f"colou*r matches: {matches}")
    
    # One or more (+)
    text = "goooooal goal gal"
    matches = re.findall(r"go+al", text)
    print(f"go+al matches: {matches}")
    
    # Zero or one (?)
    text = "color colour"
    matches = re.findall(r"colou?r", text)
    print(f"colou?r matches: {matches}")
    
    # Specific count {n,m}
    text = "1234 12 123456 12345"
    matches = re.findall(r"\d{4,5}", text)
    print(f"4-5 digit numbers: {matches}")
    
    print()


def groups_and_capturing():
    """Groups and capturing patterns"""
    print("=" * 60)
    print("GROUPS AND CAPTURING")
    print("=" * 60)
    
    # Basic groups
    text = "John Doe (john@example.com)"
    match = re.search(r"(\w+)\s+(\w+)\s+\(([^)]+)\)", text)
    if match:
        print(f"First name: {match.group(1)}")
        print(f"Last name: {match.group(2)}")
        print(f"Email: {match.group(3)}")
        print(f"All groups: {match.groups()}")
    
    # Named groups
    pattern = r"(?P<first>\w+)\s+(?P<last>\w+)"
    match = re.search(pattern, text)
    if match:
        print(f"Named groups: {match.groupdict()}")
    
    # Non-capturing groups
    text = "http://example.com https://secure.com"
    matches = re.findall(r"(?:http|https)://(\w+\.\w+)", text)
    print(f"Domains: {matches}")
    
    print()


def email_validation():
    """Email validation with regex"""
    print("=" * 60)
    print("EMAIL VALIDATION")
    print("=" * 60)
    
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    emails = [
        "user@example.com",
        "john.doe@company.co.uk",
        "invalid@",
        "@invalid.com",
        "valid_email@test.org"
    ]
    
    for email in emails:
        is_valid = bool(re.match(email_pattern, email))
        status = "✓" if is_valid else "✗"
        print(f"{status} {email}")
    
    print()


def phone_number_extraction():
    """Extract and format phone numbers"""
    print("=" * 60)
    print("PHONE NUMBER EXTRACTION")
    print("=" * 60)
    
    text = """
    Contact us at:
    (555) 123-4567
    555-987-6543
    555.456.7890
    +1-555-111-2222
    """
    
    # Pattern for various phone formats
    pattern = r"(?:\+1[-.]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}"
    phones = re.findall(pattern, text)
    
    print("Phone numbers found:")
    for phone in phones:
        print(f"  {phone.strip()}")
    
    print()


def substitution():
    """Text substitution with re.sub()"""
    print("=" * 60)
    print("TEXT SUBSTITUTION")
    print("=" * 60)
    
    # Simple substitution
    text = "The color of the car is red"
    result = re.sub(r"color", "colour", text)
    print(f"Original: {text}")
    print(f"Modified: {result}")
    
    # Case-insensitive substitution
    text = "Python is great. PYTHON is powerful."
    result = re.sub(r"python", "Python3", text, flags=re.IGNORECASE)
    print(f"\nCase-insensitive: {result}")
    
    # Substitution with function
    def uppercase_match(match):
        return match.group(0).upper()
    
    text = "hello world"
    result = re.sub(r"\b\w+\b", uppercase_match, text)
    print(f"Function substitution: {result}")
    
    # Backreferences
    text = "2024-10-30"
    result = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", text)
    print(f"Date format change: {result}")
    
    print()


def splitting():
    """Split strings with regex"""
    print("=" * 60)
    print("SPLITTING WITH REGEX")
    print("=" * 60)
    
    # Split on multiple delimiters
    text = "apple,banana;cherry:date|elderberry"
    parts = re.split(r"[,;:|]", text)
    print(f"Split on multiple delimiters: {parts}")
    
    # Split on whitespace (multiple spaces)
    text = "one  two   three    four"
    parts = re.split(r"\s+", text)
    print(f"Split on whitespace: {parts}")
    
    # Split with capturing groups
    text = "a1b2c3d4"
    parts = re.split(r"(\d)", text)
    print(f"Split with capture: {parts}")
    
    print()


def lookahead_lookbehind():
    """Lookahead and lookbehind assertions"""
    print("=" * 60)
    print("LOOKAHEAD AND LOOKBEHIND")
    print("=" * 60)
    
    # Positive lookahead
    text = "Python3 Java8 C++11"
    matches = re.findall(r"\w+(?=\d)", text)
    print(f"Words followed by digits: {matches}")
    
    # Negative lookahead
    text = "Python Java C++"
    matches = re.findall(r"\w+(?!\d)", text)
    print(f"Words NOT followed by digits: {matches}")
    
    # Positive lookbehind
    text = "$100 €200 £300"
    matches = re.findall(r"(?<=\$)\d+", text)
    print(f"Numbers after $: {matches}")
    
    # Negative lookbehind
    text = "100 $200 300"
    matches = re.findall(r"(?<!\$)\b\d+", text)
    print(f"Numbers NOT after $: {matches}")
    
    print()


def url_parser():
    """Parse URLs with regex"""
    print("=" * 60)
    print("URL PARSING")
    print("=" * 60)
    
    url_pattern = r"(?P<protocol>https?://)?(?P<domain>[\w.-]+)(?P<path>/[\w/.-]*)?(?P<query>\?[\w=&]*)?"
    
    urls = [
        "https://www.example.com/path/to/page?id=123",
        "http://test.org",
        "example.com/about",
    ]
    
    for url in urls:
        match = re.search(url_pattern, url)
        if match:
            print(f"\nURL: {url}")
            print(f"  Protocol: {match.group('protocol') or 'N/A'}")
            print(f"  Domain: {match.group('domain')}")
            print(f"  Path: {match.group('path') or '/'}")
            print(f"  Query: {match.group('query') or 'N/A'}")
    
    print()


def compiled_patterns():
    """Compiled regex patterns for performance"""
    print("=" * 60)
    print("COMPILED PATTERNS")
    print("=" * 60)
    
    # Compile pattern once, use multiple times
    email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    
    text = "Contact: john@example.com or jane@test.org for more info"
    emails = email_regex.findall(text)
    print(f"Emails found: {emails}")
    
    # Compiled pattern with flags
    word_regex = re.compile(r"\bpython\b", re.IGNORECASE)
    text = "Python is great. I love PYTHON and python3"
    matches = word_regex.findall(text)
    print(f"'Python' occurrences: {len(matches)}")
    
    print()


def practical_examples():
    """Practical real-world examples"""
    print("=" * 60)
    print("PRACTICAL EXAMPLES")
    print("=" * 60)
    
    # Extract hashtags
    text = "Learning #Python and #RegEx is fun! #coding #100DaysOfCode"
    hashtags = re.findall(r"#\w+", text)
    print(f"Hashtags: {hashtags}")
    
    # Extract mentions
    text = "Thanks @john and @jane_doe for the help!"
    mentions = re.findall(r"@\w+", text)
    print(f"Mentions: {mentions}")
    
    # Clean HTML tags
    html = "<p>This is <b>bold</b> and <i>italic</i> text</p>"
    clean = re.sub(r"<[^>]+>", "", html)
    print(f"Clean text: {clean}")
    
    # Validate password strength
    password = "MyP@ssw0rd123"
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    is_long = len(password) >= 8
    
    print(f"\nPassword strength for '{password}':")
    print(f"  Has uppercase: {has_upper}")
    print(f"  Has lowercase: {has_lower}")
    print(f"  Has digit: {has_digit}")
    print(f"  Has special char: {has_special}")
    print(f"  Length >= 8: {is_long}")
    print(f"  Strong: {all([has_upper, has_lower, has_digit, has_special, is_long])}")
    
    print()


def main():
    """Run all regex demonstrations"""
    print("\n" + "=" * 60)
    print("PYTHON REGULAR EXPRESSIONS SHOWCASE")
    print("=" * 60 + "\n")
    
    basic_patterns()
    character_classes()
    quantifiers()
    groups_and_capturing()
    email_validation()
    phone_number_extraction()
    substitution()
    splitting()
    lookahead_lookbehind()
    url_parser()
    compiled_patterns()
    practical_examples()
    
    print("=" * 60)
    print("Regular expressions demonstration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
