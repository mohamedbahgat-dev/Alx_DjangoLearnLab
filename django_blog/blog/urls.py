from django.urls import path
from .views import BlogHomeView, PostListView, LogInView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from .views import ProfileView


urlpatterns = [
    path('', BlogHomeView.as_view(), name= 'home' ),
    path('posts/new/', PostCreateView.as_view(), name = 'post_new'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/',PostListView.as_view(), name='posts' ),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
]