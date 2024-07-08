from django.contrib import admin
from .models import Stock,UserStock

# Register your models here.
admin.site.register(Stock)
admin.site.register(UserStock)
