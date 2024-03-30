"""This exercise tests your understanding of lists."""

from collections import namedtuple

# Write your code here


def find_smallest_number(numbers: list[int]):
    """Find the smallest number from list."""
    if numbers == []:
        return None
    else:
        smallest = numbers[0]
        for i in range(len(numbers) - 1):
            if smallest > numbers[i + 1]:
                smallest = numbers[i + 1]
        return smallest


def remove_repetitions(items: list[str]):
    """Remove consecutive repetition from list."""
    if items == []:
        return items
    result = [items[0]]
    for i in range(1, len(items)):
        if items[i] != items[i - 1]:
            result.append(items[i])
    return result


def find_shared_values(list_1: list[str], list_2: list[str]):
    """Return list of shared values between 2 lists."""
    result = []
    if not list_1 or not list_2:
        return result
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                result.append(list_1[i])
    return result

# ---------------- Exercise 4 ----------------


Book = namedtuple('Book', ['id', 'title', 'author_ids'])
Author = namedtuple('Author', ['id', 'name', 'birth_year'])


def find_author_names_by_book_id(books: list[Book], authors: list[Author], book_id: int):
    """Find the author names by the book id."""
    book_authors = []
    for i in range(len(books)):
        if book_id == books[i][0]:
            author_id = books[i][2]
            for j in range(len(author_id)):
                for k in range(len(authors)):
                    if author_id[j] == authors[k][0]:
                        book_authors.append(authors[k][1])
    if book_authors == []:
        return book_authors
    else:
        return book_authors

books = [
    Book(id=123, title='Think Python', author_ids=[512]),
    Book(id=2, title='The Pragmatic Programmer', author_ids=[1252, 1253]),
    Book(id=421, title='Introduction to Algorithms', author_ids=[8215, 6883, 7124, 1255]),
]
authors = [
    Author(id=512, name='Allen B. Downey', birth_year=1967),
    Author(id=1252, name='David Thomas', birth_year=1960),
    Author(id=1253, name='Andrew Hunt', birth_year=1964),
    Author(id=8215, name='Thomas H. Cormen', birth_year=1956)
]

print(find_author_names_by_book_id(books, authors, 2))   # -> ['David Thomas', 'Andrew Hunt']
print(find_author_names_by_book_id(books, authors, 421)) # -> ['Thomas H. Cormen']
print(find_author_names_by_book_id(books, authors, 100)) # -> None

# Write your code here


def enter_the_matrix(matrix: list[list[int]]):
    """Change matrix numbers if greater than 0 to 1 and everything else to 0."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix
