from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import stock_user

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=40,label="Username",widget=forms.TextInput(attrs={
        'placeholder':'Username',
        'autocomplete':'off'
        }))

    password1 = forms.CharField(max_length=40,label='Password',widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'autocomplete':'off',
        'type':'password',
    }))

    password2 = forms.CharField(max_length=40,label='Password Again',widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'autocomplete':'off',
        'type':'password',
    }))

    class Meta:
        model = stock_user
        fields = ('username','password1','password2')    