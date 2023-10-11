from django.contrib import admin
from apps.blog_content.models import Category, Post, Comment, BlogHomeContent
from core.exceptions import BlogHomeContentSaveException
from django.contrib import messages


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'title', 'category', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_count']
    prepopulated_fields = {"slug": ("title",)}

    def post_count(self, obj):
        return obj.posts.count()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_date_time', 'is_public']
    ordering = ('-comment_date_time',)


@admin.register(BlogHomeContent)
class BlogHomeContentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except BlogHomeContentSaveException as e:
            messages.error(request, f"Error: {str(e)}")
