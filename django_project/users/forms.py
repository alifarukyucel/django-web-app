from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # nested namespace for configurations
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # Called a model form because it interacts with a database model (entity)
    email = forms.EmailField()

    class Meta:  # nested namespace for configurations
        model = User
        fields = ['username', 'email']
