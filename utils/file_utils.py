"""
File handling utility functions.

This module provides utilities for file operations including reading, writing,
path manipulation, and file system operations.
"""

import os
import json
import csv
from typing import List, Dict, Any, Optional, Union
from pathlib import Path


def read_text_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read entire text file content.
    
    Args:
        file_path (str): Path to file
        encoding (str): File encoding
        
    Returns:
        str: File content
        
    Example:
        >>> content = read_text_file("example.txt")
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {e}")


def write_text_file(file_path: str, content: str, encoding: str = 'utf-8', append: bool = False) -> bool:
    """
    Write content to text file.
    
    Args:
        file_path (str): Path to file
        content (str): Content to write
        encoding (str): File encoding
        append (bool): Whether to append or overwrite
        
    Returns:
        bool: True if successful
        
    Example:
        >>> write_text_file("output.txt", "Hello World!")
    """
    try:
        mode = 'a' if append else 'w'
        with open(file_path, mode, encoding=encoding) as file:
            file.write(content)
        return True
    except Exception as e:
        raise Exception(f"Error writing to file {file_path}: {e}")


def read_lines(file_path: str, encoding: str = 'utf-8', strip_whitespace: bool = True) -> List[str]:
    """
    Read file lines into a list.
    
    Args:
        file_path (str): Path to file
        encoding (str): File encoding
        strip_whitespace (bool): Whether to strip whitespace from lines
        
    Returns:
        List[str]: List of lines
        
    Example:
        >>> lines = read_lines("data.txt")
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
            if strip_whitespace:
                lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading lines from {file_path}: {e}")


def write_lines(file_path: str, lines: List[str], encoding: str = 'utf-8', append: bool = False) -> bool:
    """
    Write list of lines to file.
    
    Args:
        file_path (str): Path to file
        lines (List[str]): Lines to write
        encoding (str): File encoding
        append (bool): Whether to append or overwrite
        
    Returns:
        bool: True if successful
    """
    try:
        mode = 'a' if append else 'w'
        with open(file_path, mode, encoding=encoding) as file:
            for line in lines:
                file.write(line + '\n')
        return True
    except Exception as e:
        raise Exception(f"Error writing lines to {file_path}: {e}")


def read_json(file_path: str, encoding: str = 'utf-8') -> Union[Dict[Any, Any], List[Any]]:
    """
    Read JSON file.
    
    Args:
        file_path (str): Path to JSON file
        encoding (str): File encoding
        
    Returns:
        Union[Dict, List]: Parsed JSON data
        
    Example:
        >>> data = read_json("config.json")
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {file_path}: {e}")
    except Exception as e:
        raise Exception(f"Error reading JSON from {file_path}: {e}")


def write_json(file_path: str, data: Union[Dict[Any, Any], List[Any]], 
               encoding: str = 'utf-8', indent: int = 2) -> bool:
    """
    Write data to JSON file.
    
    Args:
        file_path (str): Path to JSON file
        data: Data to write
        encoding (str): File encoding
        indent (int): JSON indentation
        
    Returns:
        bool: True if successful
    """
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
        return True
    except Exception as e:
        raise Exception(f"Error writing JSON to {file_path}: {e}")


def read_csv(file_path: str, encoding: str = 'utf-8', delimiter: str = ',', 
             has_header: bool = True) -> List[Dict[str, str]]:
    """
    Read CSV file into list of dictionaries.
    
    Args:
        file_path (str): Path to CSV file
        encoding (str): File encoding
        delimiter (str): CSV delimiter
        has_header (bool): Whether first row is header
        
    Returns:
        List[Dict[str, str]]: List of row dictionaries
    """
    try:
        with open(file_path, 'r', encoding=encoding, newline='') as file:
            if has_header:
                reader = csv.DictReader(file, delimiter=delimiter)
                return list(reader)
            else:
                reader = csv.reader(file, delimiter=delimiter)
                return [{"col_" + str(i): value for i, value in enumerate(row)} 
                       for row in reader]
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading CSV from {file_path}: {e}")


