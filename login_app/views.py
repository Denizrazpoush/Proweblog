from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


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
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if User.objects.get(username=username) and password1 != password2:
            context["errors"].append(" username is already exists ")
            context["errors"].append(" Password is not same ")
            return render(request, "login_app/register.html", context)
        if password1 != password2:
            context["errors"].append(" Password is not same ")
            return render(request, "login_app/register.html", context)
        if User.objects.get(username=username):
            context["errors"].append(" username is already exists ")
            return render(request, "login_app/register.html", context)

        user = User.objects.create(username=username, password=password1, email=email)
        login(request, user)
        return redirect("/")
    return render(request, "login_app/register.html", {})





