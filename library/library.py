"""Library system with books management."""

from dataclasses import dataclass


@dataclass
class Book:
    """Book with title, author, year and availability status."""
    title: str
    author: str
    year: int
    is_available: bool = True


class LibraryError(Exception):
    """Base exception for library errors."""
    pass


class BookNotFoundError(LibraryError):
    """Raised when a book is not found."""
    pass


class BookAlreadyExistsError(LibraryError):
    """Raised when trying to add a book that already exists."""
    pass


class BookNotAvailableError(LibraryError):
    """Raised when trying to borrow an already borrowed book."""
    pass


class ToDictMixin:
    """Mixin that converts object to dict with public attributes."""

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


class Library(ToDictMixin):
    """Library that manages a collection of books."""

    def __init__(self, books=None):
        self._books = books if books is not None else []

    def add_book(self, book: Book) -> None:
        """Add a book. Raise BookAlreadyExistsError if duplicate."""
        for b in self._books:
            if b.title == book.title:
                raise BookAlreadyExistsError("Книга уже есть")
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        """Remove a book by title. Raise BookNotFoundError if not found."""
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return
        raise BookNotFoundError(f"Книга '{title}' не найдена")

    def find_by_author(self, author: str) -> list:
        """Return list of books by the given author."""
        return [book for book in self._books if book.author == author]

    def get_available_books(self) -> list:
        """Return list of available books."""
        return [book for book in self._books if book.is_available]

    def borrow_book(self, title: str) -> None:
        """Mark book as unavailable. Raise if not found or already borrowed."""
        for book in self._books:
            if book.title == title:
                if not book.is_available:
                    raise BookNotAvailableError("Книга уже выдана")
                book.is_available = False
                return
        raise BookNotFoundError("Книга не найдена")

    def return_book(self, title: str) -> None:
        """Mark book as available. Raise if not found."""
        for book in self._books:
            if book.title == title:
                book.is_available = True
                return
        raise BookNotFoundError("Книга не найдена")

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __str__(self) -> str:
        return f"Библиотека: {len(self._books)} книг"

    @property
    def available_count(self) -> int:
        """Number of available books."""
        return len([book for book in self._books if book.is_available])

    @classmethod
    def from_csv(cls, csv_string: str) -> "Library":
        """Create library from string: 'title,author,year;...'."""
        library = cls()
        for part in csv_string.split(';'):
            title, author, year = part.split(',')
            library.add_book(Book(title, author, int(year)))
        return library