from django.shortcuts import render
from rest_framework import serializers, permissions
from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsSupplier
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.db import IntegrityError

# Create your views here.
class SupplierView(ModelViewSet):
    # queryset = Supplier.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    serializer_class = SupplierSerializer
    permission_classes = [IsSupplier]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Supplier.objects.none()
        return Supplier.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class SupplierCreateView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def create(self, request):
        try:
            serializer = SupplierSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)  # Associate the current user
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise serializers.ValidationError({"error": "Already created with this id."})   # Raise a validation error if a Supplier with the same ID already exists