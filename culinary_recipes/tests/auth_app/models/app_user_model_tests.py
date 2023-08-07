from django.contrib.auth import get_user_model
from django.utils.datetime_safe import datetime

from tests.base_test_case import BestTestCase

UserModel = get_user_model()


class UserModelProfileTests(BestTestCase):
    VALID_USER_DATA = {
        'email': 'test@mail.com',
        'password': 'pass',
        'date_joined': datetime.now(),
        'is_admin': True
    }

    def test_create_app_user__expect_work_correctly(self):
        user = self.creat_and_login_user(**self.VALID_USER_DATA)
        self.assertEqual(user.pk, 1)

    def test_create_superuser__expect_work_correctly(self):
        admin_user = UserModel.objects.create_superuser(
            **self.VALID_USER_DATA
        )
        admin_user.full_clean()
        admin_user.save()

        self.assertEqual(admin_user.email, 'test@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
