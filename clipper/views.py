from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as log_user_in
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
import uuid

from .forms import LoginForm, SignupForm
from .models import UserClipboard

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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            if data['confirm_password'] == data['password']:
                user = User.objects.create_user(data['username'], data['email'], data['password'])
                clipbpoard_id = uuid.uuid4().hex
                clipboard = UserClipboard(user=user, clipbpoard_id=clipbpoard_id)
                clipboard.save()
                return redirect(reverse('login'))
            else:
                pass
    else:
        signupform = SignupForm()
        return render(request, 'signup.html', {'form': signupform})