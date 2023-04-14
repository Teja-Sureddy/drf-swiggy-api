from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum, F
from ..models_list.restaurant import Restaurant
from ..models_list.order import Order
from ..models_list.ordered_items import OrderedItems
from ..serializers.restaurant import RestaurantSerializer
from ..permissions.role import ManagerRolePermission, AdminRolePermission
from ..permissions.restaurant import RestaurantPermission
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db import connection


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, RestaurantPermission]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'name': ['istartswith', 'icontains'],
        'user__username': ['istartswith', 'icontains']
    }
    ordering_fields = ['name','user__username']

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            if 'UNIQUE constraint failed' in str(e):
                return Response({'error': 'Manager\'s restaurant already exist.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
    @action(detail=False, name='restaurantByManager', url_path='restaurantByManager', permission_classes=[IsAuthenticated, ManagerRolePermission])    
    def restaurantByManager(self, request):    
        user = self.request.user
        try:
            restaurant = user.restaurant
            serializer = self.get_serializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({"Error":"No restaurant found."}, status=status.HTTP_400_BAD_REQUEST)

            
    @action(detail=False, name='User Spendings', url_path='userSpendings', permission_classes=[IsAuthenticated, AdminRolePermission])
    def user_spendings(self, request):
        # reports = []
        # for restaurant in Restaurant.objects.all():
        #     orders = Order.objects.filter(restaurant=restaurant)
        #     user_spending = OrderedItems.objects.filter(order__in=orders).values('order__user__username').annotate(total_spending=Sum(F('item__price') * F('quantity'))).order_by('-total_spending')
        #     report = {
        #         'restaurant': restaurant.name,
        #         'user_spending': user_spending
        #     }

        #     reports.append(report)
        # return Response(reports)


        cursor = connection.cursor()
        cursor.execute('''
            SELECT MIN(order_total) as minimum, MAX(order_total) as maximum, AVG(order_total) average, SUM(order_total) as total, username from (
            SELECT SUM(OI.quantity * M.price) as order_total, U.username as username  FROM management_ordereditems AS OI
            JOIN management_menu AS M on M.id = OI.item_id
            JOIN management_order AS O on O.id = OI.order_id
            JOIN management_user AS U on O.user_id = U.id
            GROUP BY OI.`order_id`) GROUP BY username
        ''')        
        # cursor.execute('''
        #     PRAGMA table_info(management_ordereditems);
        # ''')

        rows = cursor.fetchall()
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in rows]
        return Response(result)