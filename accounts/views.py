from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from .models import Notification
from .serializers import UserSerializer, LoginSerializer, NotificationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
# from .permissions import IsAdmin #, IsDelivery, IsSupplier

# Create your views here.

User = get_user_model()

class RegisterView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    # def get_queryset(self):
    #   return User.objects.filter(is_staff=True)        

    def create(self, request):
        serializer = UserSerializer(data=request.data)                                                                  

        if serializer.is_valid():
            serializer.save() # calls the serializer's 'create' method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []

    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'detail':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            token,_ = Token.objects.get_or_create(user=user) # Generate or retrieve token
            return Response({'token':token.key}, status=status.HTTP_200_OK)
class NotificationView(ModelViewSet):
    # queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show notification for logged-in user
        return Notification.objects.filter(user=self.request.user)
    
# class AdminUserView(ModelViewSet):  # ReadOnlyModelViewSet if  only read access needed
#     queryset = User.objects.filter(role='Admin')
#     serializer_class = UserSerializer
#     permission_classes = [IsAdmin] # Restrict access to users with role = Admin

# class SupplierView(ModelViewSet):
#     queryset = 
