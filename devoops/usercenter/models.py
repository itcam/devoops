#/usr/bin/env /data/app/python/bin/python
#!coding:utf-8
from __future__ import unicode_literals

from django.db import models
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


# Create your models here.
class user_group(models.Model):
    GROUP_ID = models.AutoField(primary_key=True)
    GROUP_NAME= models.CharField(max_length=64, verbose_name=u'组名')
    class Meta:
        db_table = "user_group"
        verbose_name = u'组列表'
    def __unicode__(self):
        return self.GROUP_ID

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_group
        fields = ('GROUP_ID', 'GROUP_NAME')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

