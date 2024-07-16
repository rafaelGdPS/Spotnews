from django.urls import path
from news.views import new, news_details, create_new_category


urlpatterns = [
  path("", new, name="home-page"),
  path("news/<int:id>", news_details, name="news-details-page"),
  path("categories/", create_new_category, name="categories-form")
]
