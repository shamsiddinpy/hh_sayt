# Create your models here.

# class VerificationCode(models.Model):
#     email = models.EmailField(unique=True)
#     code = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.email} - {self.code}'


from django.db import models
from django.utils import timezone


class VerificationCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
