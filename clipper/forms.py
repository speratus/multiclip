from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=256)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=256)

class SignupForm(forms.Form):
    email = forms.CharField(label="Email", max_length=256)
    username = forms.CharField(label="Username", max_length=256)
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", max_length=256, widget=forms.PasswordInput)