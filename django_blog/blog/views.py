from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomeCreationFrom
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomeCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

    
class LogInView(LoginView):
    template_name = 'blog/login.html'

class BlogHomeView(TemplateView):
    model = Post
    template_name = 'blog/home.html'
   
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

class ProfileView(TemplateView):
    template_name = 'blog/profile.html'