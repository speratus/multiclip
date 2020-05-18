from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=256)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=256)