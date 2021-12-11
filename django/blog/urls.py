from django.urls import path
from blog.api import PostAPIView
from blog.views import PostsListView


urlpatterns = [
    path('api/V1/posts/', PostAPIView.as_view()),
    path('', PostsListView.as_view(), name='posts_list'),
]