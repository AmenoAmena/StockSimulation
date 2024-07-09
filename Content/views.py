from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import stock_user
from .prices import Price
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    user_instance = stock_user.objects.get(id=user.id)
    user_money = user_instance.get_total_stock_value() + user.money
    stock_value = user_instance.get_total_stock_value()
    user_cash = user.money
    made_money = user_money - 10000
    return render(request, 'Content/index.html', {
        'user_money': user_money,
        'stock_values':stock_value,
        'user_cash':user_cash,
        'made_money':made_money,
    })