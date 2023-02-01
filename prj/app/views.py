from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (CreateView)
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *


class CreatePost(PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_post'
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'create_post.html'
    success_url = 'posts'

    def create_post(self, request):
        if request.method == 'POST':
            form = PostForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                # print(form.cleaned_data)
                form.save()
                return redirect('home')
        return render(request, 'app/create_post.html')


def index(request):
    return render(request, 'index.html')


def posts(request):
    post = Post.objects.order_by('-id')
    return render(request, 'posts.html', {'title': 'Новостной портал - Статьи', 'post': post})


def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
        'post_title': post.post_title,
        'post_text': post.post_text,
        'post_photo': post.post_photo,
        'post_author': post.post_author,
        'post_date': post.post_date,
        'post_date_update': post.post_date_update,
    }

    return render(request, 'app/post.html', context=context)
