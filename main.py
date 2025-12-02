import sys
import os

if __name__ == "__main__":
    library = Library("Городская библиотека")
    
    # Добавляем книги
    library.add_book("1984", "Джордж Оруэлл", 1949)
    library.add_book("Мастер и Маргарита", "Михаил Булгаков", 1966)
    library.add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
    
    # Работа с книгами
    print(library.borrow_book("1984", "Анна"))
    print(library.borrow_book("Мастер и Маргарита", "Борис"))
    print(library.return_book("1984", "Анна"))
    
    # Пробуем ошибочные сценарии
    print(library.borrow_book("Несуществующая книга", "Анна"))
    print(library.return_book("1984", "Несуществующий пользователь"))