from django.urls import path, include
from .views import list_books ,  LibraryDetailView , LogInForm, ProfileTemplate
from . import views

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', LogInForm.as_view(), name='login'  ),
    path('accounts/profile/', ProfileTemplate.as_view(), name='profile'),
    path('register', views.register, name='register'  ),
  

]
