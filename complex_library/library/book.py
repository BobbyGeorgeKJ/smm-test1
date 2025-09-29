class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.history = []

    def borrow(self):
        if self.available:
            self.available = False
            self.history.append("borrowed")
            return True
        return False

    def return_book(self):
        self.available = True
        self.history.append("returned")

    # Risky hotspot
    def run_custom_code(self, code):
        return eval(code)

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
