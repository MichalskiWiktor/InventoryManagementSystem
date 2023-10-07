from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .forms import CreateUserForm

@login_required
def home_page(request):
    contex={}
    return render(request, "inventory/base.html", contex)

def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    contex = {"form":form}
    return render(request, "inventory/register.html", contex)

def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    contex = {"form":form}
    return render(request, "inventory/register.html", contex)
