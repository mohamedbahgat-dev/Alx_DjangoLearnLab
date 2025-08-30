# Method 1: Using the create() method

new_book = Book.objects.create(title='1984', author='George Orwell', publication_year = 1990)
new_book.save()

# This will create a book object with these title, author and publication_year
