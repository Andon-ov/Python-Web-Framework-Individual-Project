from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from culinary_recipes.auth_app.models import Profile, JobTitle

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
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
        max_length=LAST_NAME_MAX_LENGTH,
    )
    job_title = forms.ChoiceField(
        choices=JobTitle.choices(),
    )

    class Meta:
        model = UserModel
        fields = (
            UserModel.USERNAME_FIELD,
            'password1',
            'password2',
            'first_name',
            'last_name',
            'job_title'
        )

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


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = auth_forms.ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password',
            'is_active',
            'is_admin'
        )
