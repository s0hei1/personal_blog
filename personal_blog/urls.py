from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from apps.blog_content.views.blog_home_content_view import BlogHomeContentViewSet
from apps.blog_content.views.category_view import CategoryViewSet
from apps.blog_content.views.comment_view import CommentViewSet
from apps.blog_content.views.post_view import PostViewSet

router = routers.SimpleRouter()

router.register(r'api/blog-home-content', BlogHomeContentViewSet, basename='BlogHomeContent')
router.register(r'api/categories', CategoryViewSet)
router.register(r'api/comments', CommentViewSet)
router.register(r'api/posts', PostViewSet)

doc_patterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
urlpatterns += doc_patterns
