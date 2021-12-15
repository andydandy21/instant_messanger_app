from rest_framework import viewsets

from .models import Chatroom
from .serializers import *


class ChatroomViewSet(viewsets.ModelViewSet):
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer