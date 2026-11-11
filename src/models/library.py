from book import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        """Добавить книгу"""
        book = Book(title, author)
        self.books.append(book)
        return book

    def find_by_title(self, title):

        """Найти книгу"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        """Выдать книгу"""
        book = self.find_book(title)
        if not book:
            return False

        if book.borrow():
            return True
        return False

    def find_by_author(author: str) -> list[Book]:
        return [book for book in self.books if book.author == author]
      
    def get_sorted_by_year(self, books, reverse=False) -> list[Book]:
        sorted_list = sorted(books, key=lambda x: x.year, reverse=reverse)
        return sorted_list
