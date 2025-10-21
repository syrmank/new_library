class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self) -> str:
        return f"'{self.title}', автор - {self.author}, год публикации - {self.year}"