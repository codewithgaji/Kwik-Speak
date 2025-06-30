from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "home"

urlpatterns = [
  path("", views.landing_page, name="landing_page"),
  path("home/", views.home, name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)