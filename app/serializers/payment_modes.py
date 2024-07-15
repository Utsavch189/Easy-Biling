from rest_framework import serializers
from app.models import PaymentMode

class PaymentModeInSerializer(serializers.Serializer):
    org_id=serializers.CharField()
    name=serializers.CharField()

class PaymentModeOutSerializer(serializers.ModelSerializer):

    class Meta:
        model=PaymentMode
        fields=(
            'mode_id',
            'name',
            'is_active'
        )