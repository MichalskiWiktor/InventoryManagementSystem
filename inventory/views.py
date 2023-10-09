from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product, Tag, Category
from .forms import CreateUserForm, LoginUserForm

@login_required(login_url="login")
def home_page(request):
    products = Product.objects.all()
    contex={"products":products}
    return render(request, "inventory/list.html", contex)

def login_page(request):
    form = LoginUserForm(request)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    contex = {"form":form}
    return render(request, "inventory/login.html", contex)

def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    contex = {"form":form}
    return render(request, "inventory/register.html", contex)

def logout_page(request):
    logout(request)
    return redirect("login")