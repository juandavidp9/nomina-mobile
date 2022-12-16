from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id_user', 'email', 'password', 'name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['email'],
            email = validated_data['email'],
            password = validated_data['password'],
            name = validated_data['name'],
            last_name = validated_data['last_name'])
        return user
