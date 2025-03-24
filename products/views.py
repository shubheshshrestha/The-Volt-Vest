from rest_framework import viewsets, permissions, filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import permission_classes
from rest_framework.response import Response  # Import Response

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = [
        SessionAuthentication,
        TokenAuthentication
    ]
    #  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticated]

    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'stock']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  #  Admin can see all products
            return Product.objects.all()
        elif user.is_authenticated:  # Authenticated users
            return Product.objects.all()
        else:  #  Unauthenticated users (Customers)
            return Product.objects.filter(
                stock__gt=0
            )  #  Only show products with stock greater than 0
    
    def perform_create(self, serializer):
        serializer.save(supplier=self.request.user.supplier) # Set the supplier



# from django.shortcuts import render
# from rest_framework import viewsets, permissions, filters
# from .models import Product
# from .serializers import ProductSerializer
# from suppliers.permissions import IsSupplier
# from suppliers.models import Supplier
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication
# from rest_framework.pagination import PageNumberPagination

# # Create your views here.

# class ProductView(viewsets.ModelViewSet):
#     # queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsSupplier]
#     pagination_class = PageNumberPagination
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['name', 'description']
#     ordering_fields = ['price', 'stock']

#     def get_queryset(self):
#         try:
#             supplier = Supplier.objects.get(user=self.request.user)
#             return Product.objects.filter(supplier=supplier)
#         except Supplier.DoesNotExist:
#             return Product.objects.none()
#         # return Product.objects.filter(supplier=self.request.user)
    
#     def perform_create(self, serializer):
#         try:
#             supplier = Supplier.objects.get(user=self.request.user)
#             serializer.save(supplier=supplier)
#         except Supplier.DoesNotExist:
#             pass 
#         # serializer.save(supplier=self.request.user)
        