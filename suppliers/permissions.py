from rest_framework import permissions

class  IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'supplier')
    
class IsSupplierOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Use permissions.SAFE_METHODS # permissions.SAFE_METHODS is a built-in shortcut for ('GET', 'HEAD', 'OPTIONS')
            return True
        # if request.method in ['GET', 'HEAD', 'OPTIONS']:
        #     return True
        return request.user.is_authenticated and hasattr(request.user, 'supplier')