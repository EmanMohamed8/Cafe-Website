from rest_framework.views import APIView, status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserRegistrationSerializer, UserSerializer, UserLoginSerializer

class UserRegisterationViews(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() 
        token = AuthToken.objects.create(user)
        return Response(
            {
                "message" : "User Created Successfully.",
                "token" : token[1],
                "users" : UserSerializer(user, context=request).data,
            }, 
            status = status.HTTP_201_CREATED
        )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserLoginViews(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)
        return Response({
            "token" : token[1],
            "user": UserSerializer(user, context=request).data,
        })