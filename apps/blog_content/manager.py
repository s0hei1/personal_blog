from django.db.models import QuerySet


class CommentQuerySet(QuerySet):
    def is_public(self):
        return self.filter(is_public=True)
