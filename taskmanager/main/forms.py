from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class UserLoginForm (AuthenticationForm):
    username = forms.CharField(label="Никнейм",widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"class": "form-control"}))

class UserRegisterForm (UserCreationForm):
    username = forms.CharField(label="Никнейм",widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="Имя",widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ( "username", "first_name", "last_name","email","password1", "password2")


class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image']


