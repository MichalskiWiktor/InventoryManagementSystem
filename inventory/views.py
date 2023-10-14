from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category
from .forms import CreateUserForm, LoginUserForm, ProductForm

@login_required(login_url="login")
def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    contex={"products":products, "categories":categories, "forms":getForms(products)}
    return render(request, "inventory/list.html", contex)

def getForms(products):
    forms = {} 
    for product in products:
        form = ProductForm(instance=product)
        forms[product.pk] = form
    return forms

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

@login_required(login_url="login")
def logout_page(request):
    logout(request)
    return redirect("login")

def add_product(request):
    # When user will be creating new Product types to add products faster this will be done dynamically
    available_fields = ['name', 'category', 'stock', 'sku', 'barcode'] 
    form = ProductForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")

    return render(request, 'inventory/new_product.html', {'form': form, 'available_fields': available_fields})
    

# def update_product(request, pk):
#     obj = Product.objects.get(pk=pk)
#     form = NewItemForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save() # save method can create new object or update and existing one 
#     return redirect("home")
    

def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect("home")