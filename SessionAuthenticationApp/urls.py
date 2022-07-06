from posixpath import basename
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('studentsessionapi',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),#Use This in-built rest_framework urls to use the login page automaticaly
]
