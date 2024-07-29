from django.contrib import admin
from .models import Article, Author
from django.contrib.auth.admin import UserAdmin
from .forms import AuthorCreationForm, AuthorChangeForm

#OUR ADMIN IS ALSO AN AUTHOR MODEL
#HENCE WE HAVE TO TELL DJANGO THIS
class CustomAdmin(UserAdmin):
    #which form to use when creating a superuser
    add_form = AuthorCreationForm
    form = AuthorChangeForm
    model = Author
#view custom admins in localhost:8000/admin
admin.site.register(Author, CustomAdmin)
#py manage.py makemigrations
#py manage.py migrate


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  list_display = ["title", "published", "updated"]
