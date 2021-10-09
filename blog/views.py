from django.shortcuts import render
from blog.models import Post

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})
