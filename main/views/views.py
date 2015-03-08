from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models.corgi import Corgi
from main.models.post import Post

from .forms import *


def home(request):
    if request.user.is_authenticated():
    	form = UserSearch()
        return render(request, "home.html", {'all_users': User.objects.all(), 'form': form})
    return render(request, "splash.html", {})

def profile(request, num):
	if request.user.is_authenticated():
		sub = User.objects.get(pk=num)
		return render(request, "profile.html", {'subject': sub,
												'corgis': Corgi.objects.filter(owner = sub),'posts': Post.objects.filter(owner = sub)})
	return render(request, "splash.html", {})

def search_results(request):
	if request.method == 'POST':
		if request.user.is_authenticated():
			form = UserSearch(request.POST)
			if form.is_valid():
				query = form.cleaned_data['phrase']
				return render(request, "search.html", {
									'results': User.objects.filter(username__contains=query),
									'form': form})
	return HttpResponseRedirect('/')