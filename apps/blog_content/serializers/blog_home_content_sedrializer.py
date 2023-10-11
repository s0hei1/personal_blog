from rest_framework import serializers

from apps.blog_content.models import BlogHomeContent


class BlogHomeContentRetrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogHomeContent
        fields = '__all__'
