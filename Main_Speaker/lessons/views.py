from django.shortcuts import render
from .models import Lesson, LessonProgress, Category
# Create your views here.


def lessons(request):
  category  = Category.objects.all()
  lessons = Lesson.objects.all()
  progress = LessonProgress.objects.all

  context = {
    "category": category,
    "lessons": lessons,
    "progress": progress,
  }
  return render(request, "lessons.html", context)