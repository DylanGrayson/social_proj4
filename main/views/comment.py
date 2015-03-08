from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django import forms
from django.forms import ModelForm
from main.models.post import Post


class AddPostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ('owner',)

def add_comment(request, num):
	if request.method == 'POST':
		form = AddPostForm(request.POST)
		if form.is_valid():
			messages.success(request, "Your Comment has been added!")
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			return HttpResponseRedirect('/user/addpost/' + str(num))
	elif request.method == 'GET':
		form = AddPostForm()
	else:
		return HttpResponseRedirect('/user/addpost/' + str(num))
	return render(request, 'add_comment.html', {'form': form})