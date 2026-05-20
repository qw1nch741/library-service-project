from django.db import models

from borrowings.models import Borrowing


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

    session_url = models.URLField(max_length=10000, blank=True, null=True)

    session_id = models.CharField(max_length=255, blank=True, null=True)

    money_to_pay = models.DecimalField(max_digits=8, decimal_places=2)

    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE, related_name="payments")


    def __str__(self):
        return f"{self.type} - {self.status} for Borrowing: {self.borrowing_id}"
