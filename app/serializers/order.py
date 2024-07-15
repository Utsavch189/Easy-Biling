from rest_framework import serializers
from app.models import Order
from app.serializers.product import ProductOutSerializer

class OrderInSerializer(serializers.Serializer):
    org_id=serializers.CharField()
    customer_id=serializers.CharField()
    product_id=serializers.CharField()
    quantity=serializers.IntegerField()

class OrderUpdateSerializer(serializers.Serializer):
    order_id=serializers.CharField()
    org_id=serializers.CharField()
    customer_id=serializers.CharField()
    product_id=serializers.CharField()
    quantity=serializers.IntegerField()
    is_active=serializers.BooleanField()

class OrderOutSerializer(serializers.ModelSerializer):

    product=ProductOutSerializer()

    class Meta:
        model=Order
        fields=(
            'order_id',
            'organization',
            'product',
            'quantity',
            'order_date',
            'is_active',
            'updated_at'
        )