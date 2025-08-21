from django.shortcuts import render

# Create your views here.
# registration/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .models import Event, Registration

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'registration/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Check if the current user is already registered
    is_registered = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(user=request.user, event=event).exists()
    return render(request, 'registration/event_detail.html', {'event': event, 'is_registered': is_registered})

@login_required
def event_register(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    try:
        # Create the registration
        Registration.objects.create(user=request.user, event=event)
        messages.success(request, f'You have successfully registered for "{event.title}".')
    except IntegrityError:
        # This happens if the unique_together constraint fails
        messages.warning(request, f'You are already registered for "{event.title}".')

    return redirect('event_detail', event_id=event.id)

@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user).order_by('event__date')
    return render(request, 'registration/my_registrations.html', {'registrations': registrations})