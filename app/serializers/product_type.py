from rest_framework import serializers
from app.models import ProductType

class ProductTypeInSerializer(serializers.Serializer):
    org_id=serializers.CharField()
    name=serializers.CharField()
    desc=serializers.CharField(required=False)

    def validate(self, attrs):
        if not attrs.get('desc'):
            attrs['desc']="N/A"
        return attrs

class ProductTypeUpdateSerializer(serializers.Serializer):
    p_type_id=serializers.CharField()
    org_id=serializers.CharField()
    name=serializers.CharField()
    desc=serializers.CharField(required=False)
    is_active=serializers.BooleanField()


class ProductTypeDeleteSerializer(serializers.Serializer):
    p_type_id=serializers.CharField()


class ProductTypeOutSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductType
        fields=(
            'p_type_id',
            'name',
            'desc',
            'is_active',
            'created_at',
            'updated_at'
        )
