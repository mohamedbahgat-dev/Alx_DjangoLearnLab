from django.urls import path
from .views import LoginAPIView, RegisterAPIView, ProfileView

urlpatterns = [
    path('accounts/register/', RegisterAPIView.as_view(), name='register'),
    path('accounts/login/', LoginAPIView.as_view(), name='login'),
    path('accounts/profile/' ,ProfileView.as_view() ,name='profile')
]