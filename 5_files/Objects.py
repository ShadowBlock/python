"""This exercise tests your understanding of classes and objects."""

# Write your code here
import random


class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)


class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.student_code = first_name[0].lower() + first_name[1].lower() + first_name[2].lower() + last_name[0].lower() + last_name[1].lower() + last_name[2].lower()


class Book:
    def __init__(self, title: str):
        self.title = title

    def __eq__(self, other: str) -> bool:
        return self.title == other


class BookShelf:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.books = []

    def add_book(self, book: Book):
        if self.capacity > len(self.books):
            self.books.append(book)
        else:
            print("This bookshelf can't store any more books.")

    def take_book_by_title(self, title: str):
        for book in self.books:
            if book == title:
                self.books.remove(book)
                return book
        print(f'This bookshelf does not contain a book called {title}.')


class Weapon:
    def __init__(self, name: str, damage: float):
        self.name = name
        self.damage = damage


class Warrior:
    def __init__(self, name: str, health: float):
        self.name = name
        self.health = health
        self.weapon = None

    def warcry(self):
        if self.health > 0.0:
            print("RAAARGH")

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self, enemy):
        if enemy.health == 0.0 or self.health == 0.0:
            return None
        elif self.weapon is None:
            enemy.health -= 2
        else:
            enemy.health -= self.weapon.damage
            if enemy.health <= 0:
                enemy.health = 0
