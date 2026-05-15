from django.db import models

class Book(models.Model):
    class CoverChoices(models.TextChoices):
        HARD = 'HARD', 'Hardcover'
        SOFT = 'SOFT', 'Softcover'

    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255, unique=True)
    cover = models.CharField(
        max_length=4,
        choices=CoverChoices.choices,
        default=CoverChoices.HARD
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField()

