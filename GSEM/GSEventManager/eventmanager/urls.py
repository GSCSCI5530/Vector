from django.urls import path
from django.contrib.auth import authenticate
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('eventmanager/<int:pk>/', views.event_detail, name='event_detail'),
    path('eventmanager/new', views.event_new, name='event_new'),
    path('eventmanager/<int:pk>/edit', views.event_edit, name='event_edit'),
    path('eventmanager/search', views.event_search, name='event_search'),
    path('eventmanager/<int:pk>/attend_event/', views.attend_event, name='attend_event'),
    path('eventmanager/<int:pk>/comment', views.add_comment, name='add_comment'),
    path('eventmanager/<int:pk>/spam_redirect', views.add_comment, name='add_comment')
    # path('eventmanager/login/', views.login, name='login'),
]
