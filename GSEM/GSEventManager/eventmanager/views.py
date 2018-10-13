from django.shortcuts import render
from django.utils import timezone
from .models import Event

# Create your views here.


def event_list(request):
    events = Event.objects.order_by('published_date')
    return render(request, 'eventmanager/event_list.html', {'events': events})
