from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, register_user

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
]
