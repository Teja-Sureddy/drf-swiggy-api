from rest_framework import serializers
from ..models_list.role import Role
from ..models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    roleName = serializers.CharField(source='role.name', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'role', 'roleName']

    def create(self, validated_data):
        role = Role.objects.get(name=validated_data.pop('role'))
        password = validated_data.pop('password')
        user = User.objects.create(role=role, password = make_password(password),is_active=True, **validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password:
            instance.password = make_password(password)
        instance.save()
        return instance