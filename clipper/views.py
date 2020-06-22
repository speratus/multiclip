from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as log_user_in
from django.http.response import HttpResponseRedirect
import uuid

from .forms import LoginForm


def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return redirect(reverse('login'))


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                log_user_in(request, user)
                id = uuid.uuid4()
                response = HttpResponseRedirect(reverse('main'))
                response.set_cookie('room-id', id.hex)
                return response
    else:
        loginform = LoginForm()
        return render(request, 'login.html', {'form': loginform})