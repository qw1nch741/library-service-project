import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from borrowings.models import Borrowing

class AuthenticatedBorrowingApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="password"
        )
        self.client.force_authenticate(self.user)

        self.book = Book.objects.create(
            title="Django Advanced", inventory=2, daily_fee=1.5
        )

    def test_list_borrowings_returns_only_own(self):
        Borrowing.objects.create(
            expected_return_date=datetime.date.today(),
            book=self.book,
            user=self.user
        )

        url = reverse("borrowings:borrowing-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_borrowing_decreases_inventory(self):
        url = reverse("borrowings:borrowing-list")

        payload = {
            "book": self.book.id,
            "expected_return_date": datetime.date.today() + datetime.timedelta(days=5)
        }

        response = self.client.post(url, data=payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.book.refresh_from_db()

        self.assertEqual(self.book.inventory, 1)
