from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.user.is_authenticated and request.user.role.name in ['admin']:
            return True
        elif request.user.is_authenticated and request.user.role.name in ['manager','user'] and request.method in ['GET', 'OPTIONS']:
            return True
        return False    
        
    def has_object_permission(self, request, view, obj):
        if request.user.role.name in ['admin']:
            return True
        elif request.user.role.name in ['user'] and request.method in ['GET', 'OPTIONS']:
            return obj.user == request.user
        elif request.user.role.name in ['manager'] and request.method in ['GET', 'OPTIONS']:
            return True
        return False