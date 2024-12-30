from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, permissions, views, generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import EventSerializer
from django.utils.timezone import now
from api.permissions import IsOwner
from rest_framework import filters
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ['username', 'email']

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['date_time'] < now():
            raise serializer.ValidationError("EVENT DATE CANNOT BE IN THE PAST.")
        serializer.save(organizer=self.request.user)

    def perform_update(self, serializer):
        if serializer.validated_data['date_time'] < now():
            raise serializer.ValidationError("EVENT DATE CANNOT BE IN THE PAST.")
        serializer.save()


class UpcomingEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ['title', 'location']

    def get_queryset(self):
        queryset = Event.objects.filter(date_time__gt=now())
        title = self.request.query_params.get('title', None)
        location = self.request.query_params.get('location', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if start_date and end_date:
            queryset = queryset.filter(date_time__range=[start_date, end_date])
        return queryset


class AddAttendeeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)
        if event.is_full:
            event.waitlist.add(request.user)
            return Response({'status': 'waitlisted'}, status=status.HTTP_200_OK)
        else:
            event.attendees.add(request.user)
            return Response({'status': 'registered'}, status=status.HTTP_200_OK)


class RemoveAttendeeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)
        event.attendees.remove(request.user)
        if request.user in event.waitlist.all():
            event.waitlist.remove(request.user)
        return Response({'status': 'unregistered'}, status=status.HTTP_200_OK)
