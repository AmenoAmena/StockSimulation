from django.db import models
from django.contrib.auth.models import AbstractUser
import yfinance as yf

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

    def update_price(self):
        ticker = yf.Ticker(self.symbol)
        try:
            latest_price = ticker.history(period="1m")['Close'].iloc[-1]
            self.price = round(latest_price, 2)
        except IndexError:
            self.price = 0.00

    def save(self, *args, **kwargs):
        if self.pk is not None:  # Only update price if the stock already exists
            self.update_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.symbol

class UserStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'stock')

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"
