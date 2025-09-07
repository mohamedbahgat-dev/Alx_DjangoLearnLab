# Get book and update author name

book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
