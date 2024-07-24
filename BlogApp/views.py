from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
  all_articles = Article.objects.all()
  return render(request, "homepage.html",{"all_articles" : all_articles})


def article_content(request, id):
  single_article = Article.objects.get(id=id)
  return render(request, "article_content.html", {"article":single_article})

def search(request):
  query = request.POST.get("searched_blog")
  filtered_articles = Article.objects.filter(title__contains = query)
  return render(request, "search.html", {"filtered":filtered_articles})


@login_required
def createArticle( request ):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES["image"]
        author = request.user
        #SAVE
        new_article = Article.objects.create(title = title, content=content, image = image,
            author=author)
        new_article.save()
    return render(request, "createArticle.html")

def  updateArticle(request, id):
    #Fetch the article being updated
    #rewrites the content with new content
    #save
    article_instance = Article.objects.get(pk=id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES["image"]
        article_instance.title = title
        article_instance.content = content
        article_instance.image = image
        article_instance.save()
    return render(request, "updateArticle.html", {
        "article" : article_instance
    })
