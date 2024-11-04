from django.urls import path
from . import views

app_name = 'shopping_bag'  

urlpatterns = [
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.shopping_cart, name='shopping_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]