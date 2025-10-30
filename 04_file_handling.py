"""
Demonstration of file handling in Python.
Covers reading, writing, and working with different file formats.
"""

import json
import csv
from pathlib import Path


def demonstrate_text_files():
    """Working with text files."""
    print("=== TEXT FILE OPERATIONS ===")
    
    # Writing to a file
    filename = "sample.txt"
    with open(filename, "w") as f:
        f.write("Hello, World!\n")
        f.write("This is a sample text file.\n")
        f.write("Python makes file handling easy.\n")
    print(f"Created {filename}")
    
    # Reading entire file
    with open(filename, "r") as f:
        content = f.read()
    print(f"Content:\n{content}")
    
    # Reading line by line
    with open(filename, "r") as f:
        lines = f.readlines()
    print(f"Number of lines: {len(lines)}")
    
    # Appending to file
    with open(filename, "a") as f:
        f.write("This line was appended.\n")
    print("Appended new line")
    
    # Reading with iteration
    print("\nReading line by line:")
    with open(filename, "r") as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")


def demonstrate_json():
    """Working with JSON files."""
    print("\n=== JSON FILE OPERATIONS ===")
    
    # Data to save
    data = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "JavaScript", "SQL"],
        "address": {
            "city": "New York",
            "country": "USA"
        }
    }
    
    # Writing JSON
    json_file = "data.json"
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Created {json_file}")
    
    # Reading JSON
    with open(json_file, "r") as f:
        loaded_data = json.load(f)
    print(f"Loaded data: {loaded_data}")
    
    # JSON string operations
    json_string = json.dumps(data, indent=2)
    print(f"\nJSON string:\n{json_string}")


def demonstrate_csv():
    """Working with CSV files."""
    print("\n=== CSV FILE OPERATIONS ===")
    
    # Writing CSV
    csv_file = "students.csv"
    students = [
        ["Name", "Age", "Grade"],
        ["Alice", 20, "A"],
        ["Bob", 21, "B"],
        ["Charlie", 19, "A"],
        ["Diana", 22, "B+"]
    ]
    
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)
    print(f"Created {csv_file}")
    
    # Reading CSV
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        print("\nCSV Content:")
        for row in reader:
            print(", ".join(row))
    
    # Using DictReader
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        print("\nUsing DictReader:")
        for row in reader:
            print(f"{row['Name']}: Grade {row['Grade']}")


def demonstrate_pathlib():
    """Using pathlib for file operations."""
    print("\n=== PATHLIB OPERATIONS ===")
    
    # Create a Path object
    path = Path("sample.txt")
    print(f"File exists: {path.exists()}")
    print(f"Is file: {path.is_file()}")
    print(f"File name: {path.name}")
    print(f"File suffix: {path.suffix}")
    print(f"Absolute path: {path.absolute()}")
    
    # Reading with pathlib
    if path.exists():
        content = path.read_text()
        print(f"\nFirst 50 characters: {content[:50]}...")
    
    # Writing with pathlib
    new_file = Path("pathlib_example.txt")
    new_file.write_text("Created using pathlib!")
    print(f"\nCreated {new_file}")
    
    # List files in directory
    current_dir = Path(".")
    print("\nPython files in current directory:")
    for py_file in current_dir.glob("*.py"):
        print(f"  - {py_file.name}")


def demonstrate_context_manager():
    """Demonstrating context managers for file handling."""
    print("\n=== CONTEXT MANAGERS ===")
    
    # Multiple files with context manager
    with open("input.txt", "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
    
    print("Processed input.txt -> output.txt (uppercase)")
    
    # Reading the result
    with open("output.txt", "r") as f:
        print(f"Output content:\n{f.read()}")


def cleanup_files():
    """Clean up created files."""
    files_to_remove = [
        "sample.txt", "data.json", "students.csv",
        "pathlib_example.txt", "input.txt", "output.txt"
    ]
    
    for filename in files_to_remove:
        path = Path(filename)
        if path.exists():
            path.unlink()
    
    print("\n=== CLEANUP ===")
    print("Removed all created files")


def main():
    try:
        demonstrate_text_files()
        demonstrate_json()
        demonstrate_csv()
        demonstrate_pathlib()
        demonstrate_context_manager()
    finally:
        cleanup_files()


if __name__ == "__main__":
    main()
