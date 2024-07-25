from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import asyncio

class Stock(models.Model):
    SYMBOL_CHOICES = [
        ('AAPL', 'Apple Inc.'),
        ('MSFT', 'Microsoft Corporation'),
        ('AMZN', 'Amazon.com Inc.'),
        ('GOOGL', 'Alphabet Inc.'),
        ('TSLA', 'Tesla, Inc.'),
        ('META', 'Meta Platforms, Inc.'),
        ('NVDA', 'NVIDIA Corporation'),
        ('KO', 'Coca-Cola Company'),
        ('INTC', 'Intel Corporation'),
        ('V', 'Visa Inc.'),
    ]

    symbol = models.CharField(max_length=10, choices=SYMBOL_CHOICES, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.symbol

class stock_user(AbstractUser):
    money = models.DecimalField(default=10000.00, decimal_places=2, max_digits=10)
    current_and_yesterday_money = models.JSONField(default=list) 

    def get_total_stock_value(self):
        total_value = 0
        stock_users = UserStock.objects.filter(user=self)
        for stock_user in stock_users:
            total_value += stock_user.quantity * stock_user.stock.price
        return total_value


    def append_money(self):
        money = await asyncio.to_thread(self.get_total_stock_value)
        self.current_and_yesterday_money.append(money)
        if len(self.current_and_yesterday_money) > 2:
            self.current_and_yesterday_money = self.current_and_yesterday_money[-2:]



class UserStock(models.Model):
    user = models.ForeignKey(stock_user, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"
