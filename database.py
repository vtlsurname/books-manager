import sqlite3
from config import DATABASE_PATH


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.initialize_db()

    def initialize_db(self):
        """ Инициализирует базу данных с таблицами для книг и жанров. """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                description TEXT,
                genre_id INTEGER,
                FOREIGN KEY (genre_id) REFERENCES genres (id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL
            )
        ''')
        self.conn.commit()

    def add_book(self, title, author, description, genre_name):
        """ Добавляет новую книгу в базу данных. """
        # добавляем жанр если он не существует
        self.cursor.execute("INSERT OR IGNORE INTO genres (name) VALUES (?)", (genre_name,))
        self.cursor.execute("SELECT id FROM genres WHERE name = ?", (genre_name,))
        genre_id = self.cursor.fetchone()[0]

        # добавляем книгу
        self.cursor.execute("INSERT INTO books (title, author, description, genre_id) VALUES (?, ?, ?, ?)",
                            (title, author, description, genre_id))
        self.conn.commit()

    def delete_book(self, book_id):
        """ Удаляет книгу по идентификатору. """
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()

    def find_books(self, search_query):
        """ Ищет книги по названию или автору. """
        query = f"%{search_query}%"
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (query, query))
        return self.cursor.fetchall()

    def list_books(self):
        """ Возвращает список всех книг. """
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def close(self):
        """ Закрывает соединение с базой данных. """
        self.conn.close()
