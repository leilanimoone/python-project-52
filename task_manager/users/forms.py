from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from .models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(label=_("First Name"))
    last_name = forms.CharField(label=_("Last Name"))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
