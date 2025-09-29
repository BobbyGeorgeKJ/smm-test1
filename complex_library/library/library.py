from library.book import Book
from library.user import User

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def show_books(self):
        for book in self.books:
            print(book)

    # Duplicate method to trigger maintainability metric
    def list_books(self):
        for book in self.books:
            print(book)

    def show_users(self):
        for user in self.users:
            print(user)
