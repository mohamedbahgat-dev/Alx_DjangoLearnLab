from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Book
from .forms import ExampleForm
from django.views import View




# Create your views here.
def index(request):
    return HttpResponse('welcome to book shelf')

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    render(request, 'list_books.html', context)

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


    
class ExampleFormViewClass(View):
    """
    A class-based view for handling the FormExample.
    """
    template_name = 'example_form.html'
    
    def get(self, request):
        """Handles GET requests by rendering an empty form."""
        form = ExampleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Handles POST requests by validating and processing form data."""
        form = ExampleForm(request.POST)
        
        if form.is_valid():
            # Process and save the cleaned data.
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user_bio = form.cleaned_data['user_bio']
            
            # Example: Save user data using the User model
            # This is where you would perform your database logic.
            
            return redirect('success_url_name')
        
        # If the form is not valid, re-render the template with the errors.
        return render(request, self.template_name, {'form': form})