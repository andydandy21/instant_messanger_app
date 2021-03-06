import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Chatroom(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_chatrooms')
    added_users = models.ManyToManyField(get_user_model(), blank=True, related_name='added_chatrooms')
    banned_users = models.ManyToManyField(get_user_model(), blank=True, related_name='banned_chatrooms')
    date_created = models.DateTimeField(default=timezone.now)

    #create a slug automatically from name on save
    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Message(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(max_length=5000)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

class Role(models.Model):

    users = models.ManyToManyField(get_user_model(), blank=True, related_name='roles')
    name = models.CharField(max_length=50)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='roles')
    #permissions
    can_add_role = models.BooleanField(default=False)
    can_change_name = models.BooleanField(default=False)
    can_invite = models.BooleanField(default=False)
    can_kick = models.BooleanField(default=False)
    can_ban = models.BooleanField(default=False)
    can_send_message = models.BooleanField(default=False)

class Notification(models.Model):

    read = models.BooleanField(default=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    for_message = models.BooleanField(default=False)
    for_chatroom_inv = models.BooleanField(default=False)
    for_friend_request = models.BooleanField(default=False)
    for_friend_added = models.BooleanField(default=False)

