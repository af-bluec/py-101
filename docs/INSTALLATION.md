# Installation Guide

## Python 101 - Complete Installation Instructions

This guide will help you set up the Python 101 project on your system.

---

## System Requirements

### Minimum Requirements
- **Python 3.6 or higher**
- **Git** (for cloning the repository)
- **Text Editor or IDE** (recommended: VS Code, PyCharm, or Sublime Text)

### Recommended System Specifications
- **Operating System**: Windows 10+, macOS 10.12+, or Linux (Ubuntu 18.04+)
- **RAM**: 4GB or more
- **Storage**: 100MB free space
- **Python Version**: 3.8+ (for best performance and features)

---

## Pre-Installation Steps

### 1. Check Python Installation

First, verify that Python is installed on your system:

#### Windows:
```cmd
python --version
```
or
```cmd
python3 --version
```

#### macOS/Linux:
```bash
python3 --version
```

**Expected Output:**
```
Python 3.8.10 (or higher)
```

### 2. Install Python (if needed)

If Python is not installed or you have an older version:

#### Windows:
1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python 3.x installer
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Verify installation with `python --version`

#### macOS:
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from python.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Linux (CentOS/RHEL):
```bash
sudo yum install python3 python3-pip
```

### 3. Verify pip Installation

Pip should be included with Python 3.4+:

```bash
pip --version
# or
pip3 --version
```

---

## Installation Methods

## Method 1: Git Clone (Recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/py-101.git
cd py-101
```

### Step 2: Verify Installation

```bash
# List project files
ls -la

# Run the main script to test
python main.py
```

## Method 2: Download ZIP

### Step 1: Download
1. Go to the project's GitHub page
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file to your desired location

### Step 2: Navigate to Project
```bash
cd py-101-main  # or wherever you extracted
```

### Step 3: Verify Installation
```bash
python main.py
```

---

## Project Setup

### Directory Structure Verification

After installation, your directory should look like this:

```
py-101/
├── main.py                 # Main demonstration script
├── utils/
│   ├── __init__.py        # Package initialization
│   ├── string_utils.py    # String manipulation functions
│   ├── math_utils.py      # Mathematical utility functions
│   ├── data_structures.py # Data structure helper functions
│   ├── file_utils.py      # File handling utilities
│   └── validators.py      # Input validation functions
├── examples/
│   ├── string_examples.py # String utility examples
│   ├── math_examples.py   # Math utility examples
│   └── data_examples.py   # Data structure examples
├── tests/
│   └── test_functions.py  # Basic function tests
├── docs/                  # Documentation
├── README.md              # Project documentation
└── requirements.txt       # Dependencies (currently none)
```

### Python Path Setup

To import modules from anywhere, you can:

#### Option 1: Add to PYTHONPATH (Temporary)
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/py-101"
```

#### Option 2: Install in Development Mode
```bash
cd py-101
pip install -e .
```

---

## Installation Verification

### 1. Run Main Script

```bash
python main.py
```

**Expected Output:**
```
=== Python 101 Demonstrations ===

--- Mathematical Functions ---
Factorial of 5: 120
Is 17 prime? True
Fibonacci sequence (10): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

--- String Functions ---
Greeting: Hello, Python Learner!
...
```

### 2. Test Individual Modules

```bash
# Test string utilities
python -c "from utils.string_utils import clean_text; print(clean_text('  hello  '))"

# Test math utilities  
python -c "from utils.math_utils import gcd; print(gcd(48, 18))"

# Test data structures
python -c "from utils.data_structures import flatten_list; print(flatten_list([[1,2], [3,4]]))"
```

### 3. Run Test Suite

```bash
python tests/test_functions.py
```

**Expected Output:**
```
Running tests...
All tests passed!
```

---

## Development Environment Setup

### Recommended IDEs

#### Visual Studio Code
1. Install VS Code from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install Python extension
3. Open the py-101 folder
4. Configure Python interpreter (Ctrl+Shift+P → "Python: Select Interpreter")

#### PyCharm Community Edition
1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Install and create new project
3. Open existing folder (py-101)
4. Configure Python interpreter

#### Sublime Text
1. Install Sublime Text
2. Install Package Control
3. Install "Python" package
4. Open py-101 folder

### Git Configuration (Optional)

If you plan to contribute:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Platform-Specific Instructions

### Windows-Specific Setup

#### Using Command Prompt:
```cmd
# Navigate to project
cd C:\path\to\py-101

# Run main script
python main.py
```

#### Using PowerShell:
```powershell
# Navigate to project  
Set-Location C:\path\to\py-101

# Run main script
python main.py
```

#### Common Windows Issues:
- **Python not found**: Add Python to PATH environment variable
- **Permission errors**: Run Command Prompt as Administrator
- **Module not found**: Ensure you're in the correct directory

### macOS-Specific Setup

#### Using Terminal:
```bash
# Navigate to project
cd ~/path/to/py-101

# Run main script
python3 main.py
```

#### Common macOS Issues:
- **Command not found**: Use `python3` instead of `python`
- **Permission denied**: Check file permissions with `ls -la`
- **Xcode tools needed**: Run `xcode-select --install`

### Linux-Specific Setup

#### Using Terminal:
```bash
# Navigate to project
cd ~/path/to/py-101

# Run main script
python3 main.py
```

#### Common Linux Issues:
- **Python3 not found**: Install with package manager
- **Permission errors**: Check file ownership and permissions
- **Missing dependencies**: Install build essentials if needed

---

## Virtual Environment Setup (Optional)

For isolated development:

### Create Virtual Environment:
```bash
# Create virtual environment
python -m venv py101_env

# Activate virtual environment
# Windows:
py101_env\Scripts\activate

# macOS/Linux:
source py101_env/bin/activate
```

### Install Project:
```bash
# Navigate to project directory
cd py-101

# No additional packages needed currently
# Project uses only standard library
```

### Deactivate Virtual Environment:
```bash
deactivate
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Python is not recognized"
**Solution:**
- Windows: Add Python to PATH environment variable
- macOS/Linux: Use `python3` instead of `python`

#### Issue: "No module named 'utils'"
**Solution:**
- Ensure you're in the correct directory (py-101)
- Check that `utils/__init__.py` exists
- Verify Python can find the modules

#### Issue: "Permission denied"
**Solution:**
```bash
# Make files executable
chmod +x main.py

# Or run with python explicitly
python main.py
```

#### Issue: Tests fail
**Solution:**
- Check Python version (must be 3.6+)
- Verify all files are present
- Check file permissions

### Getting Help

If you encounter issues:

1. **Check Python version**: `python --version`
2. **Verify file structure**: Ensure all files are present
3. **Check error messages**: Read the full error output
4. **Try virtual environment**: Isolate dependencies
5. **Update Python**: Use the latest stable version

---

## Next Steps

After successful installation:

1. **Read the README**: Understanding project overview
2. **Explore examples**: Check the `examples/` directory
3. **Run demonstrations**: Execute `python main.py`
4. **Read documentation**: Browse the `docs/` folder
5. **Try modifications**: Experiment with the code
6. **Run tests**: Verify everything works with `python tests/test_functions.py`

---

## System Performance

### Expected Performance
- **Startup time**: < 1 second
- **Memory usage**: < 50MB
- **Disk space**: < 10MB

### Optimization Tips
- Use Python 3.8+ for better performance
- Consider PyPy for compute-intensive operations
- Use virtual environments to avoid conflicts

---

## Uninstallation

To remove the project:

```bash
# Simply delete the project directory
rm -rf py-101

# If installed in development mode
pip uninstall py-101
```

---

## Support

For installation support:
- **GitHub Issues**: Report bugs and ask questions
- **Documentation**: Check the `docs/` folder
- **Examples**: Review the `examples/` directory

**Happy coding! 🐍**
