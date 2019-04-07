from django.test import TestCase

# Create your tests here.
permission_queryset = [
    {
        "permissions__url": "aaa",
    },
    {
        "permissions__url": "bbb",
    },
    {
        "permissions__url": "ccc",
    },
    {
        "permissions__url": "ddd",
    },
]

permission_list = [item['permissions__url'] for item in permission_queryset]

print(permission_list)
