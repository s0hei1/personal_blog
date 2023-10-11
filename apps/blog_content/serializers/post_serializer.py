from rest_framework import serializers
from apps.blog_content.models import Post


class PostRetrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'title', 'content', 'created_at', 'edited_at', 'slug')
