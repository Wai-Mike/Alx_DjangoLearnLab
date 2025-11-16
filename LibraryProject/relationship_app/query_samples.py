"""Sample ORM queries for relationship_app."""

from typing import Optional

from .models import Book, Librarian


def get_books_by_author(author_name: str):
    """Query all books written by the specified author."""
    return Book.objects.filter(author__name=author_name)


def get_books_in_library(library_name: str):
    """List all books that belong to the specified library."""
    return Book.objects.filter(libraries__name=library_name)


def get_librarian_for_library(library_name: str) -> Optional[Librarian]:
    """Retrieve the librarian responsible for the specified library."""
    return Librarian.objects.filter(library__name=library_name).first()
