from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required(login_url='login_user')
def home(request):
    
    return render(request, "index.html")


def register(request):
    
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Created!")
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

@login_required(login_url='login_user')
def logout_user(request):
    
    logout(request)
    return redirect("home")
