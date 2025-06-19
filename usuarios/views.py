from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = "usuarios/login2.html"  # asegúrate de usar tu template
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy("admin_dashboard:dashboard")
        return reverse_lazy("core:home")  # o tu vista de inicio para usuarios normales


class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("usuarios:login")
    template_name = "usuarios/registro.html"
