from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

# Home view
@login_required
def home(request):
  return render(request, "home.html",  {})


