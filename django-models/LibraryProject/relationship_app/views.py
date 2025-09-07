from django.shortcuts import render
from .models import Book

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    context = {'book_list':books}

    return render(request, 'book_list.html', context)
