from django.contrib import admin
from .models import Post, PostImage



class PostImageInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'created', 'updated')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    readonly_fields = ('created', 'updated')
    list_per_page = 25

    inlines = [
        PostImageInline,
    ]

admin.site.register(Post, PostAdmin)