def write_csv(file_path: str, data: List[Dict[str, Any]], encoding: str = 'utf-8', 
              delimiter: str = ',') -> bool:
    """
    Write list of dictionaries to CSV file.
    
    Args:
        file_path (str): Path to CSV file
        data (List[Dict]): Data to write
        encoding (str): File encoding
        delimiter (str): CSV delimiter
        
    Returns:
        bool: True if successful
    """
    if not data:
        raise ValueError("Cannot write empty data to CSV")
    
    try:
        fieldnames = list(data[0].keys())
        with open(file_path, 'w', encoding=encoding, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        raise Exception(f"Error writing CSV to {file_path}: {e}")


def file_exists(file_path: str) -> bool:
    """
    Check if file exists.
    
    Args:
        file_path (str): Path to check
        
    Returns:
        bool: True if file exists
    """
    return os.path.isfile(file_path)


def directory_exists(dir_path: str) -> bool:
    """
    Check if directory exists.
    
    Args:
        dir_path (str): Directory path to check
        
    Returns:
        bool: True if directory exists
    """
    return os.path.isdir(dir_path)


def create_directory(dir_path: str, exist_ok: bool = True) -> bool:
    """
    Create directory (and parent directories if needed).
    
    Args:
        dir_path (str): Directory path to create
        exist_ok (bool): Don't raise error if directory exists
        
    Returns:
        bool: True if successful
    """
    try:
        os.makedirs(dir_path, exist_ok=exist_ok)
        return True
    except Exception as e:
        raise Exception(f"Error creating directory {dir_path}: {e}")


def get_file_size(file_path: str) -> int:
    """
    Get file size in bytes.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        int: File size in bytes
    """
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error getting size of {file_path}: {e}")


def get_file_extension(file_path: str) -> str:
    """
    Get file extension.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        str: File extension (including dot)
        
    Example:
        >>> get_file_extension("document.pdf")
        ".pdf"
    """
    return os.path.splitext(file_path)[1]


def get_filename_without_extension(file_path: str) -> str:
    """
    Get filename without extension.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        str: Filename without extension
        
    Example:
        >>> get_filename_without_extension("/path/to/document.pdf")
        "document"
    """
    return os.path.splitext(os.path.basename(file_path))[0]


def list_files(directory: str, extension: Optional[str] = None, recursive: bool = False) -> List[str]:
    """
    List files in directory.
    
    Args:
        directory (str): Directory to search
        extension (str, optional): Filter by extension (e.g., ".txt")
        recursive (bool): Search subdirectories
        
    Returns:
        List[str]: List of file paths
    """
    files = []
    
    if recursive:
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                if extension is None or filename.endswith(extension):
                    files.append(file_path)
    else:
        try:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    if extension is None or item.endswith(extension):
                        files.append(item_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Directory not found: {directory}")
    
    return files


def copy_file(source: str, destination: str) -> bool:
    """
    Copy file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
        
    Returns:
        bool: True if successful
    """
    try:
        import shutil
        shutil.copy2(source, destination)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {source}")
    except Exception as e:
        raise Exception(f"Error copying {source} to {destination}: {e}")


def move_file(source: str, destination: str) -> bool:
    """
    Move file from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination file path
        
    Returns:
        bool: True if successful
    """
    try:
        import shutil
        shutil.move(source, destination)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {source}")
    except Exception as e:
        raise Exception(f"Error moving {source} to {destination}: {e}")


def delete_file(file_path: str) -> bool:
    """
    Delete file.
    
    Args:
        file_path (str): Path to file to delete
        
    Returns:
        bool: True if successful
    """
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error deleting {file_path}: {e}")


def get_absolute_path(file_path: str) -> str:
    """
    Get absolute path of file.
    
    Args:
        file_path (str): Relative or absolute path
        
    Returns:
        str: Absolute path
    """
    return os.path.abspath(file_path)


def join_paths(*args: str) -> str:
    """
    Join multiple path components.
    
    Args:
        *args: Path components to join
        
    Returns:
        str: Joined path
        
    Example:
        >>> join_paths("home", "user", "documents", "file.txt")
        "home/user/documents/file.txt"
    """
    return os.path.join(*args)


def count_lines_in_file(file_path: str, encoding: str = 'utf-8') -> int:
    """
    Count number of lines in file.
    
    Args:
        file_path (str): Path to file
        encoding (str): File encoding
        
    Returns:
        int: Number of lines
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error counting lines in {file_path}: {e}")


def find_and_replace_in_file(file_path: str, find_text: str, replace_text: str, 
                           encoding: str = 'utf-8') -> bool:
    """
    Find and replace text in file.
    
    Args:
        file_path (str): Path to file
        find_text (str): Text to find
        replace_text (str): Replacement text
        encoding (str): File encoding
        
    Returns:
        bool: True if successful
    """
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
        
        modified_content = content.replace(find_text, replace_text)
        
        with open(file_path, 'w', encoding=encoding) as file:
            file.write(modified_content)
        
        return True
    except Exception as e:
        raise Exception(f"Error in find/replace for {file_path}: {e}")
