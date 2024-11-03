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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)