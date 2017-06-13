#/usr/bin/env /data/app/python/bin/python
#!coding:utf-8
from __future__ import unicode_literals

from django.db import models
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class user_group(models.Model):
    GROUP_ID = models.AutoField(primary_key=True,verbose_name=u'组ID')
    GROUP_NAME = models.CharField(max_length=64, verbose_name=u"用户组名")
    class Meta:
        db_table = "user_group"
        verbose_name = u"用户组"
        verbose_name_plural = u"用户组"
    def __unicode__(self):
        return '%s,%s' % (self.GROUP_ID,self.GROUP_NAME)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_group
        fields = ('GROUP_ID', 'GROUP_NAME')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
