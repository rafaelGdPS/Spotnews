from django.urls import path
from news.views import new, news_details


urlpatterns = [
  path("", new, name="home-page"),
  path("news/<int:id>", news_details, name="news-details-page"),
]
