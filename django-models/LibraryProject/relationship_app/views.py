from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView

from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


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


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect("profile")  # Replace "home" with your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/templates/register.html", {"form": form})

class ProfileTemplate(TemplateView):
    template_name = 'relationship_app/templates/profile.html'