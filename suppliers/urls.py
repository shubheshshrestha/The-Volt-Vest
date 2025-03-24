from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierView, SupplierCreateView

router = DefaultRouter()
router.register(r'suppliers', SupplierView, basename='supplier')
router.register(r'supplier-create', SupplierCreateView, basename='supplier-create')

urlpatterns = [
    path('', include(router.urls))
]
