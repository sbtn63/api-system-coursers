from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("password not match!!")
        return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, data):
        try:
            user = User.objects.get(username=data.get('username'))
        except User.DoesNotExist:
            raise serializers.ValidationError("Credentials incorrect!!")

        if not user.check_password(data.get('password')):
            raise serializers.ValidationError("Credentials incorrect!!")

        data['user'] = user
        return data