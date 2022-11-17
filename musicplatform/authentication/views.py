from users.models import UserProfile
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import permissions
from knox.auth import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from . import serializers
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        UserProfile.objects.create(user = user)
        return Response({
        "token": AuthToken.objects.create(user)[1],
        "user": {
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'bio':UserProfile.objects.get(user = user).bio
            }
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
        "token": AuthToken.objects.create(user)[1],
        "user": {
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'bio':UserProfile.objects.get(user = user).bio
            }
        })