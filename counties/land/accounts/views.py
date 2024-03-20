from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserForm

def user_register(request):
    form =CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registartion Sucess you can Login Now .. !")
            return redirect('accounts/login')
    return render(request , 'registration/register.html', {"form":form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/accounts/login/')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
