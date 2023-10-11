from django.shortcuts import render
from rest_framework import viewsets
from apps.blog_content.models import Post
from apps.blog_content.serializers.post_serializer import PostRetrivalSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostRetrivalSerializer
