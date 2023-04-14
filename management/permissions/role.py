from rest_framework import permissions


class RolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name in ['admin'] or request.method in ['GET', 'OPTIONS']:
            return True
        return False

class AdminRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name in ['admin']:
            return True
        return False

class ManagerRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name in ['manager']:
            return True
        return False

class UserRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name in ['user']:
            return True
        return False