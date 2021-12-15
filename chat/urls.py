from django.urls import path, include
from rest_framework import routers

from .views import ChatroomViewSet


router = routers.DefaultRouter()
router.register(r'', ChatroomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]