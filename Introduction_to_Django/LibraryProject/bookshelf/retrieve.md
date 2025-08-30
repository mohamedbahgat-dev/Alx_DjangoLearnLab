# Retrieve all objects

all_books = Book.objects.all()
print(all_books)

# Retrieve a single object by primary key (pk) or specific field

single_book = Book.objects.get(title = '1984') # Assuming pk=1 exists
print(single_book.title)

# Filter objects based on conditions

filtered_books = Book.objects.filter(author='Jane Smith')
print(filtered_books)
