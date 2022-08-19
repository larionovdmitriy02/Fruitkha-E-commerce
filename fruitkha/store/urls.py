from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('cart/', views.cart_page, name='cart_page'),
]
