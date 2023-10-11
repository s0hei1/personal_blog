from django.db import models

from apps.blog_content.manager import CommentQuerySet
from core.exceptions import BlogHomeContentSaveException


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    class RelatedNames:
        posts = 'posts'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name=Category.RelatedNames.posts)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    edited_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    image = models.ForeignKey('media.Image', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    commenter_name = models.CharField(max_length=255, null=True, blank=True)
    comment_date_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)

    objects = CommentQuerySet.as_manager()

    def __str__(self):
        return f"{self.commenter_name}'s Comment at {self.comment_date_time}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class BlogHomeContent(models.Model):
    blog_name = models.CharField(max_length=255, null=True, blank=True)
    welcome_message = models.CharField(max_length=255, null=True, blank=True)
    admin_name = models.CharField(max_length=255, null=True, blank=True)
    about_admin = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):

        if BlogHomeContent.objects.count() < 1:
            super().save(*args, **kwargs)
        else:
            raise BlogHomeContentSaveException("you can't add BlogHomeContent More than one model")

    def __str__(self):
        return "Blog Home Page Config"

    class Meta:
        verbose_name = 'Blog Home Content'
        verbose_name_plural = 'Blog Home Content'
