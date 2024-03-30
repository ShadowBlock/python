"""This exercise tests your understanding of conditional statements."""


def biggest_number(a: int, b: int):
    """Find the biggest number."""
    if a > b:
        return a
    else:
        return b


def compare_numbers(a: int, b: int):
    """Compare the numbers."""
    if a > b:
        return 'bigger'
    elif a == b:
        return 'equal'
    else:
        return 'smaller'


def contains_substring(text: str, substring: str):
    """Check if substring exists in text."""
    if substring.lower() in text.lower():
        return True
    else:
        return False


def are_equal(a, b):
    """Check if values are equal."""
    if a == b:
        if isinstance(a, int) and isinstance(b, int):
            return True
        elif isinstance(a, str) and isinstance(b, str):
            return True
        elif isinstance(a, float) and isinstance(b, float):
            return True
        else:
            return False
    else:
        return False


def calculate(a: int, b: int, operation: str):
    """Calculate with operators given by user."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return None
