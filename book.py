class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self) -> str:
        return f"'{self.title}', автор - {self.author}, год публикации - {self.year}"
    
book1 = Book("Название1", "Автор1", 1991, "978-5-17-080077-7")
print(book1)
