from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

UserModel = get_user_model()


class UserDetailsViewTests(TestCase):
    VALID_USER_DATA = {
        'email': 'test@mail.com',
        'password': 'pass',
        'date_joined': datetime.now(),
        'is_admin': True
    }

    def test_user_details_view__when_valid_data__expect_authenticated_user(self):
        app_user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.client.login(**self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': app_user.pk}))

        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
