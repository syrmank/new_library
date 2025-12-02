from datetime import datetime


def validate_book_data(title, author, year=None):
    if not title or not title.strip():
        return False, "Название книги не может быть пустым"
    
    if not author or not author.strip():
        return False, "Автор не может быть пустым"
    
    if year is not None:
        if not isinstance(year, int):
            return False, "Год должен быть числом"
        if year < 0 or year > datetime.now().year + 1:
            return False, f"Некорректный год: {year}"
    
    return True, "Данные корректны"