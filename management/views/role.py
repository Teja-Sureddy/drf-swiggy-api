from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models_list.role import Role
from ..serializers.role import RoleSerializer
from ..permissions.role import RolePermission

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, RolePermission]