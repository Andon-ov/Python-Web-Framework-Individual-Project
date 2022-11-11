from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from culinary_recipes.auth_app.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    WAITER = 'Waiter'
    COOK = 'Cook'
    MANAGER = 'Manager'
    JOB_TITLE_CHOICES = [(x, x) for x in (WAITER, COOK, MANAGER)]

    FIRST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 30

    first_name = forms.CharField(
        min_length=FIRST_NAME_MIN_LENGTH,
        max_length=FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        min_length=LAST_NAME_MIN_LENGTH,
        max_length=LAST_NAME_MAX_LENGTH
    )
    job_title = forms.ChoiceField(
        choices=JOB_TITLE_CHOICES,
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'job_title')

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            job_title=self.cleaned_data['job_title'],
            user=user,
        )
        if commit:
            profile.save()

        return user
