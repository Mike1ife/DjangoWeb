from django.shortcuts import render, redirect
from web.forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def base(request):
    return redirect("/login")


def info(request):
    username = request.user.username
    context = {"username": username}
    return render(request, "info.html", context)


def mock(request):
    username = request.user.username
    context = {"username": username}
    return render(request, "mock.html", context)


def identity(request):
    username = request.user.username
    context = {"username": username}
    return render(request, "identity.html", context)


@login_required(login_url="Login")
def index(request):
    return render(request, "accounts/index.html")


def sign_up(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/info")  # 重新導向到首頁
        else:
            # Invalid login credentials
            messages.error(request, "Invalid username or password. Please try again.")

    context = {"form": form}
    return render(request, "accounts/login.html", context)


def log_out(request):
    logout(request)
    return redirect("/login")
