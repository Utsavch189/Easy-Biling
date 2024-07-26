from rest_framework import serializers
from app.models import Billing,Customer
from app.serializers.employee import EmployeeOutSerializer
from app.serializers.payment_modes import PaymentModeOutSerializer
from app.serializers.order_biiling_map import BillForOrdersSerializer

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
class OrderForInBills(serializers.Serializer):
    order_id=serializers.CharField()

class BillingInSerializer(serializers.Serializer):
    orders=OrderForInBills(many=True)
    customer_id=serializers.CharField()
    payment_mode=serializers.CharField()
    is_inter_state=serializers.BooleanField(default=False)

    def validate(self, attrs):
        if not attrs.get('discount'):
            attrs['discount']=0
        return attrs


class BillingDeleteSerializer(serializers.Serializer):
    bill_id=serializers.CharField()

class BillingOutSerializer(serializers.ModelSerializer):

    billed_by=EmployeeOutSerializer()
    payment_mode=PaymentModeOutSerializer()
    associate_orders=BillForOrdersSerializer(source='billing_mapping')

    class Meta:
        model=Billing
        fields=(
            'bill_id',
            'invoice',
            'invoice_path',
            'organization',
            'billed_by',
            'payment_mode',
            'discount',
            'total_amount',
            'discounted_price',
            'cgst_amount',
            'sgst_amount',
            'igst_amount',
            'cgst_rates',
            'sgst_rates',
            'igst_rates',
            'is_inter_state',
            'taxable_amount',
            'billing_date',
            'is_active',
            'associate_orders',
            'updated_at'
        )

class BillingOutWithCustSerializer(serializers.ModelSerializer):

    billed_by=EmployeeOutSerializer()
    payment_mode=PaymentModeOutSerializer()
    customer=CustomerSerializer()
    associate_orders=BillForOrdersSerializer(many=True,source='billing_mapping')

    class Meta:
        model=Billing
        fields=(
            'bill_id',
            'invoice',
            'invoice_path',
            'organization',
            'billed_by',
            'customer',
            'payment_mode',
            'discount',
            'total_amount',
            'discounted_price',
            'cgst_amount',
            'sgst_amount',
            'igst_amount',
            'cgst_rates',
            'sgst_rates',
            'igst_rates',
            'is_inter_state',
            'taxable_amount',
            'billing_date',
            'is_active',
            'associate_orders',
            'updated_at'
        )