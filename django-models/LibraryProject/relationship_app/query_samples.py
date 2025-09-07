from models import Book, Librarian, Library,Author

# list all books in alibrary
books = Library.objects.get(name=library_name)
books.all()

# Filtering books by author
author = Author.objects.get(name=author_name)
books_by_author.objects.filter(author = author)

# retrive librarian for specific library
librarian_for_library = Librarian.objects.filter(library =library_name)