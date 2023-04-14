from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import User
from ..serializers.user import UserSerializer
from ..permissions.user import UserPermission
from ..permissions.role import AdminRolePermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'username': ['istartswith', 'icontains'],
        'email': ['istartswith', 'icontains'],
        'role__name': ['exact']
    }
    ordering_fields = ['username','email', 'role__name']


    @action(detail=False, name='managers', url_path='managers', permission_classes=[IsAuthenticated, AdminRolePermission])    
    def managers(self, request):    
        managers = User.objects.filter(role__name='manager')    
        serializer = self.get_serializer(managers, many=True)
        return Response(serializer.data)    
        
    @action(detail=False, name='users', url_path='users', permission_classes=[IsAuthenticated, AdminRolePermission])    
    def users(self, request):    
        user = User.objects.filter(role__name='user')    
        serializer = self.get_serializer(user, many=True)
        return Response(serializer.data)