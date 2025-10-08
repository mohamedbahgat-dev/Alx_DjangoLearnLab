from .views import PostViewSet, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post' )
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls) ),
    path('feed/', FeedView.as_view(), name='feed')
]