# main.py
from library import Library

def main():
    library = Library("City Library")

    # Add books
    library.add_book("1984", "George Orwell", "111")
    library.add_book("The Hobbit", "J.R.R. Tolkien", "222")
    library.add_book("Python Programming", "John Zelle", "333")

    # Add users
    library.add_user("Alice", 1)
    library.add_user("Bob", 2)

    # Show books and users
    print("\n📚 Books in Library:")
    library.show_books()

    print("\n👤 Users:")
    library.show_users()

    # Borrow and return
    user1 = library.find_user(1)
    book1 = library.find_book("1984")

    user1.borrow_book(book1)
    user1.borrow_book(book1)  # Trying again should fail

    print("\n📚 Books after borrowing:")
    library.show_books()

    user1.return_book(book1)

    print("\n📚 Books after returning:")
    library.show_books()

if __name__ == "__main__":
    main()
