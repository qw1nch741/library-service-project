import datetime

from django.test import TestCase
from borrowings.models import Borrowing, Book
from django.contrib.auth import get_user_model


User = get_user_model()

class BorrowingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="password")
        self.book = Book.objects.create(title="Test Book", inventory=5, daily_fee=1.0)
        self.borrowing = Borrowing.objects.create(
            expected_return_date=datetime.date.today(),
            book=self.book,
            user=self.user
        )

    def test_borrowing_str(self):
        expected_str = "Test Book (borrowed by test@test.com)"
        self.assertEqual(str(self.borrowing), expected_str)

    def test_borrow_date_is_set_automatically(self):
        expected_borrow_date = datetime.date.today()
        self.assertEqual(self.borrowing.borrow_date, expected_borrow_date)
