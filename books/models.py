from django.db import models

# Create your models here.
from django.db import models
import time


# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=120, null=True)
    writer = models.CharField(max_length=120, null=True)
    subject = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=120, null=True)
    family = models.CharField(max_length=120, null=True)
    age = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name


class librarian(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user


class reserve(models.Model):
    book_name = models.ForeignKey(book, on_delete=models.CASCADE, null=True)
    transferee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    trash=models.BooleanField(default=False)

    def __str__(self):
        return self.book
