from django.db import models
from django.contrib.auth.models import AbstractUser

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

    # Uncomment the methods below if you plan to use them for updating stock prices

    # def update_price(self):
    #     ticker = yf.Ticker(self.symbol)
    #     try:
    #         latest_price = ticker.history(period="1m")['Close'].iloc[-1]
    #         self.price = round(latest_price, 2)
    #     except IndexError:
    #         self.price = 0.00
    #
    # def save(self, *args, **kwargs):
    #     if self.pk is not None:  # Only update price if the stock already exists
    #         self.update_price()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.symbol


class stock_user(AbstractUser):

    money = models.DecimalField(default=10000.00,decimal_places=2,max_digits=10)

    def get_total_stock_value(self):
        total_value = 0
        user_stocks = UserStock.objects.filter(user=self)
        for user_stock in user_stocks:
            total_value += user_stock.quantity * user_stock.stock.price
        return total_value


class UserStock(models.Model):
    user = models.ForeignKey(stock_user, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the object is new
            existing_user_stock = UserStock.objects.filter(user=self.user, stock=self.stock).first()
            if existing_user_stock:
                existing_user_stock.quantity += self.quantity
                existing_user_stock.save()
                return  # Do not save the new instance, as we updated the existing one
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"
