from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.all()
    context = {'posts': list(reversed(posts))}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
