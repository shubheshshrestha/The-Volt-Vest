from rest_framework import permissions

class IsAdmin(permissions.BasePermission):      # Define a custom permission class
    def has_permission(self, request, view):    # Check if user is authenticated AND has 'Admin' role
        return request.user.is_authenticated and request.user.role == 'Admin'   # Check if user is authenticated AND has 'Admin' role

# class IsSupplierRole(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_autheticated and request.user.role == 'Supplier'
    
# class IsDeliveryRole(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'Delivery'