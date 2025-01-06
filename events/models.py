from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField(User, related_name='events', blank=True)
    waitlist = models.ManyToManyField(User, related_name='waitlisted_events', blank=True)

    def __str__(self):
        return self.title

    @property
    #Ensure that each event has a maximum capacity, and when the capacity is reached, new attendees cannot register.
    def is_full(self):
        return self.attendees.count() >= self.capacity

    #Prevent users from creating events with past dates
    def save(self, *args, **kwargs): 
        if self.date_time < timezone.now(): 
            raise ValueError("Event date cannot be in the past.") 
        super().save(*args, **kwargs)