from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def login_view(request):
    return HttpResponse("Hello World")

def logout_view(request):
    user = request.user
    logout(request)
    return redirect("Content:index")
