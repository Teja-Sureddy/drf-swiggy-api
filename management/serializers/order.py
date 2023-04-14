from rest_framework import serializers
from ..models_list.order import Order
from ..models_list.ordered_items import OrderedItems
from ..models import User
from ..serializers.ordered_items import OrderedItemsSerializer
from django.db.models import Sum, F


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role__name='user'))
    userName = serializers.CharField(source='user.username', read_only=True)
    restaurantName = serializers.CharField(source='restaurant.name', read_only=True)
    ordered_items = OrderedItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        ordered_items = OrderedItems.objects.filter(order=instance)
        total_price = 0
        for ordered_item in ordered_items:
            total_price += ordered_item.item.price * ordered_item.quantity
        representation['total_price'] = total_price
        return representation

