from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin




class PostList(ListView):
    model = Post
    ordering = '-timeDateCreation'
    template_name = 'post.html'
    context_object_name = 'posts_link'
    paginate_by = 10

class PostSearch(ListView):
    model = Post 
    template_name = 'news/search.html'
    context_object_name = 'posts_search'
    ordering = ['-timeDateCreation']


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class PostDetail(DetailView):
    model = Post
    order = 'title'
    template_name = 'post_detail.html'
    context_object_name = 'post_link'


class NewsPostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_create.html'
    raise_exception = True

    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.postType = 'NW'
        return super().form_valid(form)

class NewsPostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_edit.html'
    raise_exception = True



class NewsPostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_post_delete.html'
    success_url = reverse_lazy('posts')
    raise_exception = True

class ArticlePostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_post_create.html'
    raise_exception = True
    
    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.postType = 'AR'
        return super().form_valid(form)

class ArticlePostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_post_edit.html'
    raise_exception = True

class ArticlePostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'article_post_delete.html'
    success_url = reverse_lazy('posts')
    raise_exception = True