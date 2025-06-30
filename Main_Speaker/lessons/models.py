from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model): # TO determine the type of lesson wanted, maybe (video based or article based)
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name



# The lesson class for whatever type of lesson uploaded
class Lesson(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'lessons')
  title = models.CharField(max_length=250)
  video_url = models.URLField(blank=True, null = True)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  is_published = models.BooleanField(default=False)
  image = models.ImageField(upload_to="lessons/previews/", blank=True, null=True)

  def __str__(self):
    return self.title
  

# Lesson Progress class
class LessonProgress(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  completed = models.BooleanField(default=False)
  last_viewed = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.user.email} - {self.lesson.title} - {'Done' if self.completed else 'In Progress'}"




