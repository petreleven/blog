from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
  name = models.CharField(max_length=40)


class Article(models.Model):
  title = models.CharField(max_length = 50)
  image = models.ImageField(upload_to="media/articles", default="media/download.jpeg")
  content = models.TextField()
  published = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now = True)
  author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "articles")

  def __str__(self) -> str:
    return self.title


class Comment(models.Model):
  name = models.CharField(max_length=50)
  content = models.TextField()
  created = models.DateTimeField(auto_now_add = True)
  article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = "comments")

