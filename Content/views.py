from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import stock_user,UserStock,Stock
from .prices import Price
from django.contrib.auth.decorators import login_required
from .forms import StockTrade
from django.core.exceptions import ValidationError


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
    return render(request, 'Content/index.html', {
        'user_money': user_money,
        'stock_value':stock_value,
        'user_cash':user_cash,
        'made_money':made_money,
        'user_stocks':user_stocks
    })


@login_required
def trade(request):
    user = request.user
    if request.method == 'POST':
        print("Post works")
        form = StockTrade(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            quantity = form.cleaned_data['quantity']
            action = form.cleaned_data['action']
            
            if action == 'buy':
                print("Seeing buy")
                try:
                    buy_stock(user, symbol, quantity)
                except ValidationError as e:
                    form.add_error(None, e)
            elif action == 'sell':
                try:
                    sell_stock(user, symbol, quantity)
                except ValidationError as e:
                    form.add_error(None, e)
            else:
                pass
            return redirect('Content:index')
        else:
            return redirect('Content:trade')
    else:
        form = StockTrade()

    return render(request, "Content/trade.html", {
        'form': form
        })


def buy_stock(user, stock, quantity):
    user_stock = UserStock.objects.filter(user=user, stock=stock).first()
    if user_stock:
        user_stock.quantity += quantity
    else:
        user_stock = UserStock(user=user, stock=stock, quantity=quantity)

    stock_price = stock.price
    total_cost = stock_price * quantity

    if user.money < total_cost:
        raise ValidationError("Insufficient funds to buy stock.")

    user.money -= total_cost
    user.save()
    user_stock.save()

def sell_stock(user, stock, quantity):
    user_stock = UserStock.objects.filter(user=user, stock=stock).first()
    if not user_stock or user_stock.quantity < quantity:
        raise ValidationError("Insufficient stock quantity to sell.")

    stock_price = stock.price
    total_gain = stock_price * quantity

    user.money += total_gain
    user.save()

    user_stock.quantity -= quantity
    if user_stock.quantity == 0:
        user_stock.delete()
    else:
        user_stock.save()


def show_market(request):
    stocks = Stock.objects.all()
    return render(request, 'Content/market.html',{
        'stocks':stocks
    })

def update_price(request):
    pass