from django.shortcuts import render
from .models import Post


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', context={'posts': posts})


def post_detail(request, id,slug):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', context={'post': post})
