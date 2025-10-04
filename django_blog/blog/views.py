from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import CustomeCreationFrom, ProfileForm, PostForm, CommentForm
from django.urls import reverse_lazy
from .models import Post, Comment
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomeCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'blog/register.html'

class LogInView(LoginView):
    template_name = 'blog/login.html'

class BlogHomeView(TemplateView):
    model = Post
    template_name = 'blog/home.html'
   

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
    

# views to handle CRUD operations
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    success_url = reverse_lazy('posts')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('posts')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("You are not allowed to delete this post.")
        
        return redirect('login')
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("You are not allowed to delete this post.")
        
        return redirect('login')
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk = self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs = {'pk':self.kwargs['pk']})
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
