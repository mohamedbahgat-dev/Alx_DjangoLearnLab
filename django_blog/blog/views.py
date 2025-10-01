from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomeCreationFrom, ProfileForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


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

class ProfileView(View, LoginRequiredMixin):
    template_name = 'blog/profile.html'

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        method = request.POST
        form = ProfileForm(method, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfuly!')
            return redirect('profile')
        return render(request, self.template_engine, {'form':form})