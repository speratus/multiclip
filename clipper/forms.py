from django import forms
from django.core.validators import validate_email
from django.contrib.auth.forms import PasswordChangeForm as PasswordChange

from .validators import validate_unique_username

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=256,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        max_length=256,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Password'
            }
        )
    )

class SignupForm(forms.Form):
    email = forms.CharField(
        label="Email",
        max_length=256,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Email'
            }
        ),
        validators=[validate_email]
    )
    username = forms.CharField(
        label="Username",
        max_length=256,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Username'
            }
        ),
        validators=[validate_unique_username]
    )
    password = forms.CharField(
        label="Password",
        max_length=256,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Password'
            }
        )
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        max_length=256,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Confirm Password'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if confirm_password != password:
            msg = "Passwords must match!"
            self.add_error('confirm_password', msg)


class PasswordChangeForm(PasswordChange):
    old_password = forms.CharField(
        label="Old Password",
        max_length=256,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Old Password'
            }
        )
    )

    new_password1 = forms.CharField(
        label='New Password',
        max_length=256,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'New Password'
            }
        )
    )

    new_password2 = forms.CharField(
        label="Confirm Password",
        max_length=256,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'input',
                'placeholder': 'Confirm Password'
            }
        )
    )