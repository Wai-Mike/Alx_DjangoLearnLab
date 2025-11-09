"""Sample ORM queries for relationship_app."""

from typing import List, Optional

from .models import Author, Library, Librarian


def books_by_author(author_name: str) -> List[str]:
    """Return a list of book titles for the given author name."""
    author: Optional[Author] = Author.objects.filter(name=author_name).first()
    if not author:
        return []
    return list(author.books.values_list('title', flat=True))


def books_in_library(library_name: str) -> List[str]:
    """Return a list of book titles available in the named library."""
    library: Optional[Library] = Library.objects.filter(name=library_name).first()
    if not library:
        return []
    return list(library.books.values_list('title', flat=True))


def librarian_for_library(library_name: str) -> Optional[Librarian]:
    """Return the librarian for the given library name, if present."""
    library: Optional[Library] = Library.objects.filter(name=library_name).first()
    if not library:
        return None
    return getattr(library, 'librarian', None)

