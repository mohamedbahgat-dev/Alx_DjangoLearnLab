# Retrive book and delete it

book_to_delete = Book.objects.get(title='1984')
book_to_delete.delete()
