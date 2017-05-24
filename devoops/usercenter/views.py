#!coding:utf-8
from django.shortcuts import render
#from usercenter.models import UserSerializer
from usercenter.models import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

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
#from libs.api_utils import http_response_html,http_response_json


def login(request):
    """登录界面"""
    msg = ''
    status= FAIL_STATUS
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/index/')
    if request.method == 'GET':
        return render_to_response('page_user_login_2.html',msg, RequestContext(request))

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
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
                msg = '用户名或密码错误'
        else:
            status= FAIL_STATUS
            msg = '用户名或密码错误'
    return http_response_json(status=status, msg=msg)



def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/user/login/')

# def reset(request):
#     email = request.POST.get('email')
    

    


