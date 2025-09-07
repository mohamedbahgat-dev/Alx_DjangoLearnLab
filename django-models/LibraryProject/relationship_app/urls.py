from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_list, name='books'),
    path('library/', views.LibraryBooks.as_view(), name='library' )

]
