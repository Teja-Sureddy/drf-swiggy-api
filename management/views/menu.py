from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers.menu import MenuSerializer
from ..permissions.menu import MenuPermission
from ..models_list.menu import Menu
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, MenuPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'name': ['istartswith', 'icontains'],
        'price': ['range'],
        'type': ['exact'],
        'restaurant': ['exact']
    }
    ordering_fields = ['name','price']