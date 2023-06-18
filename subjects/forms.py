from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', )


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password' , )  
        widgets = { 'username': forms.TextInput(attrs={'class': 'form-control text-center'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control text-center'})
        }      