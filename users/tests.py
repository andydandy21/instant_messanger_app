from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def setUp(self):

        User = get_user_model()
        self.friend = User.objects.create_user(
            username='frienduser',
            email='frienduser@email.com',
            password='testpass123',
        )
        self.pending_friend = User.objects.create_user(
            username='pendingfriend',
            email='pendingfriend@email.com',
            password='testpass123',
        )
        self.blocked_user = User.objects.create_user(
            username='blockeduser',
            email='blockeduser@email.com',
            password='testpass123',
        )
        self.custom_user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123',
        )
        self.custom_user.friends.add(self.friend)
        self.custom_user.pending_friend_requests.add(self.pending_friend)
        self.custom_user.blocked_users.add(self.blocked_user)
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='testpass123',
        )

    def test_create_user(self):

        self.assertEqual(self.custom_user.username, 'testuser')
        self.assertEqual(self.custom_user.email, 'testuser@email.com')
        self.assertEqual(self.custom_user.profile_picture, 'default.png')
        self.assertEqual(len(self.custom_user.friend_code), 12)
        self.assertEqual(self.custom_user.friends.first().username, 'frienduser')
        self.assertEqual(self.custom_user.pending_friend_requests.first().username, 'pendingfriend')
        self.assertEqual(self.custom_user.blocked_users.first().username, 'blockeduser')
        self.assertTrue(self.custom_user.is_active)
        self.assertFalse(self.custom_user.is_staff)
        self.assertFalse(self.custom_user.is_superuser)


    def test_create_superuser(self):

        self.assertEqual(self.admin_user.username, 'admin')
        self.assertEqual(self.admin_user.email,'admin@email.com')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
        

