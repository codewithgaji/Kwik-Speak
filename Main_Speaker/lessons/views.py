from django.shortcuts import render

# Create your views here.


def lessons(request):
  return render(request, "lessons.html", {})