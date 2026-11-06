class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.borrowed_by = None  

    def __repr__(self):
        status = f"на руках у {self.borrowed_by}" if self.borrowed_by else "в библиотеке"
        return f"'{self.title}' ({self.author}, {self.year}) — {status}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, title: str, author: str, year: int) -> Book:
        book = Book(title, author, year)
        self.books.append(book)
        return book

    def borrow_book(self, title: str, reader: str) -> str:
        for book in self.books:
            if book.title == title:
                if book.borrowed_by is not None:
                    return f"Ошибка: '{title}' уже на руках у {book.borrowed_by}"
                book.borrowed_by = reader
                return f"'{title}' выдана читателю {reader}"
        return f"Ошибка: книга '{title}' не найдена"

    def return_book(self, title: str, reader: str) -> str:
        for book in self.books:
            if book.title == title:
                if book.borrowed_by is None:
                    return f"Ошибка: '{title}' не выдавалась"
                if book.borrowed_by != reader:
                    return f"Ошибка: '{title}' на руках у {book.borrowed_by}, а не у {reader}"
                book.borrowed_by = None
                return f"'{title}' возвращена в библиотеку"
        return f"Ошибка: книга '{title}' не найдена"


    def get_sorted_by_year(self, reverse: bool = False) -> list[Book]:
        return sorted(self.books, key=lambda b: b.year, reverse=reverse)

