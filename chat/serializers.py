from rest_framework import serializers

from .models import *


class ChatroomSerializer(serlializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chatroom
        fields = '__all__'

class MessageSerializer(serlializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

class RoleSerializer(serlializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class NotificationSerializer(serlializers.HyperlinkedModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'
