from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('eventmanager/<int:pk>/', views.event_detail, name='event_detail'),
    path('eventmanager/new', views.event_new, name='event_new'),
    path('eventmanager/<int:pk>/edit', views.event_edit, name='event_edit'),
]

