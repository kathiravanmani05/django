import json
from django.http import JsonResponse
from django.shortcuts import redirect, render ,HttpResponse
from .models import *
from django.contrib import messages
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    products = Product.objects.filter(trending = 1)
    return render(request , 'shop/index.html', {"products":products})

def remove_cart(request,cid):
    cartitem = Cart.objects.get(id = cid)
    cartitem.delete()
    return redirect('/cart')

def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user = request.user)
        return render(request , 'shop/cart.html', {"cart":cart})
    else:
        return redirect('/')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.error(request,"Loggedout in Sucessfully")
    return redirect('/')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user =authenticate(request , username =name , password =pwd)
            if user is not None:
                login(request,user)  
                messages.error(request,"Logged in Sucessfully")
                return redirect('/')
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect('/login')
        return render(request , 'shop/login.html')


def register(request):
    form =CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registartion Sucess you can Login Now .. !")
            return redirect('/login')
    return render(request , 'shop/register.html', {"form":form})

def collections(request):
    category = Category.objects.filter(status = 0)
    return render(request , 'shop/collections.html' , {"category":category})

def collectionsview(request,name):
    if (Category.objects.filter(name= name, status = 0)):
        products = Product.objects.filter(category__name = name)
        return render(request , 'shop/products/index.html' , {"products":products, "category_name":name})

    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')
    
def product_details(request,cname,pname):
    if (Category.objects.filter(name= cname, status = 0)):
        if (Product.objects.filter(name= pname, status = 0)):
            products = Product.objects.filter(name= pname, status = 0).first()
            return render(request , 'shop/products/product_details.html',{"products":products})
        else:
            messages.warning(request,"No Such Product Found")
            return redirect('collections')


    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')

def add_to_cart(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            #print(product_qty,product_id)
            #print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id , product_id = product_id):
                    return JsonResponse({'status': 'Product Already in cart'}, status=200)
                else:
                   if product_status.qtuantity >= product_qty: 
                    Cart.objects.create(user=request.user , product_id = product_id,product_qty=product_qty)
                    return JsonResponse({'status': 'Product added to cart'}, status=200)
                   else:
                       return JsonResponse({'status': 'Product Srock Not Available'}, status=200)
        else:
            return JsonResponse({'status':'Login to Add to Cart'}, status =200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status =200)