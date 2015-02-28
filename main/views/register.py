from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/register/")
    elif request.method == 'GET':
        form = UserCreationForm()
    else:
        return HttpResponseRedirect('/register/')
    return render(request, "registration.html", {"form": form })
