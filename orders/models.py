
from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    status = models.CharField(max_length=20, default='Pending')
