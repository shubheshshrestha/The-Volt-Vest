from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import CustomerProfile
from .serializers import CustomerProfileSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import status

class CustomerProfileView(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomerProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if CustomerProfile.objects.filter(user=request.user).exists():
            return Response({"error": "Customer profile already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
# class CustomerProfileView(viewsets.ModelViewSet):
#     serializer_class = CustomerProfileSerializer
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsCustomer]

#     def get_queryset(self):
#         return CustomerProfile.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
