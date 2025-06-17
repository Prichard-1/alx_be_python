class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        """Initialize a new book with a title and author, marked as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book, making it available again."""
        if not self._is_checked_out:
            return False  # Already available
        self._is_checked_out = False
        return True

    def __str__(self):
        """Return a string representation of the book."""
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store book objects

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out if available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"Successfully checked out: '{title}'")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        """Find a book by title and return it if checked out."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"Successfully returned: '{title}'")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found.")

    def list_available_books(self):
        """Display all books that are currently available."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books are currently available.")


