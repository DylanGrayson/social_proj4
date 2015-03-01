
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated():
        return render(request, "home.html", {'all_users': User.objects.all()})
    return render(request, "splash.html", {})

def profile(request, num):
	if request.user.is_authenticated():
		return render(request, "profile.html", {'subject': User.objects.get(pk=num)})
	return render(request, "splash.html", {})