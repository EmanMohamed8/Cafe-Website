from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

User = get_user_model()


class UserGetViews(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist: 
            return Http404

    def get(self, request, pk, format = None):
        user = self.get_object(pk)
        serializer =  UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, pk, format = None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format = None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data, partial = True)
        # if request.user.pk == user.pk:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
