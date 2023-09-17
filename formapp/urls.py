from django.urls import path, re_path
from formapp import views


urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("", views.index, name="index"),
    re_path(r"^user/", views.user, name="user"),
]
