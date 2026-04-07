from django.urls import path
from . import views

app_name = 'ex01'

urlpatterns = [
    path("", views.index),
    path("django/", views.django_view, name="django-view"),
    path("display/", views.display_view, name="display-view"),
    path("templates/", views.templates_view, name="templates-view"),
]
