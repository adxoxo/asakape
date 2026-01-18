from rest_framework import serializers
from .models import Cafe,Tags

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','aesthetic', 'specialty']

class CafeSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    class Meta:
        model = Cafe 
        fields = [
            'id',
            'name', 
            'address', 
            'location_x', 
            'location_y', 
            'price_level', 
            'atmosphere', 
            'wifi_type', 
            'socket_availability', 
            'is_24_7', 
            'open_time', 
            'close_time', 
            'tags',
            'thumbnail'
            ]