from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import *


class ChatroomTests(TestCase):

    def setUp(self):

        User = get_user_model()
        self.owner_user = User.objects.create_user(
            username = 'owner_user',
            email = 'owner_user@email.com',
            password = 'testpass123'
        )
        self.banned_user = User.objects.create_user(
            username = 'banned_user',
            email = 'banned_user@email.com',
            password = 'testpass123'
        )
        self.added_user = User.objects.create_user(
            username = 'added_user',
            email = 'added_user@email.com',
            password = 'testpass123'
        )
        self.chatroom = Chatroom.objects.create(
            name = 'the test room',
            owner = self.owner_user,
        )
        self.chatroom.added_users.add(self.added_user)
        self.chatroom.banned_users.add(self.banned_user)
        self.message = Message.objects.create(
            message = 'this is my message',
            chatroom = self.chatroom,
            author = self.owner_user
        )
        self.role = Role.objects.create(
            name='role test',
            chatroom = self.chatroom,
            can_change_name=True,
            can_invite=True,
            can_kick=True,
            can_send_message=True
        )
        self.role.users.add(self.owner_user, self.added_user)
        self.notification = Notification.objects.create(
            user=self.owner_user,
            for_message=True
        )

    def test_chatroom(self):

        self.assertEqual(self.chatroom.name, 'the test room')
        self.assertEqual(self.chatroom.owner.username, 'owner_user')
        self.assertEqual(self.chatroom.slug, 'the-test-room')
        self.assertEqual(self.chatroom.added_users.first().username, 'added_user')
        self.assertEqual(self.chatroom.banned_users.first().username, 'banned_user')
        
    def test_message(self):

        self.assertEqual(self.message.message, 'this is my message')
        self.assertEqual(self.message.chatroom, self.chatroom)
        self.assertEqual(self.message.author, self.owner_user)

    def test_role(self):

        self.assertEqual(self.role.name, 'role test')
        self.assertEqual(self.role.chatroom, self.chatroom)
        self.assertFalse(self.role.can_add_role)
        self.assertTrue(self.role.can_change_name)
        self.assertTrue(self.role.can_invite)
        self.assertTrue(self.role.can_kick)
        self.assertFalse(self.role.can_ban)
        self.assertTrue(self.role.can_send_message)

    def test_notification(self):

        self.assertFalse(self.notification.read)
        self.assertEqual(self.notification.user, self.owner_user)
        self.assertTrue(self.notification.for_message)
        self.assertFalse(self.notification.for_chatroom_inv)
        self.assertFalse(self.notification.for_friend_request)
        self.assertFalse(self.notification.for_friend_added)




