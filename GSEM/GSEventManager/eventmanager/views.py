from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event

# Create your views here.


def event_list(request):
    events = Event.objects.order_by('created_date')
    return render(request, 'eventmanager/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'eventmanager/event_detail.html', {'event': event})
