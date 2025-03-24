from rest_framework import serializers
from customers.models import CustomerProfile
from django.contrib.auth import get_user_model

# User = get_user_model()

class CustomerProfileSerializer(serializers.ModelSerializer):
    # user_details = serializers.SerializerMethodField()
    class Meta:
        model = CustomerProfile
        fields = ['id', 'shipping_address', 'billing_address', 'phone_number']
        read_only_fields = ['id']

    # def get_user_details(self, obj):
    #     return {
    #         'id': obj.user.id,
    #         'username': obj.user.username,
    #         'email': obj.user.email
    #     }