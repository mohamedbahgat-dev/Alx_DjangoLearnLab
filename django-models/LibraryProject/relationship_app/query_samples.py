# list all books in alibrary
all_books = Library.objects.all()

# Filtering books by author
books_by_author = Book.objects.filter(author='Sharles Dekens')

# retrive librarian for specific library
librarian_for_library = Librarian.objects.filter(library = 'New York')