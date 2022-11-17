from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth import authenticate
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    confirmation_password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirmation_password')
    def validate(self, data):
        # checking on passwords
        if(len(data['password']) < 8):
            raise serializers.ValidationError("Password must be at least 8 characters long")
        if not any(char.isalpha() for char in data['password']):
            raise serializers.ValidationError('Password must contain at least 1 letter.')
        if data['password'] != data['confirmation_password']:
            raise serializers.ValidationError("the passwords miss match!")
        return data
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user