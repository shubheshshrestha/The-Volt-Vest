from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerProfileView

router = DefaultRouter()
router.register(r'customer-profile', CustomerProfileView, basename='customer-profile')

urlpatterns = [
    path('', include(router.urls))
]