from django.db import models
from django.contrib.auth import get_user_model
from suppliers.models import Supplier

# Create your models here.

User = get_user_model()
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

        permissions = [
            ('can_add_product', 'Can add product'),
            ('can_change_product', 'Can change product'),
            ('can_delete_product', 'Can delete product'),
            ('can_view_product', 'Can view product'),
        ]
        