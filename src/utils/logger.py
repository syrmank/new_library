import logging
import os
from datetime import datetime

def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    logger = logging.getLogger("LibraryProject")

    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    log_file = os.path.join(log_dir, f"library_{datetime.now().strftime('%Y-%m-%d')}.log")
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("=" * 50)
    logger.info("Система логирования инициализирована")
    logger.info(f"Логи записываются в: {log_file}")
    logger.info("=" * 50)
    
    return logger

main_logger = logging.getLogger("LibraryProject.Main")
book_logger = logging.getLogger("LibraryProject.Book")
library_logger = logging.getLogger("LibraryProject.Library")