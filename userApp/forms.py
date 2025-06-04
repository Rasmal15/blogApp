from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "phone",
            "password1",
            "password2",
        ]
    first_name = forms.CharField(max_length=50, label='First Name', widget=(forms.TextInput(attrs = { 'class' : 'form-control'})))
    last_name = forms.CharField(max_length=50, label='Last Name', widget=(forms.TextInput(attrs = { 'class' : 'form-control'})))
    email = forms.CharField(max_length=50, label='Email', widget=(forms.EmailInput (attrs = {'class' : 'form-control'})))
    username = forms.CharField(max_length=50, label='Username', widget=(forms.TextInput (attrs = {'class' : 'form-control'})))
    phone = forms.CharField(max_length=15, label='Mobile Number', widget=(forms.NumberInput (attrs = {'class' : 'form-control'})))
    password1 = forms.CharField(max_length=50, label='Password', widget=(forms.PasswordInput (attrs = {'class' : 'form-control'})))
    password2 = forms.CharField(max_length=50, label='Confirm Password', widget=(forms.PasswordInput (attrs = {'class' : 'form-control'})))
