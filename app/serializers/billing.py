from rest_framework import serializers
from app.models import Billing
from app.serializers.employee import EmployeeOutSerializer
from app.serializers.payment_modes import PaymentModeOutSerializer
from app.serializers.order_biiling_map import BillForOrdersSerializer

class BillingInSerializer(serializers.Serializer):
    customer_id=serializers.CharField()
    payment_mode=serializers.CharField()
    discount=serializers.DecimalField(max_digits=10, decimal_places=2,required=False)
    total_amount=serializers.DecimalField(max_digits=10, decimal_places=2)

class BillingUpdateSerializer(serializers.Serializer):
    bill_id=serializers.CharField()
    customer_id=serializers.CharField()
    payment_mode=serializers.CharField()
    discount=serializers.DecimalField(max_digits=10, decimal_places=2)
    total_amount=serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_price=serializers.DecimalField(max_digits=10, decimal_places=2)
    is_active=serializers.BooleanField()

class BillingOutSerializer(serializers.ModelSerializer):

    billed_by=EmployeeOutSerializer()
    payment_mode=PaymentModeOutSerializer()
    associate_orders=BillForOrdersSerializer(many=True,source='billing_mapping')

    class Meta:
        model=Billing
        fields=(
            'bill_id',
            'organization',
            'billed_by',
            'payment_mode',
            'discount',
            'total_amount',
            'discounted_price',
            'billing_date',
            'is_active',
            'associate_orders',
            'update_at'
        )