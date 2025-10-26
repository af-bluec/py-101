"""
Python Pathlib Demonstration

This module showcases the pathlib module for modern path handling:
- Path objects and operations
- Cross-platform path handling
- File and directory operations
- Path properties and methods
- Pattern matching and globbing
- File system navigation
- Temporary file handling

The pathlib module provides object-oriented filesystem paths that are
more intuitive and powerful than traditional string-based paths.
"""

from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath
import os
import tempfile
import shutil
from typing import Iterator, List
import stat
import time


def demonstrate_path_creation():
    """Demonstrate different ways to create Path objects."""
    print("=== Path Creation Demo ===")
    
    # Current working directory
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Home directory
    home_dir = Path.home()
    print(f"Home directory: {home_dir}")
    
    # Create path from string
    path_from_string = Path("/usr/local/bin")
    print(f"Path from string: {path_from_string}")
    
    # Join path parts
    joined_path = Path("home") / "user" / "documents" / "file.txt"
    print(f"Joined path: {joined_path}")
    
    # Platform-specific paths
    posix_path = PurePosixPath("/usr/local/bin")
    windows_path = PureWindowsPath(r"C:\Program Files\Python")
    
    print(f"Posix path: {posix_path}")
    print(f"Windows path: {windows_path}")
    
    # Relative paths
    relative_path = Path("../parent/file.txt")
    print(f"Relative path: {relative_path}")
    
    # Resolve to absolute path
    try:
        absolute_path = relative_path.resolve()
        print(f"Resolved absolute path: {absolute_path}")
    except Exception as e:
        print(f"Could not resolve path: {e}")


def demonstrate_path_properties():
    """Demonstrate path properties and attributes."""
    print("\n=== Path Properties Demo ===")
    
    # Create a sample path
    sample_path = Path("/home/user/documents/project/script.py")
    print(f"Sample path: {sample_path}")
    
    # Path components
    print(f"Parts: {sample_path.parts}")
    print(f"Name: {sample_path.name}")
    print(f"Stem: {sample_path.stem}")
    print(f"Suffix: {sample_path.suffix}")
    print(f"Suffixes: {sample_path.suffixes}")
    print(f"Parent: {sample_path.parent}")
    print(f"Parents: {list(sample_path.parents)}")
    print(f"Anchor: {sample_path.anchor}")
    
    # Path with multiple extensions
    complex_path = Path("archive.tar.gz")
    print(f"\nComplex filename: {complex_path}")
    print(f"Name: {complex_path.name}")
    print(f"Stem: {complex_path.stem}")
    print(f"Suffix: {complex_path.suffix}")
    print(f"Suffixes: {complex_path.suffixes}")
    
    # Path methods
    print(f"\nPath methods:")
    print(f"Is absolute: {sample_path.is_absolute()}")
    print(f"Is relative to /home: {sample_path.is_relative_to('/home') if hasattr(sample_path, 'is_relative_to') else 'N/A'}")


def demonstrate_path_operations():
    """Demonstrate path operations and manipulations."""
    print("\n=== Path Operations Demo ===")
    
    # Create temporary directory for demonstrations
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        print(f"Working in temporary directory: {temp_path}")
        
        # Create directories
        project_dir = temp_path / "my_project"
        src_dir = project_dir / "src"
        docs_dir = project_dir / "docs"
        
        # Create directory structure
        src_dir.mkdir(parents=True)
        docs_dir.mkdir()
        
        print(f"Created directories:")
        print(f"  {project_dir}")
        print(f"  {src_dir}")
        print(f"  {docs_dir}")
        
        # Create files
        files_to_create = [
            src_dir / "main.py",
            src_dir / "utils.py",
            docs_dir / "README.md",
            project_dir / "requirements.txt"
        ]
        
        for file_path in files_to_create:
            file_path.write_text(f"# Content of {file_path.name}\n")
            print(f"Created file: {file_path}")
        
        # Path joining and manipulation
        config_file = project_dir / "config" / "settings.json"
        config_file.parent.mkdir(exist_ok=True)
        config_file.write_text('{"debug": true}')
        
        # Change file extensions
        backup_file = config_file.with_suffix('.bak')
        config_file.rename(backup_file)
        print(f"Renamed {config_file.name} to {backup_file.name}")
        
        # Change file name
        new_config = backup_file.with_name('app_config.json')
        backup_file.rename(new_config)
        print(f"Renamed to {new_config.name}")
        
        # Demonstrate file operations
        demonstrate_file_operations(temp_path)
        
        # Demonstrate directory traversal
        demonstrate_directory_traversal(project_dir)


def demonstrate_file_operations(base_path: Path):
    """Demonstrate file-specific operations."""
    print(f"\n--- File Operations ---")
    
    # Create a test file
    test_file = base_path / "test_file.txt"
    test_file.write_text("Hello, World!\nThis is a test file.\n")
    
    # File properties
    if test_file.exists():
        print(f"File exists: {test_file}")
        print(f"Is file: {test_file.is_file()}")
        print(f"Is directory: {test_file.is_dir()}")
        print(f"File size: {test_file.stat().st_size} bytes")
        
        # Read file content
        content = test_file.read_text()
        print(f"File content:\n{content}")
        
        # Append to file
        test_file.write_text(content + "Appended line.\n")
        
        # File statistics
        stat_info = test_file.stat()
        print(f"File mode: {stat.filemode(stat_info.st_mode)}")
        print(f"Last modified: {time.ctime(stat_info.st_mtime)}")
    
    # Binary file operations
    binary_file = base_path / "binary_test.dat"
    binary_data = b"Binary content: \x00\x01\x02\x03"
    binary_file.write_bytes(binary_data)
    
    read_binary = binary_file.read_bytes()
    print(f"Binary file written and read: {read_binary}")


