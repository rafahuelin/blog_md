from django.conf import settings
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts")

    def __str__(self) -> str:
        return f'[<img class="image" style="width: 100%" src="{settings.MEDIA_URL}{self.image}">'

