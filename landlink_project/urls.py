"""
URL configuration for landlink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from accounts.views import RegisterView, LoginView, NotificationView, AdminUserView
# from suppliers.views import SupplierView
# from products.views import ProductView
# from orders.views import OrderView
# from delivery.views import DeliveryPersonnelView, DeliveryView
# from customers.views import CustomerProfileView
# from inventory.views import InventoryLogView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('suppliers.urls')),
    path('api/', include('products.urls')),
    path('api/', include('inventory.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('delivery.urls')),
    path('api/', include('customers.urls')),
]
# router = DefaultRouter()
# router.register(r'users', AdminUserView, basename='admin-users')
# router.register(r'register', RegisterView, basename='register')
# router.register(r'login', LoginView, basename='login')
# router.register(r'notifications', NotificationView, basename='notifications')
# router.register(r'suppliers', SupplierView, basename='suppliers') # Use basename= when there is GenericViewSet
# router.register(r'products', ProductView, basename='products')
# router.register(r'inventory-log', InventoryLogView, basename='inventory-log')
# router.register(r'orders', OrderView, basename='orders')
# router.register(r'delivery', DeliveryView, basename='delivery')
# router.register(r'delivery-personnel', DeliveryPersonnelView, basename='delivery-personnel')
# router.register(r'customer-profile', CustomerProfileView, basename='customer-profile')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)), # All API endpoints under /api/
#     # path('api/analytics/', include('analytics.urls')),
# ]
