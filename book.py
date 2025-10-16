class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self) -> str:
        return f"'{self.title}', автор - {self.author}, год публикации - {self.year}"
    
book1 = Book("Название", "Автор", 1990)
print(book1)