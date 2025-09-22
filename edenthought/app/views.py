from django.shortcuts import render
from .forms import RegisterForm


def home(request):
    return render(request, "index.html")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "register.html", context)
