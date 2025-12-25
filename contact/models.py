from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)