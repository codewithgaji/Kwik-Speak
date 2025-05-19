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


# This is the Signup view
def autview(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      redirect("baseapp:home")

  else:
    form = UserCreationForm()

  context = {
    "form_key": form
  }

  return render(request, "registration/signup.html", context)

