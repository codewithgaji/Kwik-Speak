from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm # The Custom form I created

# Create your views here.




# This is the Signup view
def signup_view(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("baseapp:home")

  else:
    form = CustomUserCreationForm()

  context = {
    "form_key": form
  }

  return render(request, "registration/signup.html", context)

