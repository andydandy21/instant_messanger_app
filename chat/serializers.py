from rest_framework import serializers

from .models import *


class ChatroomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Chatroom
        fields = '__all__'

class MessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class NotificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'
