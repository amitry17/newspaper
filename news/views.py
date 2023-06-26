from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-timeDateCreation'
    template_name = 'post.html'
    context_object_name = 'posts_link'



class PostDetail(DetailView):
    model = Post
    order = 'title'
    template_name = 'post_detail.html'
    context_object_name = 'post_link'