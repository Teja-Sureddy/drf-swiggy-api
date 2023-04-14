from rest_framework import serializers
from ..models_list.restaurant import Restaurant
from ..models import User


class RestaurantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role__name='manager'))
    userName = serializers.CharField(source='user.username', read_only=True)
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Restaurant
        fields = '__all__'

    def validate(self, data):
        if len(data['name']) < 4:
            raise serializers.ValidationError("Name should have minimum 4 characters.")  
        return data