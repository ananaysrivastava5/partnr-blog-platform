from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import BlogViewSet

router = DefaultRouter()

router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('api/', include(router.urls)),
]