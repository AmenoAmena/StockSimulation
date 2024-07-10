from django.urls import path
from . import views

app_name = "Content"

urlpatterns = [
    path('',views.index,name='index'),
    path('trade/',views.trade,name='trade'),
]