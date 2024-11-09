from django.urls import path
from . import views
from .views import view_bag, add_to_bag, clear_bag


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('clear/', clear_bag, name='clear_bag'),
    path('update/<int:item_id>/', views.update_bag, name='update_bag'),
    path('remove/<int:item_id>/', views.remove_from_bag, name='remove_from_bag'),
]