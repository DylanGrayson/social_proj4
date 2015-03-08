from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django import forms
from django.forms import ModelForm
from main.models.corgi import Corgi


class AddCorgiForm(ModelForm):
	class Meta:
		model = Corgi
		# exclude owner because if I don't, they will get a dropdown menu to
		# from all of the current users. We want this automatically tied to the logged-in user
		exclude = ('owner',)

def add_corgi(request, num):
	if request.method == 'POST':
		form = AddCorgiForm(request.POST)
		if form.is_valid():
			messages.success(request, "Your new corgi has been added!")
			# put the form info in temp variable but don't save to db
			new_corgi = form.save(commit=False)
			# add the "owner" of the new corgi
			new_corgi.owner = request.user
			# now save it to db
			new_corgi.save()
			return HttpResponseRedirect('/user/addcorgi/' + str(num))
	elif request.method == 'GET':
		form = AddCorgiForm()
	else:
		return HttpResponseRedirect('/user/addcorgi/' + str(num))
	return render(request, 'add_corgi.html', {'form': form})