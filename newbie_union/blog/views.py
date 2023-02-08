from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from newbie_union.settings import PAGINATOR_COUNT
from .forms import PostForm, CommentForm
from .models import Group, Post, User, Follow


def post_paginator(blog, request):
    paginator = Paginator(blog, PAGINATOR_COUNT)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    return render(request, 'blog/index.html', {
        'page_obj': post_paginator(Post.objects.all(), request)})


def group_blog(request, slug):
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group': group,
        'page_obj': post_paginator(group.blog.all(), request),
    }
    return render(request, 'blog/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    following = request.user.is_authenticated and request.user != author and (
        Follow.objects.filter(user=request.user, author=author).exists())
    context = {
        'author': author,
        'page_obj': post_paginator(author.post.all(), request),
        'following': following,
    }
    return render(request, 'blog/profile.html', context)


def post_detail(request, post_id):
    context = {
        'post': get_object_or_404(Post, id=post_id),
        'form': CommentForm(request.POST or None),
    }
    return render(
        request, 'blog/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post:profile', post.author)
    context = {
        'form': form
    }
    return render(request, 'blog/create_post.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('post:post_detail', post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post)
    if form.is_valid():
        post.save()
        return redirect('post:post_detail', post_id)
    context = {
        'form': form,
        'is_edit': True
    }
    return render(request, 'blog/create_post.html', context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('blog:post_detail', post_id=post_id)


@login_required
def follow_index(request):
    return render(request, 'blog/follow.html', {
        'page_obj': post_paginator(Post.objects.filter(
            author__following__user=request.user),
            request)
    })


@login_required
def profile_follow(request, username):
    if username != request.user.username:
        Follow.objects.get_or_create(
            user=request.user,
            author=get_object_or_404(User, username=username))
    return redirect('blog:profile', username)


@login_required
def profile_unfollow(request, username):
    get_object_or_404(
        Follow,
        user=request.user,
        author__username=username,).delete()
    return redirect('blog:profile', username)
