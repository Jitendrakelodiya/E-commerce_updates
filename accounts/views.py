from django.shortcuts import render , redirect ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from product.models import *

# Create your views here.

# def buyerbase(request):




def Buyer_register(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        phone_number = request.POST['Number']
        username = request.POST['Username']
        password = request.POST['password']
        user_type = "buyer"

        if len(phone_number) !=10:
            messages.error(request,'Phone Number should be 10 Digit')
            return redirect('Buyer_register')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request,'Username already exists')
            return redirect('Buyer_register')
        
        myuser = User.objects.create_user(email,password)
        myuser.name = name
        myuser.phone_number = phone_number
        myuser.username = username
        myuser.user_type = user_type

        myuser.save()
        
        messages.success(request,'Account created Successfully')
        return redirect('Buyer_Login')
 
    return render(request,"accounts/Buyer_register.html")

def Buyer_Login(request):
    if request.method == "POST":
        email = request.POST.get('Email')
        password = request.POST.get('password')

        if not User.objects.filter(email = email).exists():
            messages.error(request,'Invalid Email')
            return redirect('Buyer_Login')

        user = authenticate(email = email,password= password)
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('Buyer_Login')


        if user is not None:
            login(request,user)
            return redirect('/')

    categories = Category_shop.objects.all()
    context = {
               "categories":categories
                       }
        
    return render(request,"accounts/Buyer_login.html",context)


def Seller_register(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        phone_number = request.POST['Number']
        username = request.POST['Username']
        password = request.POST['password']
        user_type = "seller"

        if len(phone_number) !=10:
            messages.error(request,'Phone Number should be 10 Digit')
            return redirect('Seller_register')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request,'Username already exists')
            return redirect('Seller_register')
        
        myuser = User.objects.create_user(email,password)
        myuser.name = name
        myuser.phone_number = phone_number
        myuser.username = username
        myuser.user_type = user_type

        myuser.save()
        
        messages.success(request,'Account created Successfully')
        return redirect('Seller_Login')
 
    return render(request,"accounts/Seller_register.html")

def Seller_Login(request):
    if request.method == "POST":
        email = request.POST.get('Email')
        password = request.POST.get('password')

        if not User.objects.filter(email = email).exists():
            messages.error(request,'Invalid Email')
            return redirect('Seller_Login')

        user = authenticate(email = email,password= password)
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('Seller_Login')


        if user is not None:
            login(request,user)
            return redirect('common')

# Ye dropdown ke liye he
    categories = Category_shop.objects.all()
    context = {
               "categories":categories
                       }
# Ye dropdown ke liye he
    return render(request,"accounts/Seller_login.html",context)

def Logout_page(request):
    logout(request)
    return redirect('home')

    




