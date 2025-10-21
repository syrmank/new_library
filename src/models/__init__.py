# Импортируем основные классы для удобного доступа
from .book import Book

# Определяем что будет доступно при from models import *
__all__ = ['Book']