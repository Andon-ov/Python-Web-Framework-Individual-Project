from django.contrib import messages
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views, login, get_user_model, update_session_auth_hash
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from culinary_recipes.auth_app.forms import SignUpForm
from culinary_recipes.auth_app.models import Profile


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up-page.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    # Signs the user in, after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in-page.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out-page.html'


UserModel = get_user_model()


# Profile
class UserDetailsView(views.DetailView):
    template_name = 'auth/profile-details-page.html'
    model = UserModel


class UserEditView(views.UpdateView):
    template_name = 'auth/profile-edit-page.html'
    model = Profile

    fields = ('first_name', 'last_name', 'job_title')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'auth/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


def change_password(request):
    if request.method == 'POST':
        form = auth_forms.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = auth_forms.PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'auth/password-change.html', context)
