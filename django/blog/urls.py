from django.urls import path
from blog.api import PostListAPI, PostDetailAPI
from blog.views import PostListView


urlpatterns = [
    path('api/V1/posts/', PostListAPI.as_view()),
    path('api/V1/posts/<int:pk>/', PostDetailAPI.as_view()),
    path('posts/', PostListView.as_view(), name='posts_list'),
]