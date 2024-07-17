from rest_framework import serializers
from app.models import Order,Customer
from app.serializers.product import ProductOutSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=(
            'cust_id',
            'name',
            'mobile',
            'email',
            'registered_at',
            'is_active',
            'updated_at'
        )

class OrderInSerializer(serializers.Serializer):
    customer_id=serializers.CharField(required=False)
    customer_phone=serializers.CharField(required=False)
    product_id=serializers.CharField()
    quantity=serializers.IntegerField()

class OrderUpdateSerializer(serializers.Serializer):
    order_id=serializers.CharField()
    customer_id=serializers.CharField(required=False)
    customer_phone=serializers.CharField(required=False)
    product_id=serializers.CharField()
    quantity=serializers.IntegerField()
    is_active=serializers.BooleanField()

class OrderDeleteSerializer(serializers.Serializer):
    order_id=serializers.CharField()

class OrderOutSerializer(serializers.ModelSerializer):

    product=ProductOutSerializer()
    customer=CustomerSerializer()

    class Meta:
        model=Order
        fields=(
            'order_id',
            'organization',
            'product',
            'customer',
            'quantity',
            'order_date',
            'is_active',
            'updated_at'
        )
