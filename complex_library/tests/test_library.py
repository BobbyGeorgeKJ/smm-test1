import unittest
from library.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library("City Library")
        self.lib.add_book("1984", "George Orwell", "111")
        self.lib.add_book("The Hobbit", "J.R.R. Tolkien", "222")
        self.lib.add_user("Alice", 1)
        self.lib.add_user("Bob", 2)

    def test_borrow_return(self):
        user = self.lib.find_user(1)
        book = self.lib.find_book("1984")
        user.borrow_book(book)
        self.assertFalse(book.available)
        user.return_book(book)
        self.assertTrue(book.available)

    def test_find_book_user(self):
        self.assertIsNotNone(self.lib.find_book("1984"))
        self.assertIsNone(self.lib.find_book("Nonexistent"))
        self.assertIsNotNone(self.lib.find_user(1))
        self.assertIsNone(self.lib.find_user(99))

if __name__ == "__main__":
    unittest.main()
