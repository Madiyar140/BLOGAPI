from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.main.views import ArticleViewSet, CommentViewSet, LikeViewSet, RatingViewSet, TagViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
