class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True

    def __str__(self) -> str:
        return f"'{self.title}', автор - {self.author}, год публикации - {self.year}"
    
    def borrow(self) -> str:
        '''Бронирование книги'''
        if self.is_available:
            self.is_available = False
            return f"Книга '{self.title}' выдана"
        else:
            return f"Выдача книги '{self.title}' невозможна!"
        
    def return_book(self) -> str:
        if not self.is_available:
            self.is_available = True
            return f"Книга '{self.title}' возвращена"
        else:
            return f"Возврат книги '{self.title}' невозможен!"
        