from rest_framework import serializers
from app.models import Customer
from app.serializers.order import OrderOutSerializer,OrderOutWithoutCustSerializer
from app.serializers.billing import BillingOutSerializer

class CustomerInSerializer(serializers.Serializer):
    org_id=serializers.CharField()
    name=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)
    address=serializers.CharField(required=False)

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        if not data.get('address'):
            data['address']=""
        return data

class CustomerUpdateSerializer(serializers.Serializer):
    cust_id=serializers.CharField()
    org_id=serializers.CharField()
    name=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        return data

class CustomerDeleteSerializer(serializers.Serializer):
    cust_id=serializers.CharField()

class CustomerOutSerializer(serializers.ModelSerializer):

    orders=OrderOutWithoutCustSerializer(many=True,source='customer_order')
    billings=BillingOutSerializer(many=True,source='customer_billing')

    class Meta:
        model=Customer
        fields=(
            'cust_id',
            'organization',
            'name',
            'mobile',
            'email',
            'address',
            'registered_at',
            'orders',
            'billings',
            'is_active',
            'updated_at'
        )

