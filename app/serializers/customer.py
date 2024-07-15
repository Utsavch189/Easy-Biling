from rest_framework import serializers
from app.models import Customer
from app.serializers.order import OrderOutSerializer
from app.serializers.billing import BillingOutSerializer

class CustomerInSerializer(serializers.Serializer):
    org_id=serializers.CharField()
    name=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        return data

class CustomerUpdateSerializer(serializers.Serializer):
    cust_id=serializers.CharField()
    org_id=serializers.CharField()
    name=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)
    is_active=serializers.BooleanField()

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        return data

class CustomerOutSerializer(serializers.ModelSerializer):

    orders=OrderOutSerializer(many=True,source='customer_order')
    billings=BillingOutSerializer(many=True,source='customer_billing')

    class Meta:
        model=Customer
        fields=(
            'cust_id',
            'name',
            'mobile',
            'email',
            'registered_at',
            'orders',
            'billings',
            'is_active',
            'updated_at'
        )