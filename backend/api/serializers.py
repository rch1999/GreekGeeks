from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email',
            'is_admin',
            'is_staff',
            'created',
            'updated',
        ]