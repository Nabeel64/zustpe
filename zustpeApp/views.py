from django.shortcuts import render
from django.shortcuts import render,redirect
from zustpeApp.forms import Signup
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'html/home.html')


def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
    context={}
    return render(request,'html/login.html',context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/login')


def signup(request):
    if request.method == 'POST':
        a = Signup(request.POST, request.FILES)
        if a.is_valid():
            a.save()
            messages.info(request,'user created!')
            return redirect('/signup')    
        else:
            messages.info(request,'Please enter valid details')
    a = Signup()
    return render(request, 'html/signup.html', {'d':a})