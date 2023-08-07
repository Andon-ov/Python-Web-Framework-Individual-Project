from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views

from culinary_recipes.auth_app.forms import SignUpForm
from culinary_recipes.auth_app.models import Profile
from culinary_recipes.core.mixins import OwnerRequiredMixin

UserModel = get_user_model()


class SignUpView(SuccessMessageMixin, views.CreateView):
    template_name = 'auth/sign-up-page.html'
    form_class = SignUpForm
    success_message = 'Вие се регистрирахте успешно в нашия саит!'

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(SuccessMessageMixin, auth_views.LoginView):
    template_name = 'auth/sign-in-page.html'
    success_url = reverse_lazy('index')
    success_message = 'Здравейте и добре дошли!'


class SignOutView(SuccessMessageMixin, auth_mixin.LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'auth/sign-out-page.html'
    success_message = 'Вие се отписахте успешно'


# Profile
class UserDetailsView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DetailView):
    template_name = 'auth/profile-details-page.html'
    model = UserModel


class UserEditView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.UpdateView):
    template_name = 'auth/profile-edit-page.html'
    model = Profile
    fields = ('first_name', 'last_name', 'job_title')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(SuccessMessageMixin, OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DeleteView):
    template_name = 'auth/profile-delete-page.html'

    model = UserModel
    success_url = reverse_lazy('index')
    success_message = 'Вашият профил беше изтрит'


class ChangeUserPasswordView(SuccessMessageMixin, auth_mixin.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'auth/password-change.html'
    success_message = 'Вашата парола беше сменена'
