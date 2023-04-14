from rest_framework import serializers
from ..models_list.menu import Menu


class MenuSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Menu
        fields = '__all__'