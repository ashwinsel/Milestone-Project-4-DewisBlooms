from django.urls import path
from . import views
from .views import view_bag, add_to_bag, clear_bag


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('clear/', clear_bag, name='clear_bag'),
]