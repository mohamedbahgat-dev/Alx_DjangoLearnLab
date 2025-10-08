from django.urls import path, include
from .views import LoginAPIView, RegisterAPIView, ProfileView, UserViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('accounts/register/', RegisterAPIView.as_view(), name='register'),
    path('accounts/login/', LoginAPIView.as_view(), name='login'),
    path('accounts/profile/' ,ProfileView.as_view() ,name='profile'),
    path('', include(router.urls)),
    path('unfollow/<int:user_id>/', UserViewSet.unfollow, name='unfollow'),
    path('follow/<int:user_id>/', UserViewSet.follow, name='follow')
]


