from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Book


# Create your views here.
def index(request):
    return HttpResponse('welcome to book shelf')

# create permissions views
@permission_required('bookshelf.can_view', raise_exception=True)
class BooksView(ListView):
    model = Book
    fields = '__all__'
    template_name = 'book_view.html'

@permission_required('bookshelf.can_create', raise_exception=True)
class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_create_form.html'


@permission_required('bookshelf.can_edit', raise_exception=True)
class BookEditView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_edit_form.html'

@permission_required('bookshelf.can_delete', raise_exception=True)
class BookDeleteView(DeleteView):
    model = Book
    fields = '__all__'
    template_name = 'book_confirm_delete_form.html'


    
