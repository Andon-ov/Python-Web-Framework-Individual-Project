from django.urls import path, include

from culinary_recipes.auth_app.views import SignUpView, SignInView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView, change_password

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('password/', change_password, name='change password'),

    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
