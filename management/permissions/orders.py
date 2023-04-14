from rest_framework import permissions


class OrderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name in ['admin']:
            return True
        elif request.user.role.name in ['manager'] and request.method in ['GET', 'OPTIONS']:
            return True
        elif request.user.role.name in ['user'] and request.method in ['GET', 'OPTIONS', 'POST']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role.name in ['admin']:
            return True
        elif request.user.role.name in ['manager'] and request.method in ['GET', 'OPTIONS']:
            return True
        elif request.user.role.name in ['user'] and request.method in ['GET', 'OPTIONS']:
            return obj.user == request.user
        elif request.user.role.name in ['user'] and request.method in ['POST']:
            return True
        return False