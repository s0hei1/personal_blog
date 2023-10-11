from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from apps.blog_content.models import Comment
from apps.blog_content.serializers.comment_serailizer import CommentCreationSerializer, CommentRetrivalSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.is_public()

    http_method_names = ['post', 'get']

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CommentRetrivalSerializer
            case 'retrival':
                return CommentRetrivalSerializer
            case 'create':
                return CommentCreationSerializer
            case _:
                raise NotAcceptable()
