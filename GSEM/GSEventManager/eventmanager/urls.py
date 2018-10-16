from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('eventmanager/<int:pk>/', views.event_detail, name='event_detail'),
]

