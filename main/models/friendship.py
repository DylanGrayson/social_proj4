from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	creator = models.ForeignKey(User, related_name="friender_set")
	friend = models.ForeignKey(User, related_name="friend_set")
	accepted = models.BooleanField(default=False)