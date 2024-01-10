class Book:
    def __init__(self, title, author, description, genre):
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}. Description: {self.description}"
