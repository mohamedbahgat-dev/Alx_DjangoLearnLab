from models import Book, Librarian, Library

# list all books in alibrary
books = Library.objects.get(name='library_name')
books.all()

# Filtering books by author
books_by_author = Book.objects.filter(author='author_name')

# retrive librarian for specific library
librarian_for_library = Librarian.objects.filter(library = 'library_name')