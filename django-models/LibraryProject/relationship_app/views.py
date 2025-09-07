from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView ,ListView

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    context = {'book_list':books}

    return render(request, 'list_books.html', context)


class LibraryBooks(ListView):
    template_name = 'library_detail.html'
    model = Library
    context_object_name = 'library'
    