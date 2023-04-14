from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models_list.order import Order
from ..models_list.ordered_items import OrderedItems
from ..serializers.order import OrderSerializer
from ..serializers.ordered_items import OrderedItemsSerializer
from ..permissions.orders import OrderPermission
from ..permissions.role import UserRolePermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter



class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-dateTime')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, OrderPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'restaurant__name': ['istartswith','icontains'],
        'user__username': ['istartswith','icontains'],
        'dateTime': ['lte','gte'],
        'restaurant': ['exact']
    }
    ordering_fields = ['id','restaurant__name', 'user__username', 'dateTime']


    @action(detail=False, name='userOrders', url_path='userOrders', permission_classes=[IsAuthenticated, UserRolePermission], methods=['get'])    
    def userOrders(self, request):
        user = self.request.user
        orders = Order.objects.filter(user=user).order_by('-dateTime')
        orders_with_items = []
        for order in orders:
            ordered_items = OrderedItems.objects.filter(order=order)
            serializer = OrderedItemsSerializer(ordered_items, many=True)
            order_dict = OrderSerializer(order).data
            order_dict['items'] = serializer.data
            orders_with_items.append(order_dict)
        return Response(orders_with_items)