from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib import messages


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You have been registered')
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    elif request.method == 'GET':
        form = NewUserForm()
    else:
        return HttpResponseRedirect('/register/')
    return render(request, "registration.html", {"form": form})