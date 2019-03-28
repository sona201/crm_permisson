#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import re


class CheckPermission(MiddlewareMixin):
    """
    用户权限信息校验
    """

    def process_request(self, request):
        """
        当用户请求刚进入时触发执行
        :param request:
        :return:
        """

        """
        1. 获取当前用户请求的URL
        2. 获取当前用户在session中保存的权限列表 ['/customer/list/', '/customer/list/(?P<cid>\\d+)/']
        3. 权限信息匹配
        """
        # http://127.0.0.1:8000/customer/list/         ->   /customer/list/
        # http://127.0.0.1:8000/customer/list?age=0    ->   /customer/list/
        valid_url_list = [
            '/login/',
            '/admin/.*',
        ]

        current_url = request.path_info
        for vaild_url in valid_url_list:
            if re.match(vaild_url, current_url):
                # 白名单中的URL无需权限验证即可访问
                return None  # return None 等于中间件不拦截

        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_list:
            return HttpResponse('未获取到用户权限信息，请登录！')

        # print('current_url:', current_url)
        # print('permission_list:', permission_list)

        flag = False

        for url in permission_list:
            reg = "^%s$" % url
            if re.match(reg, current_url):
                flag = True
                break

        if not flag:
            return HttpResponse('无权访问')



