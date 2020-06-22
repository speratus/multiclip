from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def main(request):
    render(request, 'main.html')

def login(request):
    if request.method == 'POST':
        pass
    else:
        loginform = LoginForm()
        render(request, 'login.html', {'form': loginform})