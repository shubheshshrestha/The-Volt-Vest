from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryPersonnelView, DeliveryView

router = DefaultRouter()

router.register(r'deliveries', DeliveryView, basename='delivery')
router.register(r'delivery-personnel', DeliveryPersonnelView, basename='delivery-personnel')

urlpatterns = [
    path('', include(router.urls))
]