#!coding:utf-8
from django.conf.urls import url,include
from django.contrib import admin
#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views
from usercenter.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'user_group', GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
