import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    friend_code = models.CharField(default=get_random_string, max_length=12, unique=True, editable=False)
    friends = models.ManyToManyField('self', blank=True, related_name='friends')
    pending_friend_requests = models.ManyToManyField('self', blank=True, related_name='friend_requests')
    blocked_users = models.ManyToManyField('self', blank=True, related_name='blocked_users') 
    profile_picture = models.ImageField(default='default.png')

