from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models_list.ordered_items import OrderedItems
from ..serializers.ordered_items import OrderedItemsSerializer
from ..permissions.orders import OrderPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class OrderedItemsViewSet(ModelViewSet):
    queryset = OrderedItems.objects.all()
    serializer_class = OrderedItemsSerializer
    permission_classes = [IsAuthenticated, OrderPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'item__name': ['istartswith', 'icontains'],
        'item__price': ['range'],
        'quantity': ['range'],
        'item__type': ['exact'],
        'order': ['exact']
    }
    ordering_fields = ['item__name','item__price', 'quantity']