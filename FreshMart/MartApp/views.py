from django.shortcuts import render , redirect,get_object_or_404
from .forms import ProductForm , SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Product
from .forms import OrderForm

# Home view
def home(request):
    return render(request , 'invApp/home.html')

# Create View 
def product_create_view(request):
    form = ProductForm()
    if(request.method == 'POST'):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request , 'invApp/product_form.html' , {'form' : form})

# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request , 'invApp/product_list.html' , {'products' : products})

# Update View
def product_update_view(request , product_id):
    product = Product.objects.get(product_id = product_id)
    form = ProductForm()
    if(request.method == 'POST'):
        form = ProductForm(request.POST , instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request , 'invApp/product_form.html' , {'form' : form})

# Delete View
def product_delete_view(request , product_id):
    product = Product.objects.get(product_id = product_id)
    if(request.method == 'POST'):
        product.delete()
        return redirect('product_list')
    return render(request , 'invApp/product_confirm_delete.html' , {'product' : product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'invApp/product_form.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")  # Change URL as needed
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request , 'invApp/login.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")

            return redirect("/login/")
    else:
        form = SignupForm()
    return render(request , 'invApp/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/login/")

def place_order(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            product.quantity -= 1
            product.save()
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'invApp/place_order.html', {
        'form': form,
        'product': product
    })


def order_success(request):
    return render(request, 'invApp/order_success.html')