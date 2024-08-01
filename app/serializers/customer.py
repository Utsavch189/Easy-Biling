from rest_framework import serializers
from app.models import Customer
from app.serializers.order import OrderOutSerializer,OrderOutWithoutCustSerializer
from app.serializers.billing import BillingOutSerializer

class CustomerInSerializer(serializers.Serializer):
    name=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)
    address=serializers.CharField(required=False)

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        if not data.get('address'):
            data['address']=""
        data['name']=data['name'].upper()
        return data

class CustomerUpdateSerializer(serializers.Serializer):
    cust_id=serializers.CharField()
    name=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)
    address=serializers.CharField(required=False)

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        if not data.get('address'):
            data['address']=""
        data['name']=data['name'].upper()
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

