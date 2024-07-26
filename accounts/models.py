from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

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
    today_money = models.DecimalField(default=10000,decimal_places=2,max_digits=10)
    yesterday_money = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)

    def get_total_stock_value(self):
        total_value = 0
        stock_users = UserStock.objects.filter(user=self)
        for stock_user in stock_users:
            total_value += stock_user.quantity * stock_user.stock.price
        return total_value


    def change_money(self):
        self.yesterday_money = self.today_money
        self.today_money = self.money
        self.save()


class UserStock(models.Model):
    user = models.ForeignKey(stock_user, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"
