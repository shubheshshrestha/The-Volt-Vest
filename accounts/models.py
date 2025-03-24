from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# User Profile and Authentication
class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[
        ('Supplier', 'Supplier'),
        ('Customer', 'Customer'),
        ('Delivery', 'Delivery')
    ])
    
    # def save(self, *args, **kwargs):
    #     if self.role == 'Admin':  # if self.role in ['Admin', 'Supplier']
    #         self.is_staff = True
    #         self.is_superuser = True
    #     else:
    #         self.is_staff = False
    #         self.is_superuser = False
    #     super().save(*args, **kwargs)

# User Notifications
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
