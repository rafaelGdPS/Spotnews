from django.urls import path
from news.views import new


urlpatterns = [
  path("", new, name="home-page"),
]
