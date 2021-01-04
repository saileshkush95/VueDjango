from rest_framework.permissions import (DjangoModelPermissions)
from rest_framework import permissions
from django.db import connection


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


# class TenantVerify(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if connection.schema_name == 'yarshatech':
#             return True
#         else:
#             return False
