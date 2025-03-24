from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from inventory.models import InventoryLog
from inventory.serializers import InventoryLogSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import permission_classes

class InventoryLogView(viewsets.ModelViewSet):
    serializer_class = InventoryLogSerializer
    authentication_classes = [
        SessionAuthentication,
        TokenAuthentication
    ]
    #  permission_classes = [IsSupplier]  #  Remove custom permission
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:  #  Admin
            return InventoryLog.objects.all()  #  Admins see all
        elif hasattr(user, 'supplier'):  #  Supplier
            #  Filter logs for the supplier's products
            return InventoryLog.objects.filter(
                product__supplier=user.supplier
            )
        else:
            return InventoryLog.objects.none()  #  Other users see none
    def create(self, request, *args, **kwargs):
        print("--- Create View ---")
        print(f"Authentication Header: {request.META.get('HTTP_AUTHORIZATION')}")
        print(f"User Authenticated: {request.user.is_authenticated}")
        print(f"User: {request.user}")  #   Print the entire user object
        print(f"User Permissions: {request.user.get_all_permissions()}")  #   Print all permissions

        if not request.user.has_perm('inventory.can_add_inventorylog'):
            print("Permission check failed!")  #  Indicate permission failure
            return Response(
                {"error": "You do not have permission to add inventory logs."},
                status=status.HTTP_403_FORBIDDEN
            )
        print("Permission check passed!")  #  Indicate permission success
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data['product']
        print(f"Product ID from request: {product.id}")  #  Print the product ID

        #   Check product ownership
        if product.supplier != request.user.supplier:  #  Use user.supplier
            print("Product ownership check failed!")  #  Indicate ownership failure
            return Response(
                {"error": "You do not own this product"},
                status=status.HTTP_403_FORBIDDEN
            )
        print("Product ownership check passed!")  #  Indicate ownership success

        action = serializer.validated_data['action']
        quantity = serializer.validated_data['quantity']

        #   Update product stock based on inventory action
        if action == 'increase':
            product.stock += quantity
        elif action == 'decrease':
            if product.stock < quantity:
                return Response(
                    {"error": "Insufficient stock"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            product.stock -= quantity
        else:
            return Response(
                {"error": "Invalid action"},
                status=status.HTTP_400_BAD_REQUEST
            )  #  Handle invalid action

        product.save()

        #   Save the inventory log and return response
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
        print(request.META.get('HTTP_AUTHORIZATION'))
        print(request.user.is_authenticated)

# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from inventory.models import InventoryLog
# from inventory.serializers import InventoryLogSerializer
# from suppliers.permissions import IsSupplier
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes

# # Create your views here.

# class InventoryLogView(viewsets.ModelViewSet):
#     serializer_class = InventoryLogSerializer
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     # permission_classes = [IsSupplier]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return InventoryLog.objects.filter(product__supplier=self.request.user)
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         product = serializer.validated_data['product']
#         # if product.supplier != request.user:
#         #     return Response({"error": "You do not own this product"}, status=status.HTTP_403_FORBIDDEN)
        
#         # Update product stock based on inventory action
#         if serializer.validated_data['action'] == 'increase':
#             product.stock += serializer.validated_data['quantity']
#         elif serializer.validated_data['action'] == 'decrease':
#             product.stock -= serializer.validated_data['quantity']
#         product.save()

#         # Save the inventory-log and return response
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)