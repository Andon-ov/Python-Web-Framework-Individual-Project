from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class UserDeleteViewTests(TestCase):
    VALID_USER_DATA = {
        'email': 'test@mail.com',
        'password': 'pass',
        'date_joined': datetime.now(),
        'is_admin': True
    }

    def test_user_delete_view__when_delete_user__expect_anonymous_user(self):
        app_user = UserModel.objects.create_user(
            **self.VALID_USER_DATA
        )
        self.client.login(
            **self.VALID_USER_DATA
        )

        response = self.client.delete(reverse('delete user', kwargs={'pk': app_user.pk}), follow=True)
        self.assertNotEqual(response.context['user'], app_user)
