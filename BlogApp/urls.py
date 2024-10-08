from django.urls import path
from .views import homepage, article_content, search, createArticle, deleteArticle

urlpatterns = [
  path("", homepage, name="homepage"),
  path("content/<int:id>", article_content, name="article_content"),
  path("search", search, name="search"),
  path("createArticle/", createArticle, name="createArticle"),
  path("deleteArticle/<int:id>", deleteArticle, name="deleteArticle")
]
