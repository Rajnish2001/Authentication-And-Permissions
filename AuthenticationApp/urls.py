from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('studentapi',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),
]
