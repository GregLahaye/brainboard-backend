from django.urls import path, include
from rest_framework.routers import DefaultRouter

from boards import views

router = DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
