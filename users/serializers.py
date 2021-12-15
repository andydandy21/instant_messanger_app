from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from dj_rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers

from .forms import CustomPasswordResetForm


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'url',
            'id',
            'username',
            'email',
            'friend_code',
            'friends',
            'pending_friend_requests',
            'blocked_users',
            'profile_picture'
        ]
        
class CustomPasswordResetSerializer(PasswordResetSerializer):

    @property
    def password_reset_form_class(self):
        if 'allauth' in settings.INSTALLED_APPS:
            return CustomPasswordResetForm
        else:
            return PasswordResetForm