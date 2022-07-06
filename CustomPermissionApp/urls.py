from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('customstudentapi',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('cust/',include('rest_framework.urls')),#Use This in-built rest_framework urls to use the login page automaticaly
]
