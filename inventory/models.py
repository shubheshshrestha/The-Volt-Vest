from django.db import models
from products.models import Product

# Create your models here.

class InventoryLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    action = models.CharField(max_length=20, choices=[('increase', 'Increase'), ('decrease', 'Decrease')])
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} ({self.action})"
    
    class Meta:
          permissions = [
              ('can_view_inventorylog', 'Can view inventory log'),
              ('can_add_inventorylog', 'Can add inventory log'),
              ('can_change_inventorylog', 'Can change inventory log'),
              ('can_delete_inventorylog', 'Can delete inventory log'),
          ]