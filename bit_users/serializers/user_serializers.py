from rest_framework import serializers
from bit_users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('id', 'username','email','first_name','last_name')
        
        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                id=validated_data['id'],
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
        )
            return user
