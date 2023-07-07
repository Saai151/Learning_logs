from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Entry
from .forms import TopicForm
from .forms import EntryForm
# Create your views here.


def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics' : topics}    
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    #Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #NO data has been submitted; create a blank form.
        form = TopicForm()
    else:
        #POST data submitted, so process that data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entries(request, topic_id):
    """Add a new entry"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # NO data has been submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted, so process that data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', kwargs={'topic_id': topic_id}))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entries.html', context)

@login_required
def edit_entry(request, entry_id):
    """Editing an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #NO data has been submitted, so keep the current entry
        form = EntryForm(instance=entry)
    else:
        #POST data has ben submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic , 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

