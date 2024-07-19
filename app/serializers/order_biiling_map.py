from rest_framework import serializers
from app.serializers.order import OrderOutWithoutCustSerializer
from app.models import OrderMapToBilling

class BillForOrdersSerializer(serializers.ModelSerializer):

    order=OrderOutWithoutCustSerializer()

    class Meta:
        model=OrderMapToBilling
        fields=('order',)
    