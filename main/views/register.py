from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import socket
socket.getaddrinfo('localhost', 8000)


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():


            new_user = form.save()
            email = new_user.email
            username = new_user.username

            messages.success(request, 'You have been registered')
            send_mail('Welcome to CorgiBook', 'Hello %s and welcome to CorgiBook! ' %(username) , settings.EMAIL_HOST_USER, [email], fail_silently=False)
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    elif request.method == 'GET':
        form = NewUserForm()
    else:
        return HttpResponseRedirect('/register/')
    return render(request, "registration.html", {"form": form})