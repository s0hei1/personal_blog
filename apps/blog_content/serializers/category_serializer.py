from rest_framework import serializers

from apps.blog_content.models import Category


class CategoryRetrievalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
