import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    friend_code = models.CharField(default=get_random_string, unique=True)
    friends = models.ManyToManyField('self', blank=True)
    blocked_users = models.ManyToManyField('self', blank=True) 