def demonstrate_directory_traversal(root_path: Path):
    """Demonstrate directory traversal and pattern matching."""
    print(f"\n--- Directory Traversal ---")
    
    print(f"Contents of {root_path}:")
    
    # List immediate children
    for item in root_path.iterdir():
        if item.is_file():
            print(f"  📄 {item.name}")
        elif item.is_dir():
            print(f"  📁 {item.name}/")
    
    # Recursive traversal
    print(f"\nRecursive traversal:")
    for item in root_path.rglob("*"):
        indent = "  " * (len(item.relative_to(root_path).parts) - 1)
        if item.is_file():
            print(f"{indent}📄 {item.name}")
        elif item.is_dir():
            print(f"{indent}📁 {item.name}/")
    
    # Pattern matching
    print(f"\nPython files:")
    for py_file in root_path.rglob("*.py"):
        print(f"  {py_file}")
    
    print(f"\nAll text files:")
    for text_file in root_path.rglob("*.{txt,md}"):
        print(f"  {text_file}")


def demonstrate_path_matching():
    """Demonstrate path pattern matching."""
    print("\n=== Path Matching Demo ===")
    
    # Sample paths
    paths = [
        Path("src/main.py"),
        Path("src/utils.py"),
        Path("tests/test_main.py"),
        Path("docs/README.md"),
        Path("config/settings.json"),
        Path("data/sample.csv"),
        Path("scripts/backup.sh")
    ]
    
    print("Sample paths:")
    for path in paths:
        print(f"  {path}")
    
    # Match patterns
    patterns = [
        "*.py",
        "src/*.py",
        "**/test_*.py",
        "*.{py,md}",
        "**/README.*"
    ]
    
    for pattern in patterns:
        print(f"\nMatching pattern '{pattern}':")
        matching_paths = [p for p in paths if p.match(pattern)]
        for path in matching_paths:
            print(f"  ✓ {path}")


def demonstrate_path_utilities():
    """Demonstrate utility functions with paths."""
    print("\n=== Path Utilities Demo ===")
    
    # Create temporary workspace
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create some test files
        test_files = [
            temp_path / "document.txt",
            temp_path / "image.jpg",
            temp_path / "script.py",
            temp_path / "data.csv"
        ]
        
        for file_path in test_files:
            file_path.write_text(f"Content of {file_path.name}")
        
        # Group files by extension
        files_by_ext = {}
        for file_path in temp_path.iterdir():
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext not in files_by_ext:
                    files_by_ext[ext] = []
                files_by_ext[ext].append(file_path)
        
        print("Files grouped by extension:")
        for ext, files in files_by_ext.items():
            print(f"  {ext or '(no extension)'}: {[f.name for f in files]}")
        
        # Find largest file
        largest_file = max(temp_path.iterdir(), key=lambda p: p.stat().st_size if p.is_file() else 0)
        if largest_file.is_file():
            print(f"Largest file: {largest_file.name} ({largest_file.stat().st_size} bytes)")
        
        # Create backup directory structure
        backup_dir = temp_path / "backup"
        backup_dir.mkdir()
        
        for file_path in test_files:
            backup_file = backup_dir / f"{file_path.stem}_backup{file_path.suffix}"
            shutil.copy2(file_path, backup_file)
            print(f"Backed up {file_path.name} to {backup_file.name}")


def demonstrate_cross_platform_paths():
    """Demonstrate cross-platform path handling."""
    print("\n=== Cross-Platform Paths Demo ===")
    
    # Current platform
    current_platform = os.name
    print(f"Current platform: {current_platform}")
    
    # Path separators
    print(f"Path separator: {os.sep!r}")
    print(f"Alternative separator: {os.altsep!r}")
    
    # Pure paths (no filesystem access)
    unix_style = PurePosixPath("/home/user/file.txt")
    windows_style = PureWindowsPath(r"C:\Users\User\file.txt")
    
    print(f"Unix-style path: {unix_style}")
    print(f"Windows-style path: {windows_style}")
    
    # Converting between styles
    print(f"Unix parts: {unix_style.parts}")
    print(f"Windows parts: {windows_style.parts}")
    
    # Path operations work regardless of current platform
    generic_path = Path("documents") / "projects" / "python" / "script.py"
    print(f"Generic path: {generic_path}")
    print(f"As POSIX: {generic_path.as_posix()}")
    
    # URI conversion
    file_uri = generic_path.as_uri() if hasattr(generic_path, 'as_uri') else f"file://{generic_path.as_posix()}"
    print(f"As URI: {file_uri}")


if __name__ == "__main__":
    print("=== Python Pathlib Demo ===")
    
    demonstrate_path_creation()
    demonstrate_path_properties()
    demonstrate_path_operations()
    demonstrate_path_matching()
    demonstrate_path_utilities()
    demonstrate_cross_platform_paths()
    
    print("\n=== Pathlib Demo Complete ===")
