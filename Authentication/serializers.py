from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.db.models import fields


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        read_only_fields = ['id']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, validators = [validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password1', 'password2')
        extra_kwargs = {'password1': {'write_only': True}, 
                        'password2': {'write_only': True}
                        }
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'].lower(),
            password = validated_data['password1'],
        )
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
