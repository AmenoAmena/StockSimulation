from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import stock_user,UserStock
from .prices import Price
from django.contrib.auth.decorators import login_required
from .forms import StockTrade

# Create your views here.
@login_required
def index(request):
    user = request.user
    user_instance = stock_user.objects.get(id=user.id)
    user_money = user_instance.get_total_stock_value() + user.money
    stock_value = user_instance.get_total_stock_value()
    user_cash = user.money
    made_money = user_money - 10000
    user_stocks = UserStock.objects.filter(user=user)
    print(user_stocks)
    return render(request, 'Content/index.html', {
        'user_money': user_money,
        'stock_value':stock_value,
        'user_cash':user_cash,
        'made_money':made_money,
        'user_stocks':user_stocks
    })

@login_required
def trade(request):
    form = StockTrade()
    return render(request,"Content/trade.html",{
        'form':form
    })