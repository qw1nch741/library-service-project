from django.db import models

class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = 'HARD', 'Hardcover'
        SOFT = 'SOFT', 'Softcover'

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=4,
        choices=CoverChoices.choices,
        default=CoverChoices.HARD
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        # This prevents duplicate books by the same author
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_book_author'
            )
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"
