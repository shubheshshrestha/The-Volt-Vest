from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'

# class IsSupplierRole(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_autheticated and request.user.role == 'Supplier'
    
# class IsDeliveryRole(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'Delivery'