from django.contrib import admin
from .models import Delivery, DeliveryPersonnel

# Register your models here.

admin.site.register(Delivery)   # Register the Delivery model with the admin site
admin.site.register(DeliveryPersonnel)