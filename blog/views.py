from django.views.generic import ListView
from blog.models import Post

class PostsListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
