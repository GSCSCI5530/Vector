from django.db import models
from django.utils import timezone

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

class Comment(models.Model):
	event = models.ForeignKey('eventmanager.Event', on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	content = models.TextField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)
	
	def approve(self):
		self.approved = True
		self.save()
		
	def __str__(self):
		return self.content