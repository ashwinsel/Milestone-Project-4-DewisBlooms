from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product

def homepage(request):
    return HttpResponse("Welcome to Dewi's Blooms!")


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def search(request):
    # Placeholder logic for search functionality delete later

    return render(request, 'home/search_results.html')

def products_view(request):
    categories = Category.objects.all()  # Get all categories
    products_by_category = {
        category: Product.objects.filter(category=category)  # Group products by category
        for category in categories
    }
    return render(request, 'products.html', {'products_by_category': products_by_category, 'categories': categories})