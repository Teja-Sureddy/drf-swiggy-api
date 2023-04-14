from rest_framework import serializers
from ..models_list.role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields ='__all__'