from django.shortcuts import render
from .models import UserProfile
from rest_framework import generics, permissions
from .permissions import IsUserOwnerOrReadOnly
from .serializers import UserProfileSerializer
# Create your views here.
class UserList(generics.ListAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserDetail(generics.RetrieveDestroyAPIView):
    permission_classes=[IsUserOwnerOrReadOnly]
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
    permission_classes=[IsUserOwnerOrReadOnly]
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

