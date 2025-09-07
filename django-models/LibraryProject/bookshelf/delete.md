from bookshelf.models import Book

# Retrive book and delete it

book = Book.objects.get(title='1984')
book.delete()
