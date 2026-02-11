from rest_framework import serializers
from .models import ConfirmationCode
from users.models import CustomUser
import random
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class OAuthSerializer(serializers.Serializer):
    code = serializers.CharField()
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirmation_code = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "confirmation_code"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create(
            email=validated_data["email"],
            is_active=False
        )
        user.set_password(password)
        user.save()

        code = str(random.randint(100000, 999999))
        ConfirmationCode.objects.create(user=user, code=code)

        user.confirmation_code = code 
        return user


class ConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()