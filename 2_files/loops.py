def count_letters(text: str, letter: str):
    """Count the letter in text."""
    index = 0
    counter = 0
    for index in range(len(text)):
        if letter.lower() == text[index].lower():
            counter = counter + 1
    return counter


def calculate_sum(number: int):
    """Calculate the sum of number range."""
    sum = 0
    i = 0
    for i in range(number + 1):
        sum = sum + i
    return sum


def reverse_string(text: str):
    """Reverse the string order."""
    length = len(text)
    new_string = ""
    i = 0
    for i in range(length):
        new_string = new_string + text[length - 1 - i]
    return new_string


def is_palindrome(word: str):
    """Check for palindrome."""
    reversed = reverse_string(word)
    if reversed.lower() == word.lower():
        return True
    else:
        return False


def trim_start(text: str):
    """Trim whitespace from text."""
    while text and text[0] == ' ':
        text = text[1:]
    return text
