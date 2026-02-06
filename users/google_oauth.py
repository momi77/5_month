import requests
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import OAuthSerializer  

import os
from dotenv import load_dotenv

load_dotenv()

User = get_user_model()


class GoogleLoginAPIView(GenericAPIView):
    serializer_class = OAuthSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

  
        code = serializer.validated_data["code"]

   
        token_response = requests.post(
            url="https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "redirect_uri": os.getenv("REDIRECT_URI"),
                "grant_type": "authorization_code"
            }
        )

        token_data = token_response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            return Response({"error": "Invalid access token!"})

        user_info = requests.get(
            url="https://www.googleapis.com/oauth2/v3/userinfo",
            params={"alt": "json"},
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        email = user_info.get("email")
        first_name = user_info.get("given_name", "")
        last_name = user_info.get("family_name", "")

        if not email:
            return Response({"error": "Email not provided by Google"})

        user, created = User.objects.get_or_create(
            email=email
        )

        if created:
            user.first_name = first_name
            user.last_name = last_name
            user.registration_source = "google"

        else:
            user.first_name = first_name
            user.last_name = last_name

        user.is_active = True
        user.last_login = timezone.now()
        user.save()

        refresh = RefreshToken.for_user(user)
        refresh["email"] = user.email
        refresh["birthdate"] = str(user.birthdate)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
