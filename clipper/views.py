from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import LoginForm


def main(request):
    render(request, 'main.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                redirect(reverse('main'))
    else:
        loginform = LoginForm()
        render(request, 'login.html', {'form': loginform})