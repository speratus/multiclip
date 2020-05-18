from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        pass
    else:
        loginform = LoginForm()
        render(request, 'login.html', {'form': loginform})