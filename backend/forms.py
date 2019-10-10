from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django import forms
from django.contrib.auth import login, authenticate
from backend.models import *
from django.forms.widgets import ClearableFileInput

class EmptyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = ''
    clear_checkbox_label = ''


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
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Логин:')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Пароль:')
    class Meta:
        model = User
        fields = ['username', 'password']


class RouteForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Код:')
    start = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}, format='%H:%M'),
                            label='Начало работы:')
    end = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}, format='%H:%M'),
                          label='Окончание работы:')
    type_route = forms.ChoiceField(widget=forms.Select(attrs={'class': 'mdb-select md-form'}),
                                   choices=Route.TYPE_CHOICE,
                                   label='Тип маршрута/транспорта:')
    map_city = forms.ImageField(label='Карта')

    class Meta:
        model = Route
        fields = '__all__'


class DriverForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Имя:')
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(),
                                     widget=forms.Select(attrs={'class': 'mdb-select md-form'}),
                                     required=True,
                                     empty_label='Выберите транспорт')
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker'}, format='%d.%m.%Y'),
                                 input_formats=['%d.%m.%Y'],
                                 label='Дата рождения:')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             label='Email:')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                            label='Телефон:')
    
    avatar = forms.ImageField(label='Аватар')

    class Meta:
        model = Driver
        fields = '__all__'

class StationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Имя:')
    position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Позиция:')
    route = forms.ModelChoiceField(queryset=Route.objects.filter(id__gt=1).all(),
                                   widget=forms.Select(attrs={'class': 'mdb-select md-form'}),
                                   required=True,
                                   empty_label='Выберите маршрут')
    class Meta:
        model = Station
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Имя:')
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  label='Вместимость:')
    type_vehicle = forms.ChoiceField(widget=forms.Select(attrs={'class': 'mdb-select md-form'}),
                                     choices=Route.TYPE_CHOICE,
                                     label='Тип транспорта:')
    route = forms.ModelChoiceField(queryset=Route.objects.filter(id__gt=1).all(),
                                   widget=forms.Select(attrs={'class': 'mdb-select md-form'}),
                                   required=True,
                                   empty_label='Выберите маршрут')

    class Meta:
        model = Vehicle
        fields = '__all__'

class XMLForm(forms.Form):
    route = forms.ModelChoiceField(queryset=Route.objects.filter(id__gt=1).all(),
                                   widget=forms.Select(attrs={'class': 'mdb-select md-form'}),
                                   required=True,
                                   empty_label='Выберите маршрут')
    xml = forms.FileField(label='XML', widget=forms.FileInput(attrs={'accept': 'text/xml'}))