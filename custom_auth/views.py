from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from custom_auth.forms import *


# Create your views here.

class RegistrationView(CreateView):
    model = User
    # template_name = ''
    form_class = UserForm
    # success_url = '/custom/login'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return redirect('custom_auth:login')


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user

        if user.role == 'company':
            return reverse('company:company_dashboard_index')

        else:
            return reverse('job_seeker:seeker_dashboard_index')


class CustomLogoutView(LogoutView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return redirect('custom_auth:login')



