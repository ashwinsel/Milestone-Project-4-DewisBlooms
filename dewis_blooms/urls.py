from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.index, name='homepage'),  # Home page
    path('search/', views.search, name='search'),  # Search functionality
    path('products/', include('products.urls')),  # Products app URLs
    path('accounts/', include('allauth.urls')),  # Authentication URLs
    path('bag/', include('shopping_bag.urls')),  # Shopping bag URLs
    path('checkout/', include('checkout.urls')), # Checkout URLs
    path('profile/', include('profiles.urls')), # User Profile URLs    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)