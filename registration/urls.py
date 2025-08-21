# registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.event_register, name='event_register'),
    path('my_registrations/', views.my_registrations, name='my_registrations'),
]