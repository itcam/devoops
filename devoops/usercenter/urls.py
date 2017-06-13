#!coding:utf-8
from django.conf.urls import url,include
from django.contrib import admin
#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views ,test_views
from rest_framework.authtoken import views as authtoken_views
from .views import UserList
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^$', views.login),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^hel/$', test_views.hello_world),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    #url(r'^userlist/', UserList.as_view()),
    url(r'^userlist/', views.user_group_list),
    url(r'^snippets/$', views.group_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
