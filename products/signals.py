from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
from accounts.models import Notification

@receiver(post_save, sender=Product) # The @receiver decorator connects the check_stock function to the post_save signal for the Product model.
def check_stock(sender, instance, **kwargs):
    if instance.stock < 5:
        Notification.objects.create(user=instance.supplier, message=f"Low stock alert for {instance.name} (Current stock: {instance.stock})")