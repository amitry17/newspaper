from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth.decorators import login_required
from news.models import Author


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = ''

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('posts')

@login_required
def not_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if request.user.groups.filter(name='authors').exists():
        authors_group.user_set.remove(user)
    return redirect('posts')