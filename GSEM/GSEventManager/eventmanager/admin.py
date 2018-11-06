from django.contrib import admin
from .models import Event, Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Event)
