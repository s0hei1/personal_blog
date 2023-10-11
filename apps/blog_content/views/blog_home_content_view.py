from django.shortcuts import render
from rest_framework import viewsets
from apps.blog_content.models import BlogHomeContent
from apps.blog_content.serializers.blog_home_content_sedrializer import BlogHomeContentRetrivalSerializer


class BlogHomeContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogHomeContent.objects.first()
    serializer_class = BlogHomeContentRetrivalSerializer
