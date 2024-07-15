from rest_framework import serializers
from app.serializers.order import OrderOutSerializer
from app.models import OrderMapToBilling

class BillForOrdersSerializer(serializers.ModelSerializer):

    order=OrderOutSerializer(many=True)

    class Meta:
        model=OrderMapToBilling
        fields=('order',)
    