from django.shortcuts import render
from rest_framework import viewsets
from apps.blog_content.models import Category
from apps.blog_content.serializers.category_serializer import CategoryRetrievalSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrievalSerializer
