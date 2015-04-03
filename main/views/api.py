from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from main.models.post import Post
from main.models.friendship import Friendship
from django.contrib.auth.models import User
from main.models import Corgi
from main.serializers import PostSerializer, FriendshipSerializer
from django.contrib.sessions.models import Session

"""
This file holds the special views that will act as the api for this site
The views will return JSON and will be accessed from the regular django templates
using javascript remote calls. In essence the website will access itself.

Currently, the idea is to only have a sidebar that will update constantly showing
your friends' comments.
"""

def _get_friend_list(num):
	"""
	Use the current logged in user to search for their friends in the Friendship model.
	Then get the "friend" attribute, which is a User object, from each friendship.
	Put these friends into a list.
	Return the list of User objects that are the current user's friends
	"""
	current_user = User.objects.get(pk=num)
	friendships = Friendship.objects.filter(creator=current_user, accepted=True)
	friends = [current_user] # include the current user -- we want their posts to show up too
	for friendship in friendships:
		friends.append(friendship.friend)
	friendships = Friendship.objects.filter(friend=current_user, accepted=True)
	for friendship in friendships:
		friends.append(friendship.friend)
	return friends


def _get_friend_posts(num):
	"""
	Uses above method to get all friends then gets all the posts that any of these users
	have made
	"""
	friends = _get_friend_list(num)
	posts = Post.objects.filter(owner__in=friends).order_by('-date')
	return posts



def post_list(request, num):
	"""
	List all of the available comments (for now). Will later only show friends'
	"""
	if request.method == 'GET':
		posts = _get_friend_posts(num)[:5]
		serializer = PostSerializer(posts, many=True)
		return JsonResponse(serializer.data, status=200, safe=False)

	else:
		return JsonResponse({}, status=404)


def site_stats(request):
	"""
	Give total numbers on various statistics on the site
	"""
	if request.method == 'GET':
		data = {
			'total_users': User.objects.all().count(),
			'total_friendships': Friendship.objects.all().count(),
			'pending_friendships': Friendship.objects.filter(accepted=False).count(),
			'total_corgis': Corgi.objects.all().count()
		}

		return JsonResponse(data)
	else:
		return JsonResponse({}, status=404)
		
