from django.db import models
from accounts.views import User
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

User = get_user_model()
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supplier')
    company_name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_name
    


    # website = models.URLField(blank=True, null=True)
    # logo = models.ImageField(upload_to='supplier_logos/', blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    # bank_account = models.CharField(max_length=100, blank=True, null=True)
    # tax_id = models.CharField(max_length=50, blank=True, null=True)