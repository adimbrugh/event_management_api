

from django.contrib.auth.models import User
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the obj is an Event and ensure the organizer is the request user
        if isinstance(obj, User):
            return obj == request.user
        return obj.organizer == request.user
