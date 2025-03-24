from rest_framework import permissions

class IsDelivery(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user.role == 'deliverypersonnel')