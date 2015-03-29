from django.db import models
from django.contrib.auth.models import User


class Corgi(models.Model):
	name = models.CharField(max_length=80)
	owner = models.ForeignKey(User)
	image = models.ImageField(upload_to = 'profile_pictures/', default = 'profile_pictures/no_image.png')
