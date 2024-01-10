from database import Database
from book import Book
import search


def print_menu():
    """ Печатает главное меню приложения. """
    print("\nГлавное меню:")
    print("1. Добавить книгу")
    print("2. Просмотреть список книг")
    print("3. Поиск книги")
    print("4. Удалить книгу")
    print("5. Выход")


def add_book_ui():
    """ Интерфейс для добавления новой книги. """
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    description = input("Введите описание книги: ")
    genre = input("Введите жанр книги: ")

    book = Book(title, author, description, genre)
    db = Database()
    db.add_book(book.title, book.author, book.description, book.genre)
    db.close()
    print("Книга добавлена.")


def list_books_ui():
    """ Интерфейс для просмотра списка книг. """
    db = Database()
    books = db.list_books()
    db.close()
    for book in books:
        print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}")


def search_books_ui():
    """ Интерфейс для поиска книг. """
    query = input("Введите запрос для поиска: ")
    search.search_books(query)


def delete_book_ui():
    """ Интерфейс для удаления книги. """
    book_id = input("Введите ID книги для удаления: ")
    db = Database()
    db.delete_book(book_id)
    db.close()
    print("Книга удалена.")


def main():
    while True:
        print_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            add_book_ui()
        elif choice == "2":
            list_books_ui()
        elif choice == "3":
            search_books_ui()
        elif choice == "4":
            delete_book_ui()
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
