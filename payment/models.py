from django.db import models

from borrowing.models import Borrowing


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'PENDING'
        PAID = 'PAID', 'PAID'

    class TypeChoices(models.TextChoices):
        PAYMENT  = 'PAYMENT', 'PAYMENT'
        FINE = 'FINE', 'FINE'

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        default=TypeChoices.PAYMENT
    )

    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE, related_name="payments")

    def __str__(self):
        return f"{self.type} - {self.status} for Borrowing: {self.borrowing_id}"
