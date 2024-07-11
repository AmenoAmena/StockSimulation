from django.urls import path
from . import views

app_name = "Content"

urlpatterns = [
    path('',views.index,name='index'),
    path('trade/',views.trade,name='trade'),
    path('market/',views.show_market,name='market'),
    path('update/price/new/prices/update/',views.update_price,name='update_price')
]