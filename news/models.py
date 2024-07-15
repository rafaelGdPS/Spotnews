from django.db import models

from news.validators import validate_length_title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_length_title]
        )
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_created=True)
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField(Category, related_name="news")

    def __str__(self) -> str:
        return self.title
