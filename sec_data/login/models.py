from django.db import models

class LoginAttempt(models.Model):
    # logging login details
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class PageVisit(models.Model):
    # number of visits
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.path} at {self.timestamp}"

