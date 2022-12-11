from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from culinary_recipes.auth_app.views import SignUpView, SignInView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView, ChangeUserPasswordView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password-change-done/', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),

    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
