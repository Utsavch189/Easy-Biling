from rest_framework import serializers
from app.models import Role

class RoleInSerializer(serializers.Serializer):
    org_id=serializers.CharField(required=False)
    name=serializers.CharField()


class RoleOutSerializer(serializers.ModelSerializer):

    class Meta:
        model=Role
        fields=(
            'role_id',
            'name',
            'created_at',
            'is_active'
        )