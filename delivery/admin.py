from django.contrib import admin
from .models import Delivery, DeliveryPersonnel

# Register your models here.

admin.site.register(Delivery)
admin.site.register(DeliveryPersonnel)