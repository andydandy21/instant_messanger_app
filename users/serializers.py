from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        