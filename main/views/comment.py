from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from main.models.post import Post
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class AddPostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ('owner', 'date', 'recipient')

def add_comment(request, num):
	if request.method == 'POST':
		form = AddPostForm(request.POST)
		if form.is_valid():
			messages.success(request, "Your Comment has been added!")
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.recipient = User.objects.get(pk=num)
			new_post.save()
			return HttpResponseRedirect('/user/addpost/' + str(num))
	elif request.method == 'GET':
		form = AddPostForm()

	else:
		return HttpResponseRedirect('/user/addpost/' + str(num))
	return render(request, 'add_comment.html', {'form': form})\

class LinkForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("owner",)

class LinkUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy("home")

class LinkDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("home")