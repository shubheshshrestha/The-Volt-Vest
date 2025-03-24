from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['company_name', 'address', 'phone_number']
        # read_only_fields = ['user']
        # extra_kwargs = {
        #     'phone_number': {'required': True}
        # }
