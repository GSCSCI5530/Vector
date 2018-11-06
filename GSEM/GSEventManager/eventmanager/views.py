from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event, Comment
from .forms import EventForm, CommentForm
from django.shortcuts import redirect


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


def event_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        events = Event.objects.filter(event_name__icontains=q).order_by('-created_date')
        events.union(Event.objects.filter(text__icontains=q))
        # events = Event.objects.get(Q(event_name__icontains=q) | Q(text__icontains=q)).order_by('-created_date')
        return render(request, 'eventmanager/event_search.html', {'events': events, 'query': q})
    else:
        return redirect('event_list')
		
def add_comment(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = CommentForm()
    return render(request, 'eventmanager/add_comment.html', {'form': form})
	

