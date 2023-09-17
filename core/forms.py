from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder_classes = 'w-full py-4 px-6 rounded-xl'

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
            'class': placeholder_classes
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
            'class': placeholder_classes
        })

class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder_classes = 'w-full py-4 px-6 rounded-xl'

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
            'class': placeholder_classes
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email',
            'class': placeholder_classes
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter your password',
            'class': placeholder_classes
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm your password',
            'class': placeholder_classes
        })
