from django.urls import path
from .views import BlogHomeView, PostListView, LogInView
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from .views import ProfileView


urlpatterns = [
    path('', BlogHomeView.as_view(), name= 'home' ),
    path('posts/',PostListView.as_view(), name='posts' ),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name = 'profile')

]