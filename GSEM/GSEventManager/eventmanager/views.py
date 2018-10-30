from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from .forms import EventForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def event_list(request):
    events = Event.objects.order_by('-created_date')
    return render(request, 'eventmanager/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'eventmanager/event_detail.html', {'event': event})


def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.published_date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'eventmanager/event_edit.html', {'form': form})


def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.published_date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'eventmanager/event_edit.html', {'form': form})
