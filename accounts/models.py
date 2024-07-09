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

    def get_total_stock_value(self):
        total_value = 0
        stock_users = UserStock.objects.filter(user=self)
        for stock_user in stock_users:
            total_value += stock_user.quantity * stock_user.stock.price
        return total_value

class UserStock(models.Model):
    user = models.ForeignKey(stock_user, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the object already exists
            existing_stock_user = UserStock.objects.filter(pk=self.pk).first()
            if existing_stock_user:
                # Handle case where quantity is updated
                quantity_difference = self.quantity - existing_stock_user.quantity
                if quantity_difference != 0:
                    # Update user money based on quantity difference
                    stock_price = self.stock.price
                    total_cost = stock_price * quantity_difference
                    if total_cost > 0 and self.user.money < total_cost:
                        raise ValidationError("Insufficient funds to buy stock.")
                    self.user.money -= total_cost
                    self.user.save()
                super().save(*args, **kwargs)
                return
        
        # Handle case where new stock is being added
        stock_price = self.stock.price
        total_cost = stock_price * self.quantity
        if self.user.money < total_cost:
            raise ValidationError("Insufficient funds to buy stock.")
        self.user.money -= total_cost
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"
