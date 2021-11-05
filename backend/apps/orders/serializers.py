from apps.order_items.serializers import OrderItemSerializer
from .models import Order
from rest_framework import serializers
from apps.order_items.models import OrderItem


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            'user',
            'customer_name',
            'customer_phone',
            'address',
            'pin_code',
            'building_type',
            'city',
            'state',
            'total_price',
            'total_qty',
            'order_items'
        ]
    
    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(**item, order=order)

        return order

class OrderListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'