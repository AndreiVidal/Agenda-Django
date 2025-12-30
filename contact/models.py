from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True, null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='contacts',
                                 blank=True,
                                 null=True,
                                 )
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              )
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"