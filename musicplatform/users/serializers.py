from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        extra_kwargs = {'username': {'validators': []}}
        fields = ('username','email')
    def update(self, instance, validated_data):
        instance.username = instance.username
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ('user', 'bio')
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        if 'email' in user_data:
            user.email = user_data['email']
        if 'username' in user_data:
            user.username = user_data['username']
        user.save()
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance