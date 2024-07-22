from rest_framework import serializers
from app.models import Product
from app.serializers.product_type import ProductTypeOutSerializer

class ProductInSerializer(serializers.Serializer):
    name=serializers.CharField()
    types=serializers.CharField(required=False)
    desc=serializers.CharField(required=False)
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    discount=serializers.DecimalField(max_digits=10, decimal_places=2,required=False)

    def validate(self, attrs):
        if not attrs.get('desc'):
            attrs['desc']="N/A"
        
        if not attrs.get('discount'):
            attrs['discount']=0

        return attrs

class ProductUpdateSerializer(serializers.Serializer):
    p_id=serializers.CharField()
    name=serializers.CharField()
    types=serializers.CharField(required=False)
    desc=serializers.CharField()
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    discount=serializers.DecimalField(max_digits=10, decimal_places=2,required=False)
    is_available=serializers.BooleanField()


class ProductDeleteSerializer(serializers.Serializer):
    p_id=serializers.CharField()

    
class ProductOutSerializer(serializers.ModelSerializer):

    types=ProductTypeOutSerializer(many=False)

    class Meta:
        model=Product
        fields=(
            'p_id',
            'name',
            'types',
            'desc',
            'price',
            'discount',
            'is_available',
            'added_at',
            'updated_at',
            'is_active'
        )