from rest_framework import serializers
from delivery.models import DeliveryPersonnel, Delivery
from orders.serializers import OrderSerializer

class DeliveryPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPersonnel
        fields = ['id', 'user', 'vehicle_type', 'license_number', 'available']      # Specify the fields to include in the serialization
        read_only_fields = ['user']

class DeliverySerializer(serializers.ModelSerializer):
    order_details = OrderSerializer(source='order', read_only=True)     # Serialize the related 'order' field using OrderSerializer, make it read-only
    delivery_personnel_details = DeliveryPersonnelSerializer(source='delivery_personnel', read_only=True)

    class Meta:
        model = Delivery
        fields = ['id', 'order', 'order_details', 'delivery_personnel', 'delivery_personnel_details', 'status', 'tracking_number', 'delivered_at', 'created_at', 'updated_at']  