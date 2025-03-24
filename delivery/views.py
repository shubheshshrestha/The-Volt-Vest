from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from delivery.models import Delivery, DeliveryPersonnel
from delivery.serializers import DeliveryPersonnelSerializer, DeliverySerializer
from delivery.permissions import IsDelivery
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# Create your views here.

class DeliveryPersonnelView(viewsets.ModelViewSet):
    serializer_class = DeliveryPersonnelSerializer
    # permission_classes = [IsDelivery]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get_queryset(self):
        if self.request.user.is_staff: # If admin, return all
            return DeliveryPersonnel.objects.all()
        return DeliveryPersonnel.objects.filter(user=self.request.user) # Otherwise, return only their own
    
    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('delivery.add_deliverypersonnel'):
            return Response({"detail": "You do not have permission to add delivery personnel."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.has_perm('delivery.change_deliverypersonnel'):
            return Response({"detail": "You do not have permission to change delivery personnel."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('delivery.delete_deliverypersonnel'):
            return Response({"detail": "You do not have permission to delete delivery personnel."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeliveryView(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get_queryset(self):
        if self.request.user.is_staff:  # If admin, return all deliveries
            return Delivery.objects.all()
        
        try:
            delivery_personnel = DeliveryPersonnel.objects.get(user=self.request.user)
            return Delivery.objects.filter(delivery_personnel=delivery_personnel)
        except DeliveryPersonnel.DoesNotExist:
            return Delivery.objects.none()

    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('delivery.add_delivery'):
            return Response({"detail": "You do not have permission to add deliveries."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        delivery_instance = self.get_object()  # Get the Delivery instance
        
        # Allow admins to update any field
        # Allow delivery personnel to update ONLY their own delivery status
        if not (self.request.user.is_staff or
                (request.user.has_perm('delivery.change_delivery') and
                 delivery_instance.delivery_personnel.user == self.request.user and
                 'status' in request.data)):
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('delivery.delete_delivery'):
            return Response({"detail": "You do not have permission to delete deliveries."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        try:
            #  Get delivery_personnel from request data if provided, otherwise, assign to the user.
            delivery_personnel_id = self.request.data.get('delivery_personnel')
            if delivery_personnel_id:
                delivery_personnel = DeliveryPersonnel.objects.get(pk=delivery_personnel_id)
            else:
                delivery_personnel = DeliveryPersonnel.objects.get(user=self.request.user)
            serializer.save(delivery_personnel=delivery_personnel)
        except DeliveryPersonnel.DoesNotExist:
            return Response({"error": "No delivery personnel found for this user"}, status=status.HTTP_400_BAD_REQUEST)

    # def get_queryset(self):
    #     return Delivery.objects.filter(delivery_personnel__user=self.request.user)
    
    # def perform_create(self, serializer):
    #     try:
    #         delivery_personnel = DeliveryPersonnel.objects.get(user=self.request.user)
    #     except DeliveryPersonnel.DoesNotExist:
    #         return Response({"error": "No delivery personnel found for this user"}, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save(delivery_personnel=delivery_personnel)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # Assign the delivery personnel based on the authenticated user
    #     delivery_personnel = DeliveryPersonnel.objects.get(user=request.user)
    #     serializer.save(delivery_personnel=delivery_personnel)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)