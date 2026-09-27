class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, isbn):
        """Initialize a new book with title, author, and ISBN."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Return the book information."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def get_details(self):
        """Return the book's details."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }