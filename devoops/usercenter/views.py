#!coding:utf-8
from django.http import HttpResponse 
from django.shortcuts import render
#from usercenter.models import UserSerializer
from usercenter.models import *
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from rest_framework import versioning
from django.contrib.auth.models import User
from libs.const import *
from libs.api_utils import render_response_html,http_response_json_v2
from rest_framework.test import APIRequestFactory

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = user_group.objects.all()
    serializer_class = GroupSerializer


#coding:utf-8
from django.shortcuts import render,render_to_response

import uuid
import urllib

from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseNotFound,HttpResponse,HttpResponseRedirect
# from jperm.models import Apply
# import paramiko
from usercenter.models import *
#from devoops.api import *
# from jumpserver.models import Setting
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from devlog.models import Log, FileLog
# from jperm.perm_api import get_group_user_perm, gen_resource
# from jasset.models import Asset, IDC
# from jperm.ansible_api import MyRunner
#import zipfile
#from libs.const import *
from libs.api_utils import http_response_html,http_response_json


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import user_group,GroupSerializer


def login(request):
    """登录界面"""
    msg = ''
    status= FAIL_STATUS
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/index/')
    if request.method == 'GET':
        data = dict()
        return render_response_html(request, 'login.html', data)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username,password
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    status= SUCCESS_STATUS
                    # return HttpResponse(user)
                # response.set_cookie('username', username, expires=604800)
                # response.set_cookie('seed', PyCrypt.md5_crypt(password), expires=604800)
                # return response
                else:
                    status= FAIL_STATUS
                    msg = '用户未激活'
            else:
                status= FAIL_STATUS
                msg = '用户名或密码错误1'
        else:
            status= FAIL_STATUS
            msg = '用户名或密码错误1'
    return http_response_json(status=status, msg=msg)



def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/user/login/')

@login_required
def index(request):
    data = dict()
    return render_response_html(request,'sidebar.html',data)


@api_view(['GET', 'POST'])
def user_group_list(request):
    if request.method == 'GET':
        queryset = user_group.objects.all()
        serializer = GroupSerializer
        versioning_class = versioning.QueryParameterVersioning
        return Response(serializer.data,status=status.HTTP_302_FOUND)
        #return HttpResponse(serializer.data,status=status.HTTP_302_FOUND)
        #return HttpResponse("haha")
    elif request.method == 'POST':
        print "POST................."
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def reset(request):
#     email = request.POST.get('email')
    

    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    versioning_class = versioning.QueryParameterVersioning  # 版本
    print "--------------",serializer_class.data,status.HTTP_302_FOUND
    #return Response(serializer_class.data, status=status.HTTP_400_BAD_REQUEST)

    #def post(self, request, *args, **kwargs):
    #    return self.create(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def group_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        usergroup = user_group.objects.all()
        serializer = GroupSerializer(usergroup, many=True)
        return http_response_json_v2(status.HTTP_200_OK,SUCCESS_MSG,serializer.data)

    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return http_response_json_v2(status.HTTP_201_CREATED,SUCCESS_MSG,serializer.data)
        return http_response_json_v2(status.HTTP_400_BAD_REQUEST,FAIL_MSG,serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = user_group.objects.get(pk=pk)
    except user_group.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
        return http_response_json_v2(status.HTTP_404_NOT_FOUND,FAIL_MSG)

    if request.method == 'GET':
        serializer = GroupSerializer(snippet)
        return http_response_json_v2(status.HTTP_200_OK,SUCCESS_MSG,serializer.data)

    elif request.method == 'PUT':
        serializer = GroupSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data)
            return http_response_json_v2(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return http_response_json_v2(status.HTTP_400_BAD_REQUEST,FAIL_MSG,serializer.errors)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
