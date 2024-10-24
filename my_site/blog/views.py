from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post
from django.views.generic import ListView


# Create your views here.

class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

def posts(requet):
    all_posts = Post.objects.all().order_by('-date')
    return render(requet, 'blog/all-posts.html', {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()
        })