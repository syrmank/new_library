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
    
    def find_book(self, title):
        """Найти книгу"""
        for book in self.books:
            if book.title == title:
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
    