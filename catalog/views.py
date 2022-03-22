from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from catalog.forms import CustomUserCreationForm
from . import test_instruments2 as ti2
from del_mid import del_mid_def
from uuid import uuid4
from time import time


def index(request):
    del_mid_def()
    return render(request, "index.html")


def MusicLoad(request):
    del_mid_def()
    data = []
    obj = {}
    name1 = ""
    inst = ""
    if request.user.username != "":
        name1 = (
            str(uuid4())
            + "__"
            + request.user.username
            + "__"
            + str(int(time()))
            + ".mid"
        )
        inst = ti2.test5_chord_def(name="/home/tatem2/tatem2/static/" + name1)
        obj["link-music"] = name1
        obj["inst"] = inst
    data.append(obj)
    return JsonResponse({"data": data})


def menu(request):
    del_mid_def()
    reg = False
    name1 = ""
    inst = ""
    if request.user.username != "":
        del_mid_def()
        reg = True
        name1 = (
            str(uuid4())
            + "__"
            + request.user.username
            + "__"
            + str(int(time()))
            + ".mid"
        )
        inst = ti2.test5_chord_def(name="/home/tatem2/tatem2/static/" + name1)
    return render(
        request,
        "users/menu.html",
        {"name1": "/static/" + name1, "reg": reg, "inst": inst},
    )


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("menu"))
        else:
            name_errors = form.errors
            name_errors = list(name_errors.keys())
            info_name_errors = {
                "email": "Вы некорректно ввели почту.",
                "password2": "Пароли некорректны или  не совпадают.",
                "username": "Такой user  уже есть.",
            }
            info_errors = []
            for i in name_errors:
                info_errors.append(info_name_errors[i])
            return render(
                request,
                "users/register.html",
                {"form": CustomUserCreationForm, "info_errors": info_errors},
            )
