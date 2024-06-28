from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User1
from django import forms
from django.contrib.auth.models import User
from .models import Customer, Owner


class UserForm(ModelForm):
    class Meta:
        model = User1
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class SignupForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control"
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         "class": "form-control"
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         "class": "form-control"
#     }))
#     email = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control"
#     }))

#     class Meta:
#         model = Status
#         fields = ['username', 'email', 'password1',
#                   'password2', 'is_admin', 'is_customer']
