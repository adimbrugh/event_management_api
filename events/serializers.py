

from rest_framework import serializers
from django.utils.timezone import now
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['organizer', 'created_date']


    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("TITLE IS REQUIRED.")
        return value

    def validate_date_time(self, value):
        if value < now():
            raise serializers.ValidationError("EVENT DATE CANNOT BE IN THE PAST.")
        return value

    def validate_location(salf, value):
        if not value:
            raise serializers.ValidationError("LOCATION IS REQUIRED.")
        return value