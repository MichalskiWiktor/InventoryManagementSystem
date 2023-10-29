from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category
from .forms import CreateUserForm, LoginUserForm, ProductForm
from django.http import JsonResponse, HttpResponse

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
    required_fields = ['image', 'name', 'category', 'stock', 'selling_price']
    form = ProductForm(request.POST or None, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return HttpResponse("Validation error")

    return render(request, 'inventory/new_product.html', {'form': form, 'available_fields': required_fields})

def get_field_data(request):
    field_name = request.GET.get('field_name', '').lower()
    form = ProductForm()
    field = form.fields.get(field_name)
    typeField = ''

    if type(field).__name__ in ['FloatField', 'IntegerField']:
        typeField = "number"
    elif type(field).__name__ == "ImageField":
        typeField = "image"
    elif type(field).__name__ == "DateField":
        typeField = "date"
    else:
        typeField = "text"
    
    if field_name in form.fields:
        data = {
            'success': True,
            'id': form[field_name].id_for_label,
            'type': typeField,
            'name': form[field_name].name,
            'label': form[field_name].label,
        }
    else:
        data = {'success': False}
    
    return JsonResponse(data)

def update_product(request, pk):
    obj = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            # Return the form with errors
            return render(request, 'inventory/update_product.html', {'form': form, 'product': obj})
    else:
        form = ProductForm(instance=obj)
        return render(request, 'inventory/update_product.html', {'form': form, 'product': obj})

    

def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect("home")