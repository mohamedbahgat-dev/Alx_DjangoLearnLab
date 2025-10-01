from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CustomeCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']