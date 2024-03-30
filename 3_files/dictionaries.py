"""This exercise tests your understanding of dictionaries."""

from collections import namedtuple
from typing import TypedDict

# Write your code here


def create_statistics_map(word_statistics: list[tuple[str, int]]):
    """Make tuples into dictionaries."""
    result = {

    }
    for i in range(len(word_statistics)):
        result[word_statistics[i][0]] = word_statistics[i][1]
    return result


def find_words_by_appearance(word_statistics: dict[str, int], minimum_occurences: int):
    """Find words by how many times it has appeared in the statistics."""
    words = []
    for key, value in word_statistics.items():
        if value > minimum_occurences:
            words.append(key)
    return words


def group_names_by_letter(name: list[str]):
    """Create and return dictionary where names are grouped in sets based on their first letter."""
    result = {}
    for name in name:
        first_letter = name[0]
        if first_letter in result:
            result[first_letter].add(name)
        else:
            result[first_letter] = {name}
    return result


# ---------------- Exercise 4 ----------------

Book = namedtuple('Book', ['title', 'author_ids'])
Author = namedtuple('Author', ['name', 'birth_year'])

# Write your code here


def find_author_names_by_book_id(books: dict[int, Book], authors: dict[int, Author], book_id: int):
    """Find author names by book id from books dictionary and then from authors dictionary."""
    book_authors = []
    author_id = []
    for key, value in books.items():
        if key == book_id:
            author_id = value.author_ids
            for key, value in authors.items():
                for i in range(len(author_id)):
                    if key == author_id[i]:
                        book_authors.append(value.name)
    return book_authors


# ---------------- Exercise 5 ----------------

Game = TypedDict(
    'Game',
    {
        'id': int,
        'name': 'str',
        'developer': str,
        'publisher': str,
        'year_published': int,
        'genres': list[str],
        'full_price': float,
        'current_price': float,
    }
)

GameFilter = TypedDict('GameFilter', {'name_contains': str, 'price_less_than': float, 'has_genre': str}, total=False)

# Write your code here
def filter_games(games: list[Game], game_filter: GameFilter):
    """Filter games by name, price or genre."""
    filtered_games = []
    for key, value in game_filter.items():
        if key == 'name_contains':
            for game in games:
                if value.lower() in game['name'].lower():
                    filtered_games.append(game)
                elif value.lower() not in game['name'].lower() and game in filtered_games:
                    filtered_games.remove(game)
        if key == 'price_less_than':
            for game in games:
                if value >= game['current_price']:
                    filtered_games.append(game)
                elif value < game['current_price'] and game in filtered_games:
                    filtered_games.remove(game)
        if key == 'has_genre':
            for game in games:
                for genre in game['genres']:
                    if genre == value:
                        filtered_games.append(game)
                    elif genre != value and game in filtered_games:
                        filtered_games.remove(game)
    return filtered_games



games: list[Game] = [
    {
        'id': 5125424,
        'name': 'Dishonored',
        'developer': 'Arkane Studios',
        'publisher': 'Bethesda Softworks',
        'year_published': 2012,
        'genres': ['Action'],
        'full_price': 9.99,
        'current_price': 2.50,
    },
    {
        'id': 5125424,
        'name': 'Lethal Company',
        'developer': 'Zeekerss',
        'publisher': 'Zeekerss',
        'year_published': 2023,
        'genres': ['Action', 'Adventure', 'Indie', 'Early Access'],
        'full_price': 9.75,
        'current_price': 6.82,
    },
    {
        'id': 5125424,
        'name': 'Cyberpunk 2077',
        'developer': 'CD PROJECT RED',
        'publisher': 'CD PROJECT RED',
        'year_published': 2020,
        'genres': ['RPG'],
        'full_price': 59.99,
        'current_price': 29.99,
    },
]

print(filter_games(games, {'name_contains': 'c', 'price_less_than': 10.0}))
# -> [
#     {
#         'id': 5125424,
#         'name': 'Lethal Company',
#         'developer': 'Zeekerss',
#         'publisher': 'Zeekerss',
#         'year_published': 2023,
#         'genres': ['Action', 'Adventure', 'Indie', 'Early Access'],
#         'full_price': 9.75,
#         'current_price': 6.82,
#     },
# ]