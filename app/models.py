from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('Fruit', 'Fruit'),
    ('Vegetables', 'Vegetables'),
    ('Meat', 'Meat'),
]


class Product(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="media")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
