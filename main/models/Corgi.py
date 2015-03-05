from django.db import models
from django.contrib.auth.models import User


class Corgi(models.Model):
	name = models.CharField(max_length=80)
	owner = models.ForeignKey(User)