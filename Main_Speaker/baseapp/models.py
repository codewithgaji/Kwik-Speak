from django.db import models

# Create your models here.

class CommunicationTip(models.Model):
  tip_title = models.CharField(max_length=100)
  tip_content = models.TextField()
  tip_image = models.ImageField(upload_to="tips/images/", blank=True, null=True)
  tip_video = models.FileField(upload_to="tips/videos/", blank=True, null=True)

  def __str__(self):
    return self.tip_title
  

class Orators(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  image = models.ImageField(upload_to="home/images/", blank=True, null=True)
  content = models.TextField()
  
  def __str__(self):
    return self.name or "Unnamed Orator"


