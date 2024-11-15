from django.urls import path
from . import views
from shopping_bag.views import add_to_bag


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),    
    path('cart/', views.shopping_cart, name='shopping_cart'),
    path('add/<int:item_id>/', add_to_bag, name='add_to_bag'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]