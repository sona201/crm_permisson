#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from rbac.views import role, user

app_name = 'rbac'

urlpatterns = [
    re_path(r'^role/list/$', role.role_list, name='role_list'),  # rbac:role_list
    re_path(r'^role/add/$', role.role_add, name='role_add'),  # rbac:role_add
    re_path(r'^role/edit/(?P<pk>\d+)/$', role.role_edit, name='role_edit'),  # rbac:role_edit
    re_path(r'^role/del/(?P<pk>\d+)/$', role.role_del, name='role_del'),  # rbac:role_del

    re_path(r'^user/list/$', user.user_list, name='user_list'),  # user:user_list
    re_path(r'^user/add/$', user.user_add, name='user_add'),  # user:user_add
    re_path(r'^user/edit/(?P<pk>\d+)/$', user.user_edit, name='user_edit'),  # user:user_edit
    re_path(r'^user/del/(?P<pk>\d+)/$', user.user_del, name='user_del'),  # user:user_del
]