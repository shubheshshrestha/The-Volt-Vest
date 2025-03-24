from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierOrderView, CustomerOrderView

router = DefaultRouter()
router.register(r'supplier-orders', SupplierOrderView, basename='supplier-order')
router.register(r'customer-orders', CustomerOrderView, basename='customer-order')

urlpatterns = [
    path('', include(router.urls))
]