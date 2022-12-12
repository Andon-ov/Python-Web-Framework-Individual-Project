from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tests.base_test_case import BestTestCase

UserModel = get_user_model()


class UserDetailsViewTests(BestTestCase):
    VALID_USER_DATA = {
        'email': 'test@mail.com',
        'password': 'pass',
        'date_joined': datetime.now(),
        'is_admin': True
    }

    def test_user_sign_in_view__when_valid_data__expect_logged_in_user(self):
        UserModel.objects.create_user(**self.VALID_USER_DATA)
        self.client.login(**self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('sign in'))

        self.assertEqual(self.VALID_USER_DATA['email'], response.context['user'].email)
