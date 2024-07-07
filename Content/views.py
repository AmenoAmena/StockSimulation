from django.shortcuts import render
from django.http import HttpResponse
from .prices import getting_prices

# Create your views here.
def index(request):
    prices = getting_prices()
    return render(request, 'Content/index.html',{
        'prices_dict': prices.items()
    })
