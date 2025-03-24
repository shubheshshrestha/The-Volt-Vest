from rest_framework import serializers
from .models import Product
from suppliers.serializers import SupplierSerializer

class ProductSerializer(serializers.ModelSerializer):
    supplier_details = SupplierSerializer(source='supplier', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'supplier', 'supplier_details']
        read_only_fields = ['supplier']