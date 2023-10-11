from rest_framework import serializers

from apps.blog_content.models import Comment


class CommentRetrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('commenter_name', 'comment_date_time', 'comment')


class CommentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('commenter_name', 'comment_date_time', 'comment')
