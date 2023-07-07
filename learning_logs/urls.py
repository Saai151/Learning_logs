"""Defines URL patters for learning_logs."""

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    #Show all topics
    path('topics/', views.topics, name='topics'),

    #Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #This is a page that will be used to add new topics
    path('new_topic/', views.new_topic, name = 'new_topic'),

    #This is a page that will be used to add new entries
    path('new_entries/<int:topic_id>', views.new_entries, name = 'new_entries'),

    #This is a page for edditing existing entries
    path('edit_entry/<int:entry_id>', views.edit_entry, name = 'edit_entry'),
]
