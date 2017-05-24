#!coding:utf-8
from django.conf.urls import url,include
from django.contrib import admin
#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views



urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
]
