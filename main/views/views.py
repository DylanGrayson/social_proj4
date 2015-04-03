from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models.corgi import Corgi
from main.models.post import Post
from main.models.friendship import Friendship

from main.views.forms import *


def home(request):
    if request.user.is_authenticated():
    	me = request.user
    	friends = Friendship.objects.filter(creator=me)
        return render(request, "home.html", {'all_users': User.objects.all(),
        									 'friends': friends})
    return render(request, "splash.html", {})

def profile(request, num):
	if request.user.is_authenticated():
		sub = User.objects.get(pk=num)
		friend_requests = Friendship.objects.filter(friend = request.user, accepted = False)
		pending = Friendship.objects.filter(friend = sub, creator=request.user, accepted = False).exists()
		not_friends = not (Friendship.objects.filter(friend = sub, creator=request.user, accepted = True).exists())\
			and not (Friendship.objects.filter(creator = sub, friend=request.user, accepted = True).exists())

		friend_list = Friendship.objects.filter(friend = sub, accepted = True)
		friends = []
		for i in range(len(friend_list)):
			friends.append({'friend': friend_list[i].creator, 'since': friend_list[i].created})
		friend_list = Friendship.objects.filter(creator = sub, accepted = True)
		for i in range(len(friend_list)):
			friends.append({'friend': friend_list[i].friend, 'since': friend_list[i].created})

		return render(request, "profile.html", {'subject': sub,
											'corgis': Corgi.objects.filter(owner = sub),
											'posts': Post.objects.filter(recipient = sub),
											'requests': friend_requests,
											'pending': pending,
											'not_friends': not_friends,
											'friends': friends})
	return render(request, "splash.html", {})

def friendrequest(request, num):
	if request.user.is_authenticated():
		if request.method == 'POST':
			sub = User.objects.get(pk=num)
			friendship = Friendship(creator=request.user, friend=sub, accepted=False)
			if not (Friendship.objects.filter(creator=request.user, friend=sub).exists())\
				and not (Friendship.objects.filter(friend=request.user, creator=sub).exists()):
				friendship.save()
		sub = User.objects.get(pk=num)
		friend_requests = Friendship.objects.filter(friend = request.user, accepted = False)
		pending = Friendship.objects.filter(friend = sub, creator=request.user, accepted = False).exists()

		return render(request, "profile.html", {'subject': sub,
											'corgis': Corgi.objects.filter(owner = sub),
											'posts': Post.objects.filter(recipient = sub),
											'pending': pending})
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

def accept(request, num):
	if request.user.is_authenticated():
		req = Friendship.objects.get(id=num)
		req.accepted = True
		req.save()
		return HttpResponseRedirect('/user/' + str(request.user.id))
	return HttpResponseRedirect('/')

def deny(request, num):
	if request.user.is_authenticated():
		Friendship.objects.get(id=num).delete()
		return HttpResponseRedirect('/user/' + str(request.user.id))


def notifications(request):
	if request.user.is_authenticated():
		form = UserSearch()
		return {'requests': Friendship.objects.filter(friend = request.user, accepted = False),
				'search': form}
	return {}