from . import views
from django.urls import path

app_name = 'lessons' # For namespacing

urlpatterns = [
  path("", views.lessons,  name="lessons")
]