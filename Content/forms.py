from django import forms
from accounts.models import Stock

class StockTrade(forms.Form):
    ACTION_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    symbol = forms.ModelChoiceField(
        queryset=Stock.objects.all(), 
        to_field_name='symbol', 
        empty_label="Select a stock",
        label='Symbol'
    )
    action = forms.ChoiceField(choices=ACTION_CHOICES, label='Action')
    quantity = forms.IntegerField(min_value=1, label='Quantity')
