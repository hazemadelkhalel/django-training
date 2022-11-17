from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response

class UserProfileGenerics(generics.UpdateAPIView, generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    def get_queryset(self):
        try: 
            user = User.objects.get(pk = self.kwargs['pk'])
            userProfile = UserProfile.objects.filter(user = user)
            return userProfile
        except:
            raise Http404
    def update(self, request, *args, **kwargs):
        user = User.objects.get(pk = kwargs['pk'])
        prof = UserProfile.objects.get(user = user)
        serializer = UserProfileSerializer(prof, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)