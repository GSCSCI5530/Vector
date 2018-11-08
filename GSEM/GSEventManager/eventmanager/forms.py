from django import forms
from .models import Event, Comment


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'text', 'event_date', 'event_place')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
