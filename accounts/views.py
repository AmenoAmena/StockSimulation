from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate,login
from .forms import RegisterForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Content:index")
        else:
            return redirect("Content:index")
    return render(request,"accounts/login.html")

def logout_view(request):
    user = request.user
    logout(request)
    return redirect("Content:index")

def register_view(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html",{
        'form':form
    })