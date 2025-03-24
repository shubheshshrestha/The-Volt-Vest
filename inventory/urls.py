from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryLogView

router = DefaultRouter()
router.register(r'inventory-log', InventoryLogView, basename='inventory-log')

urlpatterns = [
    path('', include(router.urls))
]