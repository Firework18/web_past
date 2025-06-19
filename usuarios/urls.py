from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = "usuarios"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("registro/", RegistroUsuarioView.as_view(), name="registro"),
    path("login2/", CustomLoginView.as_view(), name="login2"),
]
