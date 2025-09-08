from django.urls import path, include
from .views import list_books ,  LibraryDetailView 
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library' ),
    path('login/', LoginView.as_view(template_name='relationship_app/templates/login.html'), name='login'  ),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/logout.html'), name='logout' ),
    # path('profile/', ProfileTemplate.as_view(), name='profile'),
    path('register', views.register, name='register'),
]
