# Zwergenland Python Converter

Goal is to convert an Excel file to a .csv file.

## Setup Environment

### Install Tools and Plugins

- Python 3.12
  - venv
- VS Code
  - Code Spell Check
  - Python Extension Pack
  - autopep8
- Powershell 7

### Setup

In the root directory of the Git project.

```bash
python -m venv .venv
.venv/Scripts/activate.ps1
pip install -r requirements.txt
```

To leave the virtual environment simply type.

```bash
deactivate
```

## Test

```bash
python -m unittest
python -m pylint converter --max-line-length=120
```

## Run

Run the application from virtual environment in Git root.

```bash
python.exe ./converter/main.py
```

## Build

```bash
pyinstaller --onefile --noconsole converter/main.py
```
