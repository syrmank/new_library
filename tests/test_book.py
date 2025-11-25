from src.models.book import Book

def test_book_borrow_true():
    book = Book("Алиса в Стране Чудес", "Льюис Кэрролл", 1865, "1234-234-345-34")
    assert book.borrow() == "Книга 'Алиса в Стране Чудес' выдана"
    b = a + 1

