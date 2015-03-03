from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import ModelForm


class EditUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


def edit(request, num):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/user/edit/' + str(num))
    elif request.method == 'GET':
        form = EditUserForm(instance=request.user)
    else:
        return HttpResponseRedirect('/user/edit/' + str(num))
    return render(request, 'edit_user.html', { 'form': form })
