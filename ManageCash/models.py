from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.display_name} - {self.username}'

class AddCash(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cash')
    source = models.CharField(max_length=255, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.source} - {self.amount} - {self.user.username}'

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.amount} - {self.description} - {self.user.username}'