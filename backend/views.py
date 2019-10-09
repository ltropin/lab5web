from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from backend.forms import *
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', context={'form': SignInForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        form = SignInForm(request.POST)
        if form.is_valid():
            user_active = authenticate(username=username, password=password)
            if user_active is None:
                login(request, user_active)
                return redirect('index')
            else:
                messages.error(request, 'Не верный логин или пароль')
                return render(request, 'signin.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', context={'form': SignUpForm()})
