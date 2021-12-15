from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from django.shortcuts import render
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import CustomUser
from .serializers import CustomUserSerializer


class GoogleLogin(SocialLoginView):

    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.FRONTEND_URL

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer