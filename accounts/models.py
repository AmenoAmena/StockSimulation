from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone

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

    def get_total_stock_value(self):
        cache_key = f"user_{self.id}_total_stock_value"
        total_value = cache.get(cache_key)

        if total_value is None:
            total_value = 0
            stock_users = UserStock.objects.filter(user=self)
            for stock_user in stock_users:
                total_value += stock_user.quantity * stock_user.stock.price
            
            cache.set(cache_key, total_value, timeout=600)

        return total_value
        
class UserStock(models.Model):
    user = models.ForeignKey(stock_user, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"

class MoneyLog(models.Model):
    user = models.ForeignKey(stock_user, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.amount} at {self.timestamp}"