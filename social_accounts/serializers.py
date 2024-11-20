from rest_framework import serializers
from .utils import Google, register_social_user
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

class GoogleSingInSerializer(serializers.Serializer):
    access_token = serializers.CharField(min_length=6)
    
    def validate_access_token(self, access_token):
        google_user_data = Google.validate(access_token)
        try:
            userid = google_user_data["sub"]
        except:
            raise serializers.ValidationError('this token is invalid or expired')

        if google_user_data["aud"] != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed(detail='could not verify your client id')
        email = google_user_data["email"]
        username = google_user_data["given_name"]
        provider = "google"

        return register_social_user(provider, email, username)