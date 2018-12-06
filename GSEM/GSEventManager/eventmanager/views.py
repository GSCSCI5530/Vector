from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event, Comment, Attendee
from .forms import EventForm, CommentForm
from django.shortcuts import redirect

import re
import pickle
import numpy as np

# Create your views here.
def event_list(request):
    events = Event.objects.order_by('-created_date')
    return render(request, 'eventmanager/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = CommentForm()
    user = request.user.username
    attendees = Attendee.objects.filter(user_name=user)
    attending = False
    for attendee in attendees:
        if attendee.event_name == event.event_name:
            attending = True
        else:
            attending = False
    return render(request, 'eventmanager/event_detail.html', {'event': event, 'attending': attending, 'form': form})

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
        form = EventForm(request.POST,request.FILES or None, instance=event, )
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.published_date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'eventmanager/event_edit.html', {'form': form})
import re

def event_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        events = Event.objects.filter(event_name__icontains=q).order_by('-created_date')
        events.union(Event.objects.filter(text__icontains=q))
        # events = Event.objects.get(Q(event_name__icontains=q) | Q(text__icontains=q)).order_by('-created_date')
        return render(request, 'eventmanager/event_search.html', {'events': events, 'query': q})
    else:
        return redirect('event_list')

def censor(words):
    black_list = ["fuck", "shit", "piss", "damn", "ass", "cock", "balls", "nigger"] #Add words to censor here
    text = words
    patt = re.compile("|".join(black_list), re.I)
    return patt.sub(lambda m: "*" * len(m.group(0)) , text)

def check_spam(words): #1 = spam, 0 = not spam
    stopset = pickle.load(open("C:/Users/Chanukya Badri/Desktop/Vector/GSEM/GSEventManager/eventmanager/spamStopset.pkl", 'rb'))
    classifier = pickle.load(open("C:/Users/Chanukya Badri/Desktop/Vector/GSEM/GSEventManager/eventmanager/spamPickle.pkl", 'rb'))
    vectorizer = pickle.load(open("C:/Users/Chanukya Badri/Desktop/Vector/GSEM/GSEventManager/eventmanager/spamVectorizer.pkl", 'rb'))
    prediction = classifier.predict(vectorizer.transform(np.array([words])))
    return prediction[0]
	
def add_comment(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.user = request.user
            if check_spam(request.POST.get('content')) == 0:
                comment.content = censor(request.POST.get('content'))
            else:
                return render(request, 'eventmanager/spam_redirect.html') #redirects here if it is spam
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = CommentForm()
    return render(request, 'eventmanager/add_comment.html', {'form': form})


def attend_event(request, pk):
    if request.method == "GET":
        attendee = Attendee()
        event = get_object_or_404(Event, pk=pk)
        user = request.user
        attendee.event_name = event.event_name
        attendee.user_name = user.username
        attendee.user_email = user.email
        attendee.save()
        return redirect('event_list')
    else:
        return redirect('event_list')
		
