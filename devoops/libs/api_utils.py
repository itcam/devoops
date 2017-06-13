# coding:utf8
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
import math
# from usercenter.models import User, UserDepartMentInfo

from django.contrib.auth.models import User 

import json
import re
from django.http import HttpResponse
from django.utils.html import conditional_escape
import logging
from rest_framework.response import Response
logger = logging.getLogger('pams')


def trans_illegal(s):
    """
    转换不合法的字符
    """
    g = lambda src: src if re.search(r'^http', src) else conditional_escape(src)
    if isinstance(s, (str, unicode)):
        return g(s)
    elif isinstance(s, (list, tuple)):
        s = list(s)
        for i in s:
            trans_illegal(i)
    elif isinstance(s, dict):
        for k, v in s.items():
            s[k] = trans_illegal(v)
    else:
        pass
    return s


def http_response_json(status=0, msg="", data=""):
    data = trans_illegal(data)
    return HttpResponse(content=json.dumps({'status': status, 'msg': msg, 'data': data}),
                        content_type="application/json")

def http_response_json_v2(status=0, msg="", data=""):
    #data = trans_illegal(data)
    #return HttpResponse(content=json.dumps({'status_code': status, 'msg': msg, 'data': data}),
    return Response({'status_code': status, 'msg': msg, 'data': data})

def http_response_json_data(data=""):
    data = trans_illegal(data)
    return HttpResponse(content=json.dumps(data),
                        content_type="application/json")

def http_response_html(status=0, msg="", data=""):
    data = trans_illegal(data)
    return HttpResponse(content=json.dumps({'status': status, 'msg': msg, 'data': data}),
                        content_type="text/html;charset=utf-8")


def render_response_html(request, html, data):
    user_id = request.session.get('_auth_user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            data['username'] = user.username
            data["is_superuser"] = user.is_superuser
            now_month = datetime.now().month
            data["is_active"] = user.is_active
            data["last_login"] = user.last_login
        except Exception as e:
            print e
            pass
    return render_to_response(html, data, RequestContext(request))
