
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated():
        return render(request, "profile.html", {})
    return render(request, "home.html", {})