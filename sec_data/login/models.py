from django.db import models

class LoginAttempt(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
