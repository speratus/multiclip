from django import forms

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
    email = forms.CharField(label="Email", max_length=256)
    username = forms.CharField(label="Username", max_length=256)
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", max_length=256, widget=forms.PasswordInput)