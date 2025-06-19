from django.urls import path
from .views import *

urlpatterns = [
    path("category/", CategoryList.as_view(), name="mark_list"),
    path("category/save", category_save, name="category_save"),
    path("category/delete/<int:pk>", category_delete, name="category_delete"),
]
