from django.shortcuts import render
from .models import Book
from .models import Library

from django.views.generic import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list':books}

    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'library'
    