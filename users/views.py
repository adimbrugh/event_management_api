from django.shortcuts import render

# Create your views here.


from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from api.permissions import IsOwner
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ['username', 'email']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = [AllowAny]
        #return User(UserViewSet, self).get_permissions()
        return [permission() for permission in self.permission_classes]
