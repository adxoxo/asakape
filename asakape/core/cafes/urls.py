from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CafeViewSet

router = DefaultRouter()
router.register(r'cafes', CafeViewSet, basename='cafe')

urlpatterns = [
    path('', include(router.urls))
]