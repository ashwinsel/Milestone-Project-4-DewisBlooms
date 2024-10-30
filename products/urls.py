from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/add/', views.add_to_cart, name='add_to_cart'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]