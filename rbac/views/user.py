#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户管理
"""
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from rbac import models
from rbac.forms.user import UserModelForm


def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    user_queryset = models.UserInfo.objects.all()

    return render(request, 'rbac/user_list.html', {'users': user_queryset})


def user_add(request):
    """
    角色列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = RoleModelForm()
        return render(request, 'rbac/change.html', {'form': form})

    form = RoleModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/change.html', {'form': form})


def user_edit(request, pk):
    """
    编辑角色
    :param request:
    :param pk: 要修改的角色ID
    :return:
    """
    obj = models.Role.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('角色不存在')
    if request.method == 'GET':
        form = RoleModelForm(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})

    form = RoleModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/change.html', {'form': form})


def user_del(request, pk):
    """
    删除角色
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:role_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': origin_url})

    models.Role.objects.filter(id=pk).delete()
    return redirect(origin_url)
