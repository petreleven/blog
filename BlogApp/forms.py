from BlogApp.models import Author
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #the custom model we are using
        model = Author

class AuthorChangeForm(UserChangeForm):
    class Meta:
        # firstname, secondname, email etc
        fields = UserCreationForm.Meta.fields
