# Get book and update author name

book_to_update = Book.objects.get(title='New Book')
book_to_update.author = 'Fitzgerald, F. Scott'
book_to_update.save()
