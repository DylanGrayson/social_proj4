from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length= 140)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    owner = models.ForeignKey(User, related_name="author_set")
    recipient = models.ForeignKey(User, related_name="recipient_set")



    def __unicode__(self):
        return self.title