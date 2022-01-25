from django.db import models
from django import forms
from django.contrib.auth.models import User

#회원가입
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#로그인폼
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']