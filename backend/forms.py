from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django import forms
from django.contrib.auth import login, authenticate
from backend.models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             help_text='Это поле обязательно')
    username = forms.CharField(min_length=3,
                               max_length=20,
                               help_text='Длина логина должна быть не меньше 3-х и не больше 20',
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Логин:')
    password1 = forms.CharField(min_length=6,
                               max_length=35,
                               help_text='Длина пароля должна быть не меньше 6 и не больше 35',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Пароль:')
    password2 = forms.CharField(min_length=6,
                               max_length=35,
                               help_text='Длина пароля должна быть не меньше 6 и не больше 35',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Повторите пароль:')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(min_length=3,
                               max_length=20,
                               help_text='Длина логина должна быть не меньше 3-х и не больше 20',
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Логин:')
    password = forms.CharField(min_length=6,
                               max_length=35,
                               help_text='Длина пароля должна быть не меньше 6 и не больше 35',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Пароль:')
    class Meta:
        model = User
        fields = ['username', 'password']