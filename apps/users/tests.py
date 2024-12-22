from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.urls import reverse

from django.test import TestCase
from apps.users.models import CustomUser
from .api.serializers import UserSerializer


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="securepassword",
            phone="1234567890",
            role="Customer",
            address="123 Test Street",
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.role, "Customer")

    def test_staff_role(self):
        self.user.is_staff = True
        self.user.save()
        self.assertEqual(self.user.role, "Staff")

    def test_admin_role(self):
        self.user.is_superuser = True
        self.user.save()
        self.assertEqual(self.user.role, "Admin")


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="securepassword",
        )

    def test_serializer_output(self):
        serializer = UserSerializer(self.user)
        data = serializer.data
        self.assertEqual(data["email"], "test@example.com")
        self.assertNotIn("password", data)


class CustomUserSaveLogicTest(TestCase):
    def test_staff_role_auto_update(self):
        user = CustomUser.objects.create_user(
            username="staffuser",
            email="staff@example.com",
            password="password",
            is_staff=True,
        )
        self.assertEqual(user.role, "Staff")

    def test_admin_role_auto_update(self):
        user = CustomUser.objects.create_user(
            username="adminuser",
            email="admin@example.com",
            password="password",
            is_superuser=True,
        )
        self.assertEqual(user.role, "Admin")


class UserViewSetTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="securepassword"
        )
        self.url = reverse("users-list")

    def test_get_user_list(self):
        self.client.login(username="testuser", password="securepassword")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)  # Check the total count
        self.assertEqual(len(response.data["results"]), 1)  # Check the number of users in 'results'
        self.assertEqual(response.data["results"][0]["email"], "test@example.com")
