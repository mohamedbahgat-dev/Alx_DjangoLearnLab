from django.urls import path, include
from .views import list_books ,  LibraryDetailView 
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .accounts import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library' ),
    path('login/', LoginView.as_view(template_name='relationship_app/templates/login.html'), name='login'  ),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/logout.html'), name='logout' ),
    # path('profile/', ProfileTemplate.as_view(), name='profile'),
    path('register', views.register, name='register'),
    path('admin-only/', admin_view.admin_view, name='admin_view'),
    path('librarian-only/', librarian_view.librarian_view, name='librarian_view'),
    path('member-only/', member_view.member_view, name='member_view'),
    # Add a new book (requires 'relationship_app.can_add_book')
    path('books/add_book/', views.add_book, name='book_add'),

    # Edit an existing book (requires 'relationship_app.can_change_book')
    path('books/<int:pk>/edit_book/', views.edit_book, name='book_edit'),

    # Delete an existing book (requires 'relationship_app.can_delete_book')
    path('books/<int:pk>/delete/', views.delete_book, name='book_delete'),

]
