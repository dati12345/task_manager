from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm)
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
        class Meta:
            fields = ['username', 'email', 'password1', 'password2']
            model = User

class UserLoginForm(AuthenticationForm):
        class Meta:
            fields = ['username', 'password']
            model = User