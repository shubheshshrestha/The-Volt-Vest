from rest_framework import permissions

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if user has a linked Supplier profile or has the 'Supplier' role
        return request.user.is_authenticated and hasattr(request.user, 'customerprofile')
    

# # Recommendation:
# If the IsCustomer permission is only used within the customers app, it's fine to keep it there. 
# However, if multiple apps need to use this permission (e.g., orders, notifications), 
# consider moving it to the accounts app to centralize role-based permissions.