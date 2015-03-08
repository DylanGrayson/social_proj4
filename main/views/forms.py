from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

class UserSearch(forms.Form):
	phrase = forms.CharField(label='', max_length=100)

