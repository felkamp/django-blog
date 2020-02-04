from django.shortcuts import render, redirect
from .models import Post, Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin
from .forms import TagForm


# Create your views here.
class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(id=id)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


def posts_list(request):
    posts = Post.objects.all().order_by('id')
    return render(request, 'blog/posts.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags': tags})

# def post_detail(request, id, slug):
#     post = Post.objects.get(id=id)
#     return render(request, 'blog/post_detail.html', context={'post': post})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})
