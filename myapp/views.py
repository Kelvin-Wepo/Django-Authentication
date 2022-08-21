# Create your views here.

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method== "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("/")
    return render(request,'login.html')

       
def register(request):
    if request.method== "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 != password2:
            messages.error(request,"Your Passwords do not Match!! Please Try Again")
            return redirect('/register')
        new_user=User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        new_user.save()
        return render (request,'login.html')
    return render(request,'register.html')

def signout(request):
    logout(request)
    messages.success(request,"You have logged out, we will be glad to have you back again")
    return redirect ("login")

