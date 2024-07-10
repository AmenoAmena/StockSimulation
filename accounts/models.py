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

#    def save(self, *args, **kwargs):
#        existing_stock_user = UserStock.objects.filter(user=self.user, stock=self.stock).first()
#        
#        if existing_stock_user:
#            quantity_difference = self.quantity
#        else:
#            quantity_difference = self.quantity
#
#        stock_price = self.stock.price
#        total_cost = stock_price * quantity_difference
#
#        if quantity_difference > 0 and self.user.money < total_cost:
#            raise ValidationError("Insufficient funds to buy stock.")
#        
#        if quantity_difference > 0:
#            self.user.money -= total_cost
#        else:
#            self.user.money += abs(total_cost)
#
#        self.user.save()
#
#        if existing_stock_user:
#            existing_stock_user.quantity += quantity_difference
#            UserStock.objects.filter(id=existing_stock_user.id).update(quantity=existing_stock_user.quantity)
#        else:
#            super().save(*args, **kwargs)
#
    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.quantity})"
