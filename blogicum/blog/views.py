from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .constants import POSTS_PER_PAGE


def index(request):
    template = 'blog/index.html'
    posts = (
        Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )[:POSTS_PER_PAGE]
    )
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = (
        category.posts.filter(
            is_published=True,
            pub_date__lte=timezone.now()
        ))
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
