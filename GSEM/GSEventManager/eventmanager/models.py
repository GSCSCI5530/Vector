from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    event_date = models.DateTimeField(default=timezone.now)
    event_place = models.CharField(max_length=200)

    def post(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name


class Attendee(models.Model):
    # event = models.ForeignKey('Event', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    # user_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def attend(self):
        self.save()

