from django.shortcuts import render


# Create your views here.
def posts_list(request):
    n = ['Oleg', 'Masha', 'Olya','Ksu']
    return render(request, 'blog/posts.html', context={'names': n})
