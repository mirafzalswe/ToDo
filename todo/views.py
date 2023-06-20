from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'todo/index.html')

def todo(request):
    return render(request, 'todo/todo.html')

def about(request):
    return render(request, 'todo/about.html')

def login(request):
    return render(request, 'todo/login.html')
def register(request):
    if request.method == "POST":
        username1 = request.POST['uname']
        password1 = request.POST['psw']
        passwrod2 = request.POST['psw agn']
        if User.objects.filter(uname=username1):
            form = "this username already exist"
            return render(request, 'todo/register.html', {
                'form': form
            })
        if password1 != passwrod2:
            form = "Password mismatch"
            return render(request, 'todo/register.html', context={
                'form': form
            })
        if password1 != passwrod2:
            user = User.objects.create_user(uname=username1, password=password1)
            user.save()
            return redirect('/')


        return render(request,'todo/register.html')


    return render(request, 'todo/register.html')
