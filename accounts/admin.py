from django.contrib import admin
from .models import Stock,UserStock,stock_user

# Register your models here.
admin.site.register(Stock)
admin.site.register(UserStock)
admin.site.register(stock_user)

