from rest_framework import serializers

from .models import *


class ChatroomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chatroom
        fields = [
            'url',
            'id',
            'slug',
            'name',
            'owner',
            'added_users',
            'banned_users',
            'date_created',
            'messages',
            'roles',
        ]

class MessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = [
            'id',
            'message',
            'chatroom',
            'author',
            'date_created',
        ]

class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = [
            'name',
            'chatroom',
            'can_add_role',
            'can_change_name',
            'can_invite',
            'can_kick',
            'can_ban',
            'can_send_message',
        ]

class NotificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Notification
        fields = [
            'read',
            'user',
            'for_message',
            'for_chatroom_inv',
            'for_friend_request',
            'for_friend_added',
        ]
