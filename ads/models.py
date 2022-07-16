from django.db import models


class AdModel(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    description = models.TextField(max_length=1000, null=True)
    price = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)


class CategoryModel(models.Model):
    name = models.CharField(max_length=20)
