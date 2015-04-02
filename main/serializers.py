from rest_framework import serializers
from main.models.post import Post
from main.models.friendship import Friendship
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'first_name', 'last_name')


class PostSerializer(serializers.ModelSerializer):
	owner = UserSerializer(read_only=True)
	recipient = UserSerializer(read_only=True)
	date = serializers.DateTimeField(format="%A, %b %d %Y at %I:%M%p")

	class Meta:
		model = Post
		fields = ('title', 'body', 'date', 'owner', 'recipient')


class FriendshipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Friendship
		fields = ('creator', 'friend', 'accepted')