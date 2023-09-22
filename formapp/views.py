from django.shortcuts import render
from .forms import UserProfileInfoForm, UserForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "formapp/index.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request,
        "formapp/registration.html",
        {
            "registered": registered,
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print("username", user)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

            else:
                return HttpResponse("No such account")
        else:
            print(f"Username : {username} failed login ")
            return HttpResponse("Invalid login payload")
    else:
        return render(request, "formapp/login.html", {})
