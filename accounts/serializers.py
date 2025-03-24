from rest_framework import serializers
from .models import User, Notification
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'is_staff']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
            },
            'username': {
                'required': True
            } 
        }

    def validate_password(self, value):
        # Validate password complexity requirements
        # Validate password complexity requirements
        # password_validation.validate_password(value)  # Use Django's built-in validators
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters.')
        return value
    
    def create(self, validated_data):
        # Hash password and allow 'is_staff' to be  set via API
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at']