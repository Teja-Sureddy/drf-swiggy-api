from rest_framework import serializers
from ..models_list.ordered_items import OrderedItems

class OrderedItemsSerializer(serializers.ModelSerializer):
    itemName = serializers.CharField(source='item.name', read_only=True)
    itemPrice = serializers.FloatField(source='item.price', read_only=True)
    itemType = serializers.BooleanField(source='item.type', read_only=True)

    class Meta:
        model = OrderedItems
        fields = '__all__'