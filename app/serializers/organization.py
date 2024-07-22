from rest_framework import serializers
from app.models import Organization
from app.serializers.employee import EmployeeOutSerializer
from app.serializers.product import ProductOutSerializer

class OrganizationInSerializer(serializers.Serializer):
    name=serializers.CharField()
    address=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)

    def validate(self, attrs):
        if not attrs.get('email'):
            attrs['email']=""
        return attrs

class OrganizationUpdateSerializer(serializers.Serializer):
    org_id=serializers.CharField()
    name=serializers.CharField()
    address=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField()

    def validate(self, attrs):
        if not attrs.get('email'):
            attrs['email']=""
        return attrs

class OrganizationOutSerializer(serializers.ModelSerializer):

    employees=EmployeeOutSerializer(many=True,source='organization_employee')
    products=ProductOutSerializer(many=True,source='organization_product')

    class Meta:
        model=Organization
        fields=(
            'org_id',
            'name',
            'address',
            'mobile',
            'email',
            'registered_at',
            'employees',
            'products',
            'is_active',
            'updated_at'
        )
