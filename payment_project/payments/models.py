from django.db import models

class Item(models.Model):
    CURRENCY_CHOICES = [
        ('usd', 'USD'),
        ('eur', 'EUR'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name
