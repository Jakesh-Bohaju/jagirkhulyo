from django.conf.urls import url
from django.urls import path

from custom_auth import views
from custom_auth.views import *

app_name = 'custom_auth'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('password_reset', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('activate/account', AccountActivationDoneView.as_view(), name='account_activation_done'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
]
