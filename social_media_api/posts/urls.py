from .views import PostViewSet, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post' )
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls) )
]