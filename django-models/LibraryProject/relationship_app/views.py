from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list':books}

    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'library'
    
class LogInForm(LoginView):
    template_name = 'relationship_app/templates/login.html'

class ProfileTemplate(TemplateView):
    template_name = 'relationship_app/templates/profile.html'


class SignUpForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'relationship_app/templates/register.html'

class ProfileTemplate(TemplateView):
    template_name = 'relationship_app/templates/profile.html'