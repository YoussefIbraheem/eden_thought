from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ThoughtForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Thought


@login_required(login_url="login_user")
def home(request):
    query = Thought.objects.filter(user=request.user)
    context = {"thoughts": query.all()}
    return render(request, "index.html", context)


def register(request):

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created!")
            return redirect("login_user")
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):

    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    context = {"form": form}
    return render(request, "login.html", context)


@login_required(login_url="login_user")
def logout_user(request):

    logout(request)
    return redirect("home")


@login_required(login_url="login_user")
def create_thought(request):
    if request.method == "POST":
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            return redirect("home")
    else:
        form = ThoughtForm()
    context = {"form": form}
    return render(request, "create_thought.html", context)
