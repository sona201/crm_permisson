from django.test import TestCase

# Create your tests here.

permission_dict = {
    'customer_list': {
        'id': 1,
        'title': '客户列表',
        'url': '/customer/list/',
        'pid': None,
        'p_title': None,
        'p_url': None},
    'customer_add': {
        'id': 2,
        'title': '添加客户',
        'url': '/customer/add/',
        'pid': 1,
        'p_title': '客户列表',
        'p_url': '/customer/list/'},
    'customer_del': {
        'id': 3,
        'title': '删除客户',
        'url': '/customer/list/(?P<cid>\\d+)/',
        'pid': 1,
        'p_title': '客户列表',
        'p_url': '/customer/list/'},
    'customer_edit': {
        'id': 4,
        'title': '修改客户',
        'url': '/customer/edit/(?P<cid>\\d+)/',
        'pid': 1,
        'p_title': '客户列表',
        'p_url': '/customer/list/'},
    'customer_import': {
        'id': 5,
        'title': '批量导入',
        'url': '/customer/import/',
        'pid': 1,
        'p_title': '客户列表',
        'p_url': '/customer/list/'},
    'customer_tpl': {
        'id': 6,
        'title': '下载模板',
        'url': '/customer/tpl/',
        'pid': 1,
        'p_title': '客户列表',
        'p_url': '/customer/list/'},
    'payment_list': {
        'id': 7,
        'title': '账单列表',
        'url': '/payment/list/',
        'pid': None,
        'p_title': None,
        'p_url': None},
    'payment_add': {
        'id': 8,
        'title': '添加账单',
        'url': '/payment/add/',
        'pid': 7,
        'p_title': '账单列表',
        'p_url': '/payment/list/'},
    'payment_del': {
        'id': 9,
        'title': '删除账单',
        'url': '/payment/del/(?P<pid>\\d+)/',
        'pid': 7,
        'p_title': '账单列表',
        'p_url': '/payment/list/'},
    'payment_edit': {
        'id': 10,
        'title': '修改账单',
        'url': '/payment/edit/(?P<pid>\\d+)/',
        'pid': 7,
        'p_title': '账单列表',
        'p_url': '/payment/list/'}
    }

# for item in permission_dict.values():
#     print(item)

print(permission_dict.values())
