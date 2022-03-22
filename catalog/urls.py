from . import views
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("load-more-music/", views.MusicLoad, name="load-more-music"),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]
