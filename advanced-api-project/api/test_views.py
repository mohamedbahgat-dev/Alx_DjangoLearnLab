from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create a sample book
        self.book = Book.objects.create(
            title="Clean Code",
            author="Robert C. Martin",
            published_date="2008-08-01",
            isbn="9780132350884"
        )

        # Define URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    # 📘 1. Test listing books (public access)
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Clean Code")

    # 📖 2. Test retrieving a single book (public access)
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Clean Code")

    # 🧪 3. Test creating a book without authentication (should fail)
    def test_create_book_unauthenticated(self):
        data = {
            "title": "The Pragmatic Programmer",
            "author": "Andy Hunt",
            "published_date": "1999-10-30",
            "isbn": "9780201616224"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ✅ 4. Test creating a book with authentication (should succeed)
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "The Pragmatic Programmer",
            "author": "Andy Hunt",
            "published_date": "1999-10-30",
            "isbn": "9780201616224"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['book']['title'], "The Pragmatic Programmer")
        self.assertTrue(Book.objects.filter(isbn="9780201616224").exists())

    # ✏️ 5. Test updating a book (authenticated)
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Clean Code - Updated"}
        response = self.client.patch(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Clean Code - Updated")

    # ❌ 6. Test updating a book without authentication (should fail)
    def test_update_book_unauthenticated(self):
        data = {"title": "Unauthorized Update"}
        response = self.client.patch(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 🗑️ 7. Test deleting a book (authenticated)
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # ❌ 8. Test deleting a book without authentication (should fail)
    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
