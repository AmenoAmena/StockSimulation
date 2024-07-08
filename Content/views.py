from django.shortcuts import render
from django.http import HttpResponse
from .prices import Price

# Create your views here.
def index(request):

    user = request.user
    user_money = request.POST.get('')

    return render(request, 'Content/index.html', {
    })