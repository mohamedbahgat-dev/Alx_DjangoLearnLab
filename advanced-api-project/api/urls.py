from django.urls import path
from .views import ListView, DeleteView, UpdateView, DetailView, CreateView

urlpatterns = [
    path("books/create", CreateView.as_view(), name='new'),
    path("books/", ListView.as_view(), name='book_list'),
    path("books/<int:pk>/", DetailView.as_view(), name='detail'),
    path("books/update", UpdateView.as_view(), name='update'),
    path("books/delete", DeleteView.as_view(), name='delete'),

]