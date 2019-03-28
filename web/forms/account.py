from django.shortcuts import HttpResponse, render, redirect

from rbac import models


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    # 根据当前用户信息获取次用户所拥有的所有的权限， 并放入session

    # 当前用户所有权限
    permission_queryset = current_user.roles.filiter(permission__is_null=False).values("permission__id",
                                                                                       "permisssions__url").distinct()

    # 获取权限中所有的URL
    permission_list = []
    for item in permission_queryset:
        permission_list.append(item['permission__url'])

    permission_list  = [item['permission__url'] for item in permission_queryset]

    return redirect('/customer/list/')
