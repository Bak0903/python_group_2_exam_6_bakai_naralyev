from django.shortcuts import reverse,redirect, get_object_or_404, render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from webapp.models import Userinfo, Post
# from webapp.form import
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'