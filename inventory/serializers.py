from rest_framework import serializers
from inventory.models import InventoryLog

class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = ['id', 'product', 'quantity', 'action', 'created_at', 'notes']