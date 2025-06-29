from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import CommunicationTip, Orators

# Create your views here.

# Home view
@login_required
def home(request):
  tips = CommunicationTip.objects.all()
  orator = Orators.objects.all()
  context = {
    "tips" : tips,
    "orator" : orator
  }

  return render(request, "home.html", context)


