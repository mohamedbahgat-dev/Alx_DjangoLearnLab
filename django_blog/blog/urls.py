from django.urls import path
from .views import BlogHomeView, PostListView, LogInView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from .views import ProfileView


urlpatterns = [
    path('', BlogHomeView.as_view(), name= 'home' ),
    path('post/new/', PostCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/',PostListView.as_view(), name='posts' ),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name = 'add_comment' ),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]