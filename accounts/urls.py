from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, NotificationView #, AdminUserView

router = DefaultRouter()
# router.register(r'users', AdminUserView, basename='admin-users')
router.register(r'register', RegisterView, basename='register')
router.register(r'login', LoginView, basename='login')
router.register(r'notifications', NotificationView, basename='notifications')

urlpatterns = [
    path('', include(router.urls))
]