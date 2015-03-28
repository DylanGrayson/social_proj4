from rest_framework import status
from rest_framework.decorators import api_view
#from rest_framework.response import Response
from django.http import JsonResponse
from main.models.post import Post
from main.models.friendship import Friendship
from django.contrib.auth.models import User
from main.serializers import PostSerializer, FriendshipSerializer

"""
This file holds the special views that will act as the api for this site
The views will return JSON and will be accessed from the regular django templates
using javascript remote calls. In essence the website will access itself.

Currently, the idea is to only have a sidebar that will update constantly showing
your friends' comments.
"""

#@api_view(['GET'])
def post_list(request, num):
	"""
	List all of the available comments (for now). Will later only show friends'
	"""
	if request.method == 'GET':
		friends = Friendship.objects.filter()
		posts = Post.objects.all()

		serializer = PostSerializer(posts, many=True)
		return JsonResponse(serializer.data, status=200, safe=False)

	else:
		return JsonResponse({}, status=404)