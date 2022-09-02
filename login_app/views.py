from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model


# Create your views here.


def user_login(request):


    if request.user.is_authenticated == True:
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, "login_app/index.html", {})

def user_logout(request):

    logout(request)
    return redirect('/')


def user_register(request):

    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('/')

    if request.method == "POST":
        username1 = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")

        user = User.objects.filter(username=username1).exists()

        if user and password2!=password1:
            context["errors"].append("the passwords are not same ! ")
            context["errors"].append("the username is alresdy exist ")
            return render(request, "login_app/register.html", context)

        if user:
            context["errors"].append("the username is alresdy exist ")
            return render(request, "login_app/register.html", context)
        if password1 != password2:
            context["errors"].append("the passwords are not same ! ")
            return render(request, "login_app/register.html", context)

        user = User.objects.create(username=username1, password=password1, email=email)
        login(request, user)
        return redirect("/")

    return render(request, "login_app/register.html", {})





