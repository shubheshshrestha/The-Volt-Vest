from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order
# Create your models here.

User = get_user_model()

class DeliveryPersonnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_personnel = models.ForeignKey(DeliveryPersonnel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Delivery for order {self.order.id}"
    
    permissions = [
            ('view_delivery', 'Can view delivery'),
            ('add_delivery', 'Can add delivery'),
            ('change_delivery', 'Can change delivery'),
            ('delete_delivery', 'Can delete delivery'),
            ('assign_delivery', 'Can assign delivery'),  # Custom permission
            ('update_delivery_status', 'Can update delivery status'),  # Custom permission
        ]
