from rest_framework import serializers
from app.models import Employee,TwoFactorVerification
from app.serializers.role import RoleOutSerializer

class EmployeeInSerializer(serializers.Serializer):
    name=serializers.CharField()
    role_id=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField(required=False)
    password=serializers.CharField()

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        return data

class EmployeeUpdateSerializer(serializers.Serializer):
    emp_id=serializers.CharField()
    name=serializers.CharField()
    role_id=serializers.CharField()
    mobile=serializers.CharField()
    email=serializers.EmailField()

    def validate(self, data):
        if not data.get('email'):
            data['email']=""
        return data

class EmployeeDeleteSerializer(serializers.Serializer):
    emp_id=serializers.CharField()

class EmployeeOutSerializer(serializers.ModelSerializer):

    role=RoleOutSerializer()
    qr_path = serializers.SerializerMethodField()

    class Meta:
        model=Employee
        fields=(
            'emp_id',
            'name',
            'role',
            'mobile',
            'email',
            'registered_at',
            'verified_at',
            'is_active',
            'qr_path',
            'updated_at'
        )
    
    def get_qr_path(self, obj):
        try:
            two_factor = TwoFactorVerification.objects.get(user_id=obj.emp_id)
            return two_factor.qr_path
        except TwoFactorVerification.DoesNotExist:
            return None