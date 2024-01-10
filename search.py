from database import Database

def search_books(search_query):
    """ Поиск книг по заданному запросу. """
    db = Database()
    try:
        results = db.find_books(search_query)
        if results:
            print(f"Найденные книги для '{search_query}':")
            for book in results:
                print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}")
        else:
            print("Книги не найдены.")
    finally:
        db.close()
