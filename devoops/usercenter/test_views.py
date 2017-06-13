#!/usr/bin/env /data/app/python/bin/python
#coding:utf-8
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view

class ListUsers(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
