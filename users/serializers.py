from django.contrib.auth import get_user_model
from rest_framework import serializers


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
